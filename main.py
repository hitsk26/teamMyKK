
#print "Entery while roop"
#while true:
#	if isNotCaputuredOishikunare():
#		continue
#	path = captureImage()
#	outputFlavor = congnition(path)
#	motorControl(outputFlavor)

#print "End"

#!/usr/bin/python
from __future__ import print_function
import threading
import commands
from time import sleep
import RPi.GPIO as GPIO
import cognition as cognition
import moter as moter
import sound as sound
#switch=false
def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.IN)
    kirakiraSoundPath = '/home/tsuzuku/python_games/match1.wav' 
    soundThread = threading.Thread(target=sound.play,name="soundThread",args=(kirakiraSoundPath,))
    soundThread.setDaemon(False)

    while True:
      if GPIO.input(20) == GPIO.HIGH:
        soundThread.start()
        commands.getoutput("fswebcam sample.jpg")
        #1 salada 2 potato
        moter.rotate(cognition.cognition("sample.jpg"))
        commands.getoutput("rm sample.jpg")
        break
    
main()
