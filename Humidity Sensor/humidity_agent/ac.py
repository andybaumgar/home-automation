import config
from config import on_temp
import paho.mqtt.client as mqtt
import requests

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("apartment/temperature")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    respond(msg.payload)

def setup():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(config.broker_address, 1883, 60)

    client.loop_forever()

def ac_request(state):
    onUrl = 'https://maker.ifttt.com/trigger/ac_on/with/key/bOoYtkIEnZI6kUt_XWc4ay'
    offUrl = 'https://maker.ifttt.com/trigger/ac_off/with/key/bOoYtkIEnZI6kUt_XWc4ay'
    url = onUrl if state=="on" else offUrl
    r = requests.get(url)

def respond(temp):
    global ac_on
    temp = float(temp)
    if(temp > on_temp and not ac_on):
        ac_request("on")
        ac_on = True 
    if(temp <= config.off_temp and ac_on):
        ac_request("off")
        ac_on = False

if __name__ == "__main__":
    ac_request("off")
    ac_on = False
    setup()