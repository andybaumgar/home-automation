import serial
import json
from influxdb import InfluxDBClient
from datetime import datetime
import sys, os
import paho.mqtt.client as mqtt #import the client1
import config

def influxBody(measurements):
	json_body = []
	current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

	for key, value in measurements.items():
		json_part = {
			"measurement": key,
			"time": current_time,
			"fields": {
				"value": value
			}
		}

		json_body.append(json_part)

	return json_body

ser = serial.Serial(config.usbDevice, 115200)

client = InfluxDBClient('localhost', 8086, 'admin', 'admin', 'apartment')

# mqtt_client = mqtt.Client("P1") #create new instance
# mqtt_client.connect(config.broker_address) #connect to broker

while 1 :
	try:
		serialData = ser.readline()
		data = json.loads(ser.readline())

		client.write_points(influxBody(data))

		# mqtt_client.publish("apartment/temperature",data.temperature)
		# mqtt_client.publish("apartment/temperature",data["temperature"])
		# mqtt_client.publish("apartment/humidity",data["humidity"])

	except Exception as e:
		print(e)
