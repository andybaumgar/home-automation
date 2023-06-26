import serial
import json
from datetime import datetime
import sys, os
import paho.mqtt.client as mqtt #import the client1
import time

broker_address="192.168.0.153" 
#broker_address="iot.eclipse.org" #use external broker
mqtt_client = mqtt.Client("P1") #create new instance
mqtt_client.connect(broker_address) #connect to broker

while(True):
    mqtt_client.publish("house/main-light",125) #publish
    time.sleep(5)