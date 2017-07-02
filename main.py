from flask import render_template, request, redirect, url_for, session, flash
import json

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', user=user)