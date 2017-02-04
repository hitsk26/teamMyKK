print "Entery while roop"
while true:
	# おいしくなあれの発音の確認				
	if isNotCaputuredOishikunare():
		continue
	# 画像撮影
	path = captureImage()
	#　料理の認識
	outputFlavor = congnition(path)
	# モータ制御 調味料を出す
	motorControl(outputFlavor)

print "End"

