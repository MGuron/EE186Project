# -*- coding: utf-8 -*-


from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient #imports AWS IoT SDK, defines necessary file names and locations
SHADOW_CLIENT = "myShadowClient"
HOST_NAME = "ayrlsz5dvz4iu-ats.iot.us-west-2.amazonaws.com"
ROOT_CA = "root-CA.crt"
PRIVATE_KEY = "raspi.private.key"
CERT_FILE = "raspi.cert.pem"
SHADOW_HANDLER = "MyRPi"
import time
import cv2#openCV imports and startup
print(cv2.__version__)
import io
import numpy
import board
import busio

#import subprocess
#subprocess.call(['./start.sh'])#starts AWS IoT server connection, possibly not necessary

#AWSIoTPythonSDK.MQTTLib.AWSIoTMQTTClient.disableMetricsCollection()
#AWSIoTPythonSDK.MQTTLib.AWSIoTMQTTShadowClient.disableMetricsCollection()

def myShadowUpdateCallback(payload, responseStatus, token):#method to update AWS shadow client
  print()
  print('UPDATE: $aws/things/' + SHADOW_HANDLER +
    '/shadow/update/#')
  print("payload = " + payload)
  print("responseStatus = " + responseStatus)
  print("token = " + token)

# Create, configure, and connect a shadow client.
#myShadowClient = AWSIoTMQTTShadowClient(SHADOW_CLIENT)
#myShadowClient.configureEndpoint(HOST_NAME, 8883)
#myShadowClient.configureCredentials(ROOT_CA, PRIVATE_KEY,CERT_FILE)
#myShadowClient.configureConnectDisconnectTimeout(10)
#myShadowClient.configureMQTTOperationTimeout(5)
print("Here")
#myShadowClient.connect()


i2c = busio.I2C(board.SCL, board.SDA)#ADS 1115 imports and declarations
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)

cascade_src = 'cars.xml'#assigns vehicle dataset to cars.xml
#video_src = VideoStream(0).start()#assigns input to video or live webcam stream
video_src = 'dataset/video2.avi'

cap = cv2.VideoCapture(video_src)#places video into openCV instance
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cap.read()#capture image at this point in time from openCV
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:#if a vehicle is detected
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        if chan.value > 3000:#when the sensor reading is above 300
            print("Polluter found")
            cv2.imwrite("frame%d.jpg" % time.time(), img)#store the video frame at this time and assign the current time to the name of the file
            #myDeviceShadow.shadowUpdate('{"state":{"reported":{"Polluter":"Detected"}}}', myShadowUpdateCallback, 5)#send data to AWS IoT that a polluting vehicle was detected
    
    cv2.imshow('video', img) #shows input image on desktop, disabled for monitorless operation
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
