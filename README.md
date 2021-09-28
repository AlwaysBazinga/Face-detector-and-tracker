# Face-detector-and-tracker
The repository consists of a python code used to detect a face and align the it in the center of its frame using two steppper motor to control its movement by providoing pwm using Jetson nano
## Face detection
For face detection we use the python library mtcnn to use Multi-cascaded convolutional neural networks whichreturns coordinates, or the pixel values of a rectangle where the MTCNN algorithm detected faces. The “box” value above returns the location of the whole face, followed by a “confidence” level.

For more specific information we can also extarct certain features such as eyes , nose , right and left ends of the mouth.

## Face tracking 
In order to ensure the object is not lost if the detector fails due to occlusion we employ CSRT tracker.

## Controlling stepper motor 
We use the GPIO on Jetson Nano to give pwm to the stepper using L298n motor driver and a 12v power supply ,the code provides angular control over motor.
