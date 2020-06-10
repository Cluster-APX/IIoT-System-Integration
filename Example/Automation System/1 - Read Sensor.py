'''
โปรแกรม Master อย่างง่าย (ไม่มีการระบุ Address ของ Slave)
    อ่านค่า Sensor ผ่าน Slave แล้วแสดงค่าของ Sensor ใน Terminal ของ Master

คำสั่งของ Master
 0 = สั่งให้ Slave อ่านค่า Sensor จาก Plant Simulation แล้วส่งค่าดังกล่าวกลับมายัง Master
 1 = สั่งให้ Slave ควบคุม Actuator ใน Plant Simulation ให้ Linear Actuator มีสถานะ Inactive
 2 = สั่งให้ Slave ควบคุม Actuator ใน Plant Simulation ให้ Linear Actuator มีสถานะ Active
'''

import struct
import serial
import time

# เปิดใช้งาน Serial Port
print("Init Serial Port ...")
port = serial.Serial(port='COM2', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=0, xonxoff=0, rtscts=0, dsrdtr=0)

# Main Loop
print("Entering Main Loop ...")
while True:

    # สั่งให้ Slave อ่านค่าจาก Sensor
    print("Request Reading ...")
    port.write(b'0')

    # รอการตอบกลับจาก Slave
    print("Waiting for Result from Slave ...")
    while port.inWaiting() == 0:
        time.sleep(0.01)

    # มีข้อมูลตอบกลับจาก Slave
    while port.inWaiting() > 0:
        data = port.read(port.inWaiting())
        print("Result=" + str(data))

    time.sleep(0.25)
    print("")