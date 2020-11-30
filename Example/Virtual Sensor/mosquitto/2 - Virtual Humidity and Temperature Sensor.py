import os
import time
import random

print ("Start main loop")

while True:
	value1	= random.uniform(-50, 50)
	value2	= random.uniform(0, 100)
	message	= "\"{temperature:" + str(value1) + ", humidity:" + str(value2) + "}\""

	print("message=" + str(message))

	os.system("mosquitto_pub -p 1150 -t v1/devices/me/telemetry -u bKEbVF1V9mIZ3NKs2lZl -m " + str(message))
	time.sleep(1)