from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import time
import subprocess
import logging
import webbrowser
import configparser


# webbrowser.open("http://127.0.0.1:5000")
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

@app.route('/edit_config', methods=['GET', 'POST'])
def edit_config():
    config = load_config()  # Load the configuration

    if request.method == 'POST':
        # Process the configuration changes here
        for field_name, new_value in request.form.items():
            # Skip CSRF token and other form fields
            if field_name.startswith('_'):
                continue

            # Split field name into section and option
            field_parts = field_name.split('_', 1)
            
            if len(field_parts) == 2:
                section, option = field_parts
                # Save the configuration changes dynamically
                save_config_changes(section, option, new_value)
            else:
                # Handle the case where the field name doesn't contain an underscore
                print(f"Invalid field name: {field_name}")

        # Redirect to the index page
        return redirect(url_for('index'))

    return render_template('edit_config.html', config=config)

@app.route('/sitelistgen')
def sitelistgen():
    return render_template('sitelistgen.html')



def load_config():
    config = configparser.ConfigParser()
    config_path = "config/config.ini"

    if not os.path.exists(config_path):
        # Handle the case where the config file doesn't exist
        return None

    config.read(config_path)
    return config

def save_config_changes(section, option_name, new_value):
    config_path = "config/config.ini"
    config = configparser.ConfigParser()
    config.read(config_path)

    # Convert the new value to a string
    new_value = str(new_value)

    # Update the specified section and option
    config.set(section, option_name, new_value)

    print(f"Configuration change saved: {section}.{option_name} - {new_value}")
    print(f"Config file path: {config_path}")

    with open(config_path, 'w') as config_file:
        config.write(config_file)

    print(f"Config content after changes:\n{open(config_path).read()}")

    # Save the changes back to the config object (optional)
    config.read(config_path)



def process_data(text1,options=""):
    # Path to your brib.py script
    brib_script_path = "brib.py"
    
    target = text1
    
    file_path = 'captured/.txt'
    # Open the file and clear it
    try:
            with open(file_path, 'w') as file:
                # Read the contents of the file
                file.write("")
    except FileNotFoundError:
                print(f"The file at {file_path} was not found.")
    except Exception as e:
            print(f"An error occurred: {e}")
    
    try:
        # Execute the script with subprocess.run
        if os.name == "nt":
            if options == "":
                result = subprocess.run(['python.exe', brib_script_path, '-u', str(target),'-s'], capture_output=True, text=True, check=True)
            else:    
              result = subprocess.run(['python.exe', brib_script_path, '-u', str(target),'-s', str(options)], capture_output=True, text=True, check=True)
        else:
            if options == "":
                result = subprocess.run(['python3', brib_script_path, '-u', str(target), '-s'], capture_output=True, text=True, check=True)
            else:    
              result = subprocess.run(['python3', brib_script_path, '-u', str(target), '-s',str(options)], capture_output=True, text=True, check=True)
         # Specify the file path
        

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
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)