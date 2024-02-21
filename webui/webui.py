from flask import Flask, render_template, request
import os

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
        entered_text = request.form['text_input']
        save_to_file(entered_text)
    return render_template('index.html')

def save_to_file(text):
    # Generate a unique filename (you can use a better method if needed)
    filename = os.path.join(storage_directory, f"{hash(text)}.txt")
    
    # Save the text to the file
    with open(filename, 'w') as file:
        file.write(text)

if __name__ == '__main__':
    app.run(debug=True)
