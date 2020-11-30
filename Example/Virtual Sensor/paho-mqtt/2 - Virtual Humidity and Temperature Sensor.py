import time
import random
import paho.mqtt.client as mqtt

## กำหนดตัวแปร ##
# Thingsboard
THINGSBOARD_HOST	= "localhost"
THINGSBOARD_MQTT_PORT	= 1150
THINGSBOARD_TOKEN	= "bKEbVF1V9mIZ3NKs2lZl"

# MQTT
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

## เริ่มโปรแกรมหลัก ##
# กำหนด Callback ของ MQTT
print("Init MQTT")
CLIENT.on_connect	= MyMqttOnConnect
CLIENT.on_disconnect	= MyMqttOnDisconnect
CLIENT.username_pw_set(THINGSBOARD_TOKEN)
CLIENT.loop_start()

# เริ่มเชื่อมต่อ Thingsboard ด้วย MQTT
print("Connecting to thingsboard ...")
CLIENT.connect_async(THINGSBOARD_HOST, THINGSBOARD_MQTT_PORT)
while IsMqttConnect == False:
	time.sleep(0.5)

# ทำงานซ้ำตลอดเวลา
print ("Start main loop")
while True:
	value1	= random.uniform(-50, 50)
	value2	= random.uniform(0, 100)
	# ข้อมูลสำหรับส่งไปยัง Thingsboard อยู่ในรูปแบบ JSON
	message	= "{temperature:" + str(value1) + ", humidity:" + str(value2) + "}"
	print("message=" + str(message))

	# ส่งข้อมูลไปยัง Thingsboard ด้วย MQTT
	CLIENT.publish("v1/devices/me/telemetry", str(message))

	time.sleep(1)

CLIENT.loop_stop()
CLIENT.disconnect()