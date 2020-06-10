import time
import random
import paho.mqtt.client as mqtt

## VARIABLES ##
THINGSBOARD_HOST	= "localhost"
THINGSBOARD_MQTT_PORT	= 1150
THINGSBOARD_TOKEN	= "wNk9wsgtDCIOlZS3tVwc"

IsMqttConnect	= False

CLIENT	= mqtt.Client()

## FUNCTION ##

def MyMqttOnConnect(client, userdata, flag, rc):
	print(">MyMqttOnConnect")

	global CLIENT, IsMqttConnect
	IsMqttConnect	= True

def MyMqttOnDisconnect(client, userdata, rc):
	print(">MyMqttOnDisconnect")

	global IsMqttConnect
	IsMqttConnect	= False

## MAIN ##

print("Init MQTT")
CLIENT.on_connect	= MyMqttOnConnect
CLIENT.on_disconnect	= MyMqttOnDisconnect
CLIENT.username_pw_set(THINGSBOARD_TOKEN)
CLIENT.loop_start()

print("Connecting to thingsboard ...")
CLIENT.connect_async(THINGSBOARD_HOST, THINGSBOARD_MQTT_PORT)
while IsMqttConnect == False:
	time.sleep(0.5)

print ("Start main loop")
while True:
	value1	= random.uniform(-50, 50)
	message	= "{temperature:" + str(value1) + "}"
	print("message=" + str(message))

	CLIENT.publish("v1/devices/me/telemetry", str(message))

	time.sleep(1)

CLIENT.loop_stop()
CLIENT.disconnect()