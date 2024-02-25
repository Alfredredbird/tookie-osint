from flask import Flask, render_template, request, jsonify
import os
import time

app = Flask(__name__)

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
        entered_text1 = request.form.get('text_input1', '')  # Use get to avoid KeyError
        save_to_history(entered_text1)  # Save the entered text to history file
        result_text = process_data(entered_text1)
        # return render_template('index.html', result=result_text)
        # Instead of rendering a template, return JSON
        return jsonify({'result': result_text})

    return render_template('index.html', result=None)

def process_data(text1):
    # Simulate processing time
    time.sleep(3)

    # Combine the entered text
    result_text = f'Entered Text: {text1}'
    return result_text

def save_to_history(entered_text):
    history_file_path = os.path.join(base_directory, 'storage/history.txt')
    with open(history_file_path, 'a') as history_file:
        history_file.write(entered_text + '\n')

if __name__ == '__main__':
    app.run(debug=True)