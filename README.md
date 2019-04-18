# EE186Project

The project will require two different sensors at the chosen location, with the first being the camera used for object detection, and the second being the pollution sensor.

The Raspberry pi will run an OpenCV script that will detect and count each vehicle object in the frame at each point. This data about vehicle counts will then be compared to the incoming pollution data, and if the pollution data is above the expected range for the car count at a particular time, the Raspberry pi will then save the next frame of video.


The general pollution data, data about moments of high pollution, and vehicle count data will then be sent by internet to an AWS IOT account connected to a site, which will publish the gathered data. 

An extension of this project would involve integrating a machine learning framework to get a more precise correlation between the amount of pollution generated locally and the types and counts of vehicles passing at a certain point in time. This would be done with further processing on a remote server using HOG (Histogram of gradient) feature extraction and a support vector machine classifier to classify vehicles in a video stream. 
