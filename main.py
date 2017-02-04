
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

import commands
import cognition as cognition
import moter as moter
#switch=false
def main():
    #while true:
      #if switch
        commands.getoutput("fswebcam sample.jpg")
        #1 salada 2 potato
        moter.rotate(cognition.cognition("sample.jpg"))
        commands.getoutput("rm sample.jpg")

main()
