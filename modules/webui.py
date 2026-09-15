import os
import json
import requests
import re
from flask import Flask
import time


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/auth")
def web_auth():
    return "<p>Hello, World!</p>"


def run_webui():
    app.run()
