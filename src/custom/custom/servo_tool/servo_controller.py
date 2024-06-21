from BusServoControl import *

def getServoPulse(id):
    return getBusServoPulse(id)

def getServoDeviation(id):
    return getBusServoDeviation(id)

def setServoPulse(id, pulse, use_time):
    setBusServoPulse(id, pulse, use_time)

def setServoDeviation(id ,dev):
    setBusServoDeviation(id, dev)
    
def saveServoDeviation(id):
    saveBusServoDeviation(id)

def unloadServo(id):
    unloadBusServo(id)
