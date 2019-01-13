import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2
import json
import time
import os


class Stopwatch:
    def __init__(self):
        self.creationTime = time.time()

    def elapsedTime(self):
        return time.time() - self.creationTime

    def setZero(self):
        self.creationTime = time.time()


class Pole:
    def __init__(self):
        self.g = 0
        self.time = Stopwatch()


def ForStart(carsNorth, carsWest):
    if (carsNorth > carsWest):
        poleNorth.g = 1
        poleNorth.time.setZero()
        return [(1, 0), (0, 1)]

    poleWest.g = 1
    poleWest.time.setZero()
    return [(0, 1), (1, 0)]


def lights(north, west):
    if north[0].g == 0:
        toWork = west
        noWork = north
    else:
        toWork = north
        noWork = west

    if (toWork[0].time.elapsedTime() <= 10):
        return None

    elif (toWork[0].time.elapsedTime() >= 60):
        ##change Light
        toWork[0].g = 0
        noWork[0].g = 1
        noWork[0].time.setZero()



    else:
        loadFactor = toWork[1] / (toWork[1] + noWork[1])
        if (loadFactor < threshHold):
            ##change Light
            toWork[0].g = 0
            noWork[0].g = 1
            noWork[0].time.setZero()

    return [(north[0].g, (north[0].g + 1) % 2), (west[0].g, (west[0].g + 1) % 2)]


# open webcam
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    # print("Could not open webcam")
    exit()

person = {}
person['people'] = []

# loop through frames
while webcam.isOpened():

    # read frame from webcam
    status, frame = webcam.read()

    if not status:
        # print("Could not read frame")
        exit()

    # apply object detection
    bbox, label, conf = cv.detect_common_objects(frame)
    person['people'].append(label)
    # print(bbox, label, conf)
    count = 0
    size = len(label)
    for i in range(0, size):
        if (label[i] == 'car'):
            count += 1
    # print (count)

    # draw bounding box over detected objects
    out = draw_bbox(frame, bbox, label, conf)

    # display output
    cv2.imshow("Real-time object detection", out)
    time.sleep(3)
    # press "Q" to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release resources
webcam.release()
cv2.destroyAllWindows()

min = 10  # sec
max = 60  # sec

threshHold = 5 / 12

carsNorth = count
carsWest = 5

poleNorth = Pole()
poleWest = Pole()

lightStatus = ForStart(carsNorth, carsWest)
print(lightStatus)

while (1):
    lightStatus = lights((poleNorth, carsNorth), (poleWest, carsWest))
    print(lightStatus)
    time.sleep(5)
    carsWest = 5