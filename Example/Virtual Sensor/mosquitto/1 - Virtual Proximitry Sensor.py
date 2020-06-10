import os
import time
import random

print ("Start main loop")

while True:
	value1	= random.randint(0, 1)
	if value1 == 1:
		message	= "\"{state:1}\""
	else:
		message	= "\"{state:0}\""

	print("message=" + str(message))

	os.system("mosquitto_pub -p 1150 -t v1/devices/me/telemetry -u 1F4Xuz4v0296LPkSUwk3 -m " + str(message))
	time.sleep(1)