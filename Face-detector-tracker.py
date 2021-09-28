import mtcnn
import cv2
import math
import time
import Jetson.GPIO as GPIO
import tensorflow as tf
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        # Currently, memory growth needs to be the same across GPUs
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
    except RuntimeError as e:
        # Memory growth must be set before GPUs have been initialized
        print(e)

# N is the distance from the person
out1 = 29
out2 = 33
out3 = 31
out4 = 35


GPIO.setmode(GPIO.BOARD)
GPIO.setup(out1, GPIO.OUT)
GPIO.setup(out2, GPIO.OUT)
GPIO.setup(out3, GPIO.OUT)
GPIO.setup(out4, GPIO.OUT)

a0 = 0
time0 = time.time()


def shift(x1, x, f):
    global a0
    global time0
    if f != 0:
        real = 23 / f
        n = (258 / f) * 30
        if x - x1 > 0:
            angle = math.degrees(math.atan2(abs(x - x1) * real, n))
        else:
            angle = - math.degrees(math.atan2(abs(x - x1) * real, n))

        if time.time() > time0 + 1 and abs(angle)> 15:
            time0 = time.time()
            a0 = angle

            GPIO.output(out1, GPIO.LOW)
            GPIO.output(out2, GPIO.LOW)
            GPIO.output(out3, GPIO.LOW)
            GPIO.output(out4, GPIO.LOW)
            x = int(a0)
            i = 0
            positive = 0
            negative = 0
            y = 0
            if x > 0 and x <= 400:
                x += round(x / 9)
                for y in range(x, 0, -1):
                    if negative == 1:
                        if i == 7:
                            i = 0
                        else:
                            i = i + 1
                        y = y + 2
                        negative = 0
                    positive = 1
                    # print((x+1)-y)
                    if i == 0:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(0.01)
                        # time.sleep(1)
                    elif i == 1:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(0.01)
                        # time.sleep(1)
                    elif i == 2:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(0.01)
                        # time.sleep(1)
                    elif i == 3:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(0.01)
                        # time.sleep(1)
                    elif i == 4:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(0.01)
                        # time.sleep(1)
                    elif i == 5:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.HIGH)
                        time.sleep(0.01)
                        # time.sleep(1)
                    elif i == 6:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        time.sleep(0.01)
                        # time.sleep(1)
                    elif i == 7:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        time.sleep(0.01)
                        # time.sleep(1)
                    if i == 7:
                        i = 0
                        continue
                    i = i + 1


            elif x < 0 and x >= -400:
                x = x * -1
                x += round(9)
                for y in range(x, 0, -1):
                    if positive == 1:
                        if i == 0:
                            i = 7
                        else:
                            i = i - 1
                        y = y + 3
                        positive = 0
                    negative = 1
                    # print((x+1)-y)
                    if i == 0:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(0.01)
                        # time.sleep(1)
                    elif i == 1:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(0.01)
                        # time.sleep(1)
                    elif i == 2:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(0.01)
                        # time.sleep(1)
                    elif i == 3:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(0.01)
                        # time.sleep(1)
                    elif i == 4:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(0.01)
                        # time.sleep(1)
                    elif i == 5:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.HIGH)
                        time.sleep(0.01)
                        # time.sleep(1)
                    elif i == 6:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        time.sleep(0.01)
                        # time.sleep(1)
                    elif i == 7:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        time.sleep(0.01)
                        # time.sleep(1)
                    if i == 0:
                        i = 7
                        continue
                    i = i - 1


detector = mtcnn.MTCNN()
print(mtcnn.__version__)

k = 0
ok = None
m = 0
video_capture = cv2.VideoCapture(-1)
frame_width = int(video_capture.get(3))
frame_height = int(video_capture.get(4))

size = (frame_width, frame_height)
result = cv2.VideoWriter('face_mtcnn.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
tracker = cv2.TrackerCSRT_create()
while True:
    ret,frame = video_capture.read()
    faces = detector.detect_faces(frame)
    if faces:
        bbox = faces[0]['box']
        tracker = cv2.TrackerCSRT_create()
        ok = (tracker.init(frame, bbox))
        break

while True:
    ret, frame = video_capture.read()
    # Capture frame-by-frame
    timer = cv2.getTickCount()
    faces = detector.detect_faces(frame)
    # print("shit")
    if faces:
        print(faces[0]["box"])
        bbox = faces[0]['box']
        tracker = cv2.TrackerCSRT_create()
        ok = (tracker.init(frame, bbox))
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        shift(bbox[0] + bbox[2] / 2, frame_width / 2, bbox[2])
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
        # print(ok)
    # print("shit2")
    else:
        ok, bbox = tracker.update(frame)
        shift(bbox[0] + bbox[2] / 2, frame_width / 2, bbox[2])
        if ok:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
            k += 1
        else:
            pass
            # Tracking failure

    cv2.putText(frame, "CSRT" + " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
    m += 1
    # Display FPS on frame
    #cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);
    # Display result
    cv2.imshow("Tracking", frame)
    result.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
