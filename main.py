from flask import render_template, request, redirect, url_for, session, flash
from flask import Flask, render_template;
from os import environ
import json
import requests
from datetime import datetime, date, time, timedelta
API_KEY = 'AIzaSyDGHK2Revq2_iocE6G4iKDtkoqltMTbuIg'


app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/update',methods=['POST'])
def update():
	start=request.json['start']
	end=request.json['end']
	times=request.json['time']
	checks=request.json['checks'].split("&")
	res=logic(start,end,times,checks)
	temp = res
	
	return res


def logic(start,end,times,checks):
	origin = '+'.join(start.split())
	dest = '+'.join(end.split())
	d = date.today()
	t = time(0,0)
	dt = datetime.combine(d,t)
	print(dt)
	dt = int(dt.timestamp())+ 24*60*60
	API_KEY = 'AIzaSyBRxaYSL5HeGOg74xgDbJ6jjbIO0RX64c0'
	# for i in checks:
	# 	if(i=="slk"):
	# 		res=
	# 	elif(i=="blr" && i==0)
	# 		waypoint_str+="|Bellandur"
	j=1;
	waypoint_str=''
	for i in checks:
		if(i=="slk"):
			waypoint_str+="Silk+Board"
			j=0
		elif(i=="blr" and j==0):
			waypoint_str+="|Bellandur"
		elif(i=="blr" and j==1):
			waypoint_str+="Bellandur"
	url = 'https://maps.googleapis.com/maps/api/directions/json?units=metric&origin='+origin+'&destination='+dest+'&arrival_time='+str(dt)+'&key='+API_KEY+'&waypoints=optimize:true|'+waypoint_str
	response = requests.get(url)
	js = json.loads(response.text)
	# print(js)
	total_dur=0
	# f=open("file.txt",'w+')
	# js=json.loads(f.read())
	j=0
	for i in js['routes'][0]['legs']:
		print(j)
		j=j+1
		total_dur+=i['duration']['value']
		print(total_dur)
	print(len(js['routes'][0]['legs']))
	# duration=js['rows'][0]['elements'][0]['duration']['value']
	duration=total_dur
	# print "duration"
	# x=datetime.strptime(times,"%H:%M")
	t= times.split(":")
	t = int(t[0])*60*60+int(t[1])*60 - int(duration)
	h = int(t%86400/3600)
	m = int( t%3600 /60)
	return str(str(h)+":"+str(m));


HOST = environ.get('SERVER_HOST', 'localhost')
#app.secret_key = "SuPeR_SeCReT_KeY"
try:
	PORT = int(environ.get('SERVER_PORT', '5555'))
except ValueError:
	PORT = 5555
app.run(HOST, PORT, debug=True, threaded=True)

