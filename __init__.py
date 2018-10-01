from flask import Flask, render_template, request
import temp
import heart
import RPi.GPIO as gpio
import time
import pipython
import messagemod
app=Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html",dist=0)


@app.route("/collect", methods=['POST','GET'])
def collect():
	temperature = temp.readtemp()
	bpmheart=heart.readtemp()
	pipython.update(temperature,bpmheart)
	messagemod.message(bpmheart,temperature)
	return render_template("index.html",temp=temperature,bpm=bpmheart)


if __name__=="__main__":
	temp.initpins()
	heart.initpins()
	app.run(debug=True, host='0.0.0.0', port=80)
