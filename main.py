from flask import render_template, request, redirect, url_for, session, flash
from flask import Flask, render_template;
from os import environ
import json
import requests
from datetime import datetime, date, time, timedelta
API_KEY = 'AIzaSyBRxaYSL5HeGOg74xgDbJ6jjbIO0RX64c0'

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
	f=open("file.txt", 'r+').read()
	count_data=json.loads(f)
	j=0
	waypoints= waypoint_str.split('|')
	wayp={}
	for i in js['routes'][0]['legs']:
		if(j<len(waypoints)):
			wayp[waypoints[j]] = total_dur
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
	start_time = str(str(h)+":"+str(m));
	for i in wayp:
		#time at waypoint 
		tw = t+wayp[i]
		cap=5
		if(m>0 and m<=5):
			if(count_data[i][str(h)+":00-"+str(h)+":05"]>cap):
				m=m-5
				if(m<0):
					h-=1
					m=60+m
			else:
				count_data[i][str(h)+":00-"+str(h)+":05"]+=1
		elif(m>5 and m<=10):
			if(count_data[i][str(h)+":05-"+str(h)+":10"]>cap):
				m=m-5
				if(m<0):
					h-=1
					m=60+m
			else:
				count_data[i][str(h)+":05-"+str(h)+":10"]+=1
		elif(m>10 and m<=15):
			if(count_data[i][str(h)+":10-"+str(h)+":15"]>cap):
				m=m-5
				if(m<0):
					h-=1
					m=60+m
			else:
				count_data[i][str(h)+":10-"+str(h)+":15"]+=1
		elif(m>15 and m<=20):
			if(count_data[i][str(h)+":15-"+str(h)+":20"]>cap):
				m=m-5
				if(m<0):
					h-=1
					m=60+m
			else:
				count_data[i][str(h)+":15-"+str(h)+":20"]+=1
		elif(m>20 and m<=25):
			if(count_data[i][str(h)+":20-"+str(h)+":25"]>cap):
				m=m-5
				if(m<0):
					h-=1
					m=60+m
			else:
				count_data[i][str(h)+":20-"+str(h)+":25"]+=1
		elif(m>25 and m<=30):
			if(count_data[i][str(h)+":25-"+str(h)+":30"]>cap):
				m=m-5
				if(m<0):
					h-=1
					m=60+m
			else:
				count_data[i][str(h)+":25-"+str(h)+":30"]+=1
		elif(m>30 and m<=35):
			if(count_data[i][str(h)+":30-"+str(h)+":35"]>cap):
				m=m-5
				if(m<0):
					h-=1
					m=60+m
			else:
				count_data[i][str(h)+":30-"+str(h)+":35"]+=1
		elif(m>35 and m<=40):
			if(count_data[i][str(h)+":35-"+str(h)+":40"]>cap):
				m=m-5
				if(m<0):
					h-=1
					m=60+m
			else:
				count_data[i][str(h)+":35-"+str(h)+":40"]+=1
		elif(m>40 and m<=45):
			if(count_data[i][str(h)+":40-"+str(h)+":45"]>cap):
				m=m-5
				if(m<0):
					h-=1
					m=60+m
			else:
				count_data[i][str(h)+":40-"+str(h)+":45"]+=1
		elif(m>45 and m<=50):
			if(count_data[i][str(h)+":45-"+str(h)+":50"]>cap):
				m=m-5
				if(m<0):
					h-=1
					m=60+m
			else:
				count_data[i][str(h)+":45-"+str(h)+":50"]+=1
		elif(m>50 and m<=55):
			if(count_data[i][str(h)+":50-"+str(h)+":55"]>cap):
				m=m-5
				if(m<0):
					h-=1
					m=60+m
			else:
				count_data[i][str(h)+":50-"+str(h)+":55"]+=1
		elif(m>55 and m<=60):
			if(count_data[i][str(h)+":55-"+str(h+1)+":00"]>cap):
				m=m-5
				if(m<0):
					h-=1
					m=60+m
			else:
				count_data[i][str(h)+":55-"+str(h+1)+":00"]+=1
	f=open("file.txt", 'w')
	start_time = str(str(h)+":"+str(m));
	f.write(json.dumps(count_data))
	return start_time;


HOST = environ.get('SERVER_HOST', 'localhost')
#app.secret_key = "SuPeR_SeCReT_KeY"
try:
	PORT = int(environ.get('SERVER_PORT', '5555'))
except ValueError:
	PORT = 5555
app.run(HOST, PORT, debug=True, threaded=True)

