from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response
import os
import time
import bandwidthModifier

app = Flask(__name__)

@app.route('/')
def index():
	return "<h1>This Works</h1>"

@app.route('/grabFile/<fileName>', method="POST")
def grabFile(fileName):
	return "<h1>This Works</h1>"

@app.route('/playAudio/<audioFile>')
def playAudio(audioFile):
	return "<h1>This Works</h1>"

if __name__ == "__main__":
	app.run()
