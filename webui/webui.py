from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import time
import subprocess
import logging
import webbrowser
import configparser
import threading
import uuid

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

jobs = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        entered_text1 = request.form.get('text_input1')
        entered_options1 = request.form.get('text_input2')

        job_id = str(uuid.uuid4())
        jobs[job_id] = {"status": "inprogress", "result": None}

        # Run in background
        thread = threading.Thread(target=run_job, args=(job_id, entered_text1, entered_options1))
        thread.start()

        return jsonify({"job_id": job_id, "status": "inprogress"})

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





def process_data(job_id, text1, options=""):
    brib_script_path = "brib.py"

    if os.name == "nt":
        cmd = ['python.exe', brib_script_path, '-u', str(text1), '-s']
        if options: 
            cmd.append(str(options))
    else:
        cmd = ['python3', brib_script_path, '-u', str(text1), '-s']
        if options: 
            cmd.append(str(options))

    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    try:
        process.stdin.write("n\nn")
        process.stdin.flush()
    except Exception:
        pass
    finally:
        if process.stdin:
            process.stdin.close()

    jobs[job_id]["result"] = ""  # initialize
    for line in iter(process.stdout.readline, ''):
        line = line.strip()
        if line:
            print(f"[LIVE] {line}")
            jobs[job_id]["result"] += line + "\n"   # keep appending live
    process.stdout.close()

    process.wait()
    jobs[job_id]["status"] = "done"


def save_to_history(entered_text):
    history_file_path = os.path.join(base_directory, 'storage/history.txt')
    with open(history_file_path, 'a') as history_file:
        history_file.write(entered_text + '\n')

@app.route('/api/<job_id>', methods=['GET'])
def get_job(job_id):
    job = jobs.get(job_id)
    if not job:
        return jsonify({"error": "Job not found"}), 404
    return jsonify({
    "status": job["status"],
    "result": job["result"],
    "done": job["status"] == "done"
})


def run_job(job_id, text1, options=""):
    try:
        process_data(job_id, text1, options)
    except Exception as e:
        jobs[job_id]["status"] = "error"
        jobs[job_id]["result"] = str(e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=False)
