import os
import time
import random

print ("Start main loop")

while True:
	value1	= random.uniform(-50, 50)
	message	= "\"{temperature:" + str(value1) + "}\""

	print("message=" + str(message))

	os.system("mosquitto_pub -p 1150 -t v1/devices/me/telemetry -u wNk9wsgtDCIOlZS3tVwc -m " + str(message))
	time.sleep(1)