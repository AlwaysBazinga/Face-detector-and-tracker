# Face-detector-and-tracker
The repository consists of a python code used to detect a face and align the it in the center of its frame using two steppper motor to control its movement by providoing pwm using Jetson nano
## Face detection
For face detection we use the python library mtcnn to use Multi-cascaded convolutional neural networks whichreturns coordinates, or the pixel values of a rectangle where the MTCNN algorithm detected faces. The “box” value above returns the location of the whole face, followed by a “confidence” level.MTCNN is a python (pip) library written by Github user ipacz, which implements the paper Zhang, Kaipeng et al. “Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks.” IEEE Signal Processing Letters 23.10 (2016): 1499–1503. Crossref. Web.

![Face detection using mtcnn](https://miro.medium.com/max/221/0*eELmT5qRW4LlfyoE.png)

For more specific information we can also extarct certain features such as eyes , nose , right and left ends of the mouth.

## Face tracking 
In order to ensure the object is not lost if the detector fails due to occlusion we employ CSRT tracker.In the Discriminative Correlation Filter with Channel and Spatial Reliability (DCF-CSR), we use the spatial reliability map for adjusting the filter support to the part of the selected region from the frame for tracking. This ensures enlarging and localization of the selected region and improved tracking of the non-rectangular regions or objects. It uses only 2 standard features (HoGs and Colornames). It also operates at a comparatively lower fps (25 fps) but gives higher accuracy for object tracking.

![Face tracking using CSRT](https://929687.smushcdn.com/2407837/wp-content/uploads/2018/10/object_tracking_dlib_featured-300x168.jpg?lossy=1&strip=1&webp=0)

## Controlling stepper motor 
We use the GPIO on Jetson Nano to give pwm to the stepper using L298n motor driver and a 12v power supply ,the code provides angular control over motor.
