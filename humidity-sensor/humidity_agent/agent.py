import json
from datetime import datetime

import serial
from humidity_agent.usb import get_adafruit_feather, get_usb_devices
from influxdb import InfluxDBClient


def influxBody(measurements):
    json_body = []
    current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    for key, value in measurements.items():
        json_part = {
            "measurement": key,
            "time": current_time,
            "fields": {"value": value},
        }

        json_body.append(json_part)

    return json_body


def run():
    # device_path = get_adafruit_feather(get_usb_devices())
    device_path = r"/dev/ttyACM0"
    ser = serial.Serial(device_path, 115200)

    client = InfluxDBClient("localhost", 8086, "admin", "admin", "apartment")

    while 1:
        try:
            serialData = ser.readline()
            data = json.loads(ser.readline())

            client.write_points(influxBody(data))

        except Exception as e:
            print(e)
