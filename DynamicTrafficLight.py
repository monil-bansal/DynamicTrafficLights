import time

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


def ForStart(carsNorth , carsWest):
    if(carsNorth > carsWest):
        poleNorth.g = 1
        poleNorth.time.setZero()
        return [1,0,0,1]

    poleWest.g = 1
    poleWest.time.setZero()
    return [0,1,1,0]


def lights(north , west):

    if north[0].g == 0:
        toWork = west
        noWork = north
    else :
        toWork = north
        noWork = west

    if (toWork[0].time.elapsedTime() <= 10):
        return None

    elif (toWork[0].time.elapsedTime() >=60 ):
        ##change Light
        toWork[0].g = 0
        noWork[0].g = 1
        noWork[0].time.setZero()



    else :
        loadFactor = toWork[1] / (toWork[1] + noWork[1])
        if(loadFactor < threshHold):
            ##change Light
            toWork[0].g = 0
            noWork[0].g = 1
            noWork[0].time.setZero()

    return [(north[0].g,(north[0].g + 1)%2),(west[0].g,(west[0].g + 1)%2)]


min = 10  # sec
max = 60  # sec

threshHold = 5/12

carsNorth = int(input())
carsWest = int(input())

poleNorth = Pole()
poleWest = Pole()

lightStatus = ForStart(carsNorth, carsWest)
print(lightStatus)

while(1):
    lightStatus =  lights((poleNorth, carsNorth),(poleWest,carsWest))
    print(lightStatus)
    time.sleep(5)
    carsNorth = int(input())
    carsWest = int(input())








