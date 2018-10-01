import time
import paho.mqtt.client as mqtt
import ssl
import json


def update():	
	def on_connect(client, userdata, flags, rc):
   		print("Connected with result code "+str(rc))


	client = mqtt.Client()
	client.on_connect = on_connect
	client.tls_set(ca_certs='/home/pi/beProject/CA-cert.pem.crt', certfile='/home/pi/beProject/Raspberry-pi.cert.pem', keyfile='/home/pi/beProject/Raspberry-pi.private.key', tls_version=ssl.PROTOCOL_SSLv23)
	client.tls_insecure_set(True)
	client.connect("a26q0kn0yhymmo.iot.us-west-2.amazonaws.com", 8883, 60) 

	key0='slno'
	value0=34
	
#	print value0
	
	key1='bpm'
	value1=77#str(bpm)


	key2='temp'
	value2=33#str(temp)

	msg={key0:value0,key1:value1,key2:value2}

	jmsg=json.dumps(msg)
	client.reconnect()
	client.publish("patient/diagdata", payload=jmsg , qos=1, retain=False)
	return client
#def readfile():
#	f=open("slno.txt","r")
#	i=f.read(4)
#	i=int(i)
#	f.close()
#	f=open("slno.txt","w")
#	i=i+1
#	f.write('{:04d}'.format(i))
#	f.close()
#	return i-1
#update(34,76)


while True:
 incode=raw_input("Would you like to send data now to cloud? Y/N\nPress R to reconnect\n")
 if incode=='y':
	cli=update()    	
 elif incode=='r':
	cli.reconnect()
 else:
	print"wrong input"

    
#client.loop_forever()
