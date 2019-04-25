# -*- coding: utf-8 -*-
#AWSIoTPythonSDK.MQTTLib.AWSIoTMQTTClient.disableMetricsCollection()
#AWSIoTPythonSDK.MQTTLib.AWSIoTMQTTShadowClient.disableMetricsCollection()
#import subprocess
#subprocess.call(['./start.sh'])

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
SHADOW_CLIENT = "myShadowClient"
HOST_NAME = "ayrlsz5dvz4iu-ats.iot.us-west-2.amazonaws.com"
ROOT_CA = "root-CA.crt"
PRIVATE_KEY = "raspi.private.key"
CERT_FILE = "raspi.cert.pem"
SHADOW_HANDLER = "MyRPi"
import time
import cv2
print(cv2.__version__)
import io
import numpy
import board
import busio

def myShadowUpdateCallback(payload, responseStatus, token):
  print()
  print('UPDATE: $aws/things/' + SHADOW_HANDLER +
    '/shadow/update/#')
  print("payload = " + payload)
  print("responseStatus = " + responseStatus)
  print("token = " + token)

# Create, configure, and connect a shadow client.
myShadowClient = AWSIoTMQTTShadowClient(SHADOW_CLIENT)
myShadowClient.configureEndpoint(HOST_NAME, 8883)
myShadowClient.configureCredentials(ROOT_CA, PRIVATE_KEY,CERT_FILE)
myShadowClient.configureConnectDisconnectTimeout(10)
myShadowClient.configureMQTTOperationTimeout(5)
myShadowClient.connect()


i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)

cascade_src = 'cars.xml'
#video_src = VideoStream(0).start()
video_src = 'dataset/video2.avi'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        if chan.value > 3000:
            print("Polluter found")
            cv2.imwrite("frame%d.jpg" % time.time(), img)
            myDeviceShadow.shadowUpdate('{"state":{"reported":{"Polluter":"Detected"}}}', myShadowUpdateCallback, 5)
    
    #cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
