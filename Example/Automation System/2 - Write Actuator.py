'''
โปรแกรม Master อย่างง่าย (ไม่มีการระบุ Address ของ Slave)
    ควบคุม Actuator ผ่าน Slave ให้มีสถานะ Active และ Inactive ทุก ๆ 1 วินาที

คำสั่งของ Master
 0 = สั่งให้ Slave อ่านค่า Sensor จาก Plant Simulation แล้วส่งค่าดังกล่าวกลับมายัง Master
 1 = สั่งให้ Slave ควบคุม Actuator ใน Plant Simulation ให้ Linear Actuator มีสถานะ Inactive
 2 = สั่งให้ Slave ควบคุม Actuator ใน Plant Simulation ให้ Linear Actuator มีสถานะ Active
'''

import time
import serial

# เปิดใช้งาน Serial Port
print("Init Serial Port ...")
port = serial.Serial(port='COM2', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=0, xonxoff=0, rtscts=0, dsrdtr=0)

# Main Loop
print("Entering Main Loop ...")
while True:

    # สั่งให้ Slave ควบคุม Actuator มีสถานะ Inactive
    print("Inactive")
    port.write(b'1')
    time.sleep(0.5)

    # สั่งให้ Slave ควบคุม Actuator มีสถานะ Active
    print("Active")
    port.write(b'2')
    time.sleep(0.5)

    print("")
