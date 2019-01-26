from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('index.html')

@app.route('/resume')
def resume():
	return render_template('resume.html')

@app.route('/hello_world')
def hello_world():
	return 'Hello World!'
