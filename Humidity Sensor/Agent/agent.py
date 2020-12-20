import serial
import json
from influxdb import InfluxDBClient
from datetime import datetime

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

configFile = os.path.join(os.path.dirname(sys.argv[0]), 'config.json')

with open(configFile) as f:
  config = json.load(f)

ser = serial.Serial(config['usbDevice'], 115200)

client = InfluxDBClient('localhost', 8086, 'admin', 'admin', 'apartment')

while 1 :
	try:
		serialData = ser.readline()
		data = json.loads(ser.readline())

		client.write_points(influxBody(data))

	except Exception as e:
		print(e)
