import sys
import threading
sys.path.append('/home/pi/SpiderPi/')
from HiwonderSDK.Board import *
import HiwonderSDK.ActionGroupControl as AGC

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

def runActionGroup(num):
    threading.Thread(target=AGC.runAction, args=(num, )).start()    

def stopActionGroup():    
    AGC.stopAction()  
