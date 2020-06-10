'''
โปรแกรม Master อย่างง่าย (ไม่มีการระบุ Address ของ Slave)
    1) ตรวจจับวัตถุด้วย Sensor แล้วทำการ Reject ชิ้นงานด้วย Actuator
    2) ส่งค่าที่ Sensor ตรวจจับวัตถุได้ (detection) ไปยัง Thingsboard
    3) ส่งค่าการ Reject ชิ้นงานไปยัง Thingsboard

คำสั่งของ Master
 0 = สั่งให้ Slave อ่านค่า Sensor จาก Plant Simulation แล้วส่งค่าดังกล่าวกลับมายัง Master
 1 = สั่งให้ Slave ควบคุม Actuator ใน Plant Simulation ให้ Linear Actuator มีสถานะ Deactive
 2 = สั่งให้ Slave ควบคุม Actuator ใน Plant Simulation ให้ Linear Actuator มีสถานะ Active
'''

import time
import serial
import paho.mqtt.client as mqtt

## กำหนดตัวแปร ##
# Thingsboard
THINGSBOARD_HOST	= "localhost"
THINGSBOARD_MQTT_PORT	= 1150
THINGSBOARD_TOKEN	= "ov6sFHmsVDKE5amQaHjC"

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

# เปิดใช้งาน Serial Port
print("Init Serial Port ...")
port = serial.Serial(port='COM2', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=0, xonxoff=0, rtscts=0, dsrdtr=0)

# ทำงานซ้ำตลอดเวลา
print ("Start main loop")
while True:

    # สั่งให้ Slave อ่านค่าจาก Sensor
    print("Request Reading ...")
    port.write(b'0')

    # รอการตอบกลับจาก Slave
    print("Waiting for Result from Slave ...")
    while port.inWaiting() == 0:
        time.sleep(0.01)

    # มีข้อมูลตอบกลับจาก Slave
    data    = b''
    while port.inWaiting() > 0:
        data = port.read(port.inWaiting())
        print("Result=" + str(data))

        # ตรวจสอบข้อมูลจาก Sensor ว่าตรวจพบวัตถุหรือไม่
        if data == b'1':    # พบวัตถุ
            time.sleep(0.1)
            # สั่งให้ Slave ควบคุม Actuator มีสถานะ Active
            print("Active")
            port.write(b'2')
            time.sleep(0.5)
            # สั่งให้ Slave ควบคุม Actuator มีสถานะ Dective
            print("Deactive")
            port.write(b'1')
            time.sleep(0.5)

            # ข้อมูลสำหรับส่งไปยัง Thingsboard อยู่ในรูปแบบ JSON
            # ส่งข้อมูลไปยัง Thingsboard ด้วย MQTT
            CLIENT.publish("v1/devices/me/telemetry", str("{detection:1, rejection:1}"))
        else:   # ไม่พบ
            # สั่งให้ Slave ควบคุม Actuator มีสถานะ Dective
            print("Deactive")
            port.write(b'1')
            time.sleep(0.1)

            # ข้อมูลสำหรับส่งไปยัง Thingsboard อยู่ในรูปแบบ JSON
            # ส่งข้อมูลไปยัง Thingsboard ด้วย MQTT
            CLIENT.publish("v1/devices/me/telemetry", str("{detection:0}"))

    print("")

CLIENT.loop_stop()
CLIENT.disconnect()
