from flask import Flask, render_template, request, jsonify
import os
import time
import subprocess
import logging
import webbrowser

webbrowser.open("http://127.0.0.1:5000")
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
# Define the directory for file storage and templates
base_directory = os.path.dirname(os.path.abspath(__file__))
storage_directory = os.path.join(base_directory, 'storage')
template_directory = os.path.join(base_directory, 'templates')
# Ensure the storage directory exists
os.makedirs(storage_directory, exist_ok=True)
# Set the template folder
app.template_folder = template_directory



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        entered_text1 = request.form.get('text_input1')  # Use get to avoid KeyError
        entered_options1 = request.form.get('text_input2')
        app.logger.debug(f'logged input: {entered_text1}')
        app.logger.debug(f'logged options: {entered_options1}')
        save_to_history(entered_text1)  # Save the entered text to history file
        out_put = process_data(entered_text1,entered_options1)
        # return render_template('index.html', result=result_text)
        # Instead of rendering a template, return JSON
        return jsonify({'result': out_put})

    return render_template('index.html', result=None)

def process_data(text1,options=""):
    # Path to your brib.py script
    brib_script_path = "brib.py"
    
    try:
        # Execute the script with subprocess.run
        if os.name == "nt":
         result = subprocess.run(['python.exe', brib_script_path, '-u', text1,'-s', options], capture_output=True, text=True, check=True)
        else:
          result = subprocess.run(['python3', brib_script_path, '-u', text1, '-s',options], capture_output=True, text=True, check=True)
         # Specify the file path
        file_path = 'captured/.txt'

        # Open the file in read mode ('r')
        try:
            with open(file_path, 'r') as file:
                # Read the contents of the file
                file_contents = file.read()

                # Print the contents
                print(file_contents)
                result_text = file_contents
        except FileNotFoundError:
                print(f"The file at {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    except subprocess.CalledProcessError as e:
        # If an error occurs, print both stdout and stderr
        result_text = f"Error running script:\nSTDOUT: {e.stdout}\nSTDERR: {e.stderr}"
    
    return result_text

def save_to_history(entered_text):
    history_file_path = os.path.join(base_directory, 'storage/history.txt')
    with open(history_file_path, 'a') as history_file:
        history_file.write(entered_text + '\n')

if __name__ == '__main__':
    app.run(debug=False)