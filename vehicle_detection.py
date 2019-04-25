# -*- coding: utf-8 -*-
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
SHADOW_CLIENT = "myShadowClient"
HOST_NAME = "yourhostname-ats.iot.us-east-1.amazonaws.com"
ROOT_CA = "AmazonRootCA1.pem"
PRIVATE_KEY = "yourkeyid-private.pem.key"
CERT_FILE = "yourkeyid-certificate.pem.crt.txt"
SHADOW_HANDLER = "MyRPi"

import time
import cv2
print(cv2.__version__)
import io
import numpy
import board
import busio
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
    
    #cv2.imshow('video', img)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
