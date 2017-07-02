from flask import render_template, request, redirect, url_for, session, flash
from flask import Flask, render_template;
from os import environ
import json

app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')
	
HOST = environ.get('SERVER_HOST', 'localhost')
#app.secret_key = "SuPeR_SeCReT_KeY"
try:
	PORT = int(environ.get('SERVER_PORT', '5555'))
except ValueError:
	PORT = 5555
app.run(HOST, PORT, debug=True, threaded=True)

