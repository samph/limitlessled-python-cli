import sys, getopt, ledcontroller

def main(argv):
	CONTROLLER_ADDRESS="192.168.1.119"
	led = ledcontroller.LedController("192.168.1.119")
	color = 'white'
	group=0
	try:
		opts, args = getopt.getopt(argv,"hc:t:",["colour", "target"])
	except getopt.GetoptError:
		print 'limitless.py -c <color> -t <targetbulb> -m <mode>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'limitless.py -c <color> -t <targetbulb> -m <mode>'
			sys.exit()
		elif opt in ("-c", "--color"):
			color = arg
			#print(color + " is ")
		elif opt in ("-t", "--target"):
			if arg== '1':
				group=1
			elif arg == '2':
				group=2
			elif arg == '3':
				group=3


	if color == 'disco':
		print('disco')
		led.disco(group)
	elif color != 'off':
		led.set_color(color, group)
	else:
		led.off(group)


if __name__ == "__main__":
	main(sys.argv[1:])
