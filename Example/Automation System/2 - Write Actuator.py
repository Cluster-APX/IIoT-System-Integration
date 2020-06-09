'''
โปรแกรม Master อย่างง่าย (ไม่มีการระบุ Address ของ Slave)

คำสั่งของ Master
 0 = สั่งให้ Slave อ่านค่า Sensor จาก Plant Simulation แล้วส่งค่าดังกล่าวกลับมายัง Master
 1 = สั่งให้ Slave ควบคุม Actuator ใน Plant Simulation ให้ Linear Actuator มีสถานะ Deactive
 2 = สั่งให้ Slave ควบคุม Actuator ใน Plant Simulation ให้ Linear Actuator มีสถานะ Active
'''

import time
import serial

# เปิดใช้งาน Com Port
port = serial.Serial(port='COM2', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=0, xonxoff=0, rtscts=0, dsrdtr=0)

def MyDelay(sec):
    # time.sleep(sec)
    pass

# Main Loop
print("Entering Main Loop ...")
while True:

    # สั่งให้ Slave ควบคุม Actuator มีสถานะ Dective
    print("Deactive")
    port.write(b'1')
    time.sleep(0.5)

    # สั่งให้ Slave ควบคุม Actuator มีสถานะ Active
    print("Active")
    port.write(b'2')
    time.sleep(0.5)

    print("")
