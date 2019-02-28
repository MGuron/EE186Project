# EE186Project

The project will require two different sensors at the chosen location, with the first being the camera used for object detection, and the second being the pollution sensor. Depending on the exact pollution sensor used, the pollution sensor may need to be wired into an I2C clock stretching compatible microcontroller, which would necessitate a connection between the I2C clock stretching compatible microcontroller and the Raspberry PI that is running the full object detection script. This solution is due to the fact that OpenCV has to run in a computer with a full operating system, which a normal Arduino would not provide. This dual microcontroller strategy could be avoided if the I2C clock on the Raspberry pi was to be slowed, but research has shown that this approach may not work consistently.

The Raspberry pi will run an OpenCV script that will detect and count each vehicle object in the frame at each point. This data about vehicle counts will then be compared to the incoming pollution data, and if the pollution data is above the expected range for the car count at a particular time, the Raspberry pi will then save the next frame of video.


The general pollution data, data about moments of high pollution, and vehicle count data will then be sent by internet to an AWS IOT account connected to an AWS site, which will publish the gathered data. 

An extension of this project would involve integrating a machine learning framework to get a more precise correlation between the amount of pollution generated locally and the types and counts of vehicles passing at a certain point in time. This would be done with further processing on a remote server using HOG (Histogram of gradient) feature extraction and a support vector machine classifier to classify vehicles in a video stream. 

# March 7th – obtain all free parts from ETG, continued research on software and particulate sensor, begin software work

# March 14th – Obtain particulate sensor and misc parts, initial OpenCV and webcam integration

# March 28th – finish object detection script, connect and test all controllers and sensors

# April 4th – Troubleshoot data connections between sensors and microcontrollers, have full framework for all software

# April 21st – Finish outdoor installation and have all software in working condition

# April 28th – Continued outdoor and network testing program finished, Software fully functional, AWS site functional 
