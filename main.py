
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
def main():
    commands.getoutput("fswebcam sample.jpg")
    cognition.cognition("sample.jpg")
    commands.getoutput("rm sample.jpg")


main()
