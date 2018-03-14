from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response
import os
import time
import bandwidthModifier
from categorizeFiles import *
DIRECTORY = "Mp3/"
app = Flask(__name__)

@app.route('/')
def index():
	database = []
	# {Descrition: blah, "lengths": {3: {},  5: {}, 10: {} }}
	allInfo = extractAll(DIRECTORY)
	for i in range(categorizeFiles(DIRECTORY)):
		day = i + 1
		tempInfo = {"Description": "Basics Day {}".format(day), "Files": []}
		for val in allInfo:
			if val["Day"] == day:
				time = val["Time"]
				fileName = val["FileName"]
				tempInfo["Files"].append({"Time": time, "Filename": fileName})
		database.append(tempInfo)
	return render_template("index.html", DATABASE=database)

@app.route('/grabFile/<fileName>', methods=["POST"])
def grabFile(fileName):
	# This function grabs the file/JSON indicating file splits
	return "<h1>This Works</h1>"

@app.route('/playAudio/<audioFile>')
def playAudio(audioFile):
	# This function plays the audio
	return "<h1>This Works</h1>"

if __name__ == "__main__":
	app.run()



