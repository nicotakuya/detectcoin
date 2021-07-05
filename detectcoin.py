import jetson.inference
import jetson.utils
import argparse
import sys

sys.argv.append("--model=models/coin/ssd-mobilenet.onnx")
sys.argv.append("--labels=models/coin/labels.txt")
sys.argv.append("--input_blob=input_0")
sys.argv.append("--output-cvg=scores")
sys.argv.append("--output-bbox=boxes")
sys.argv.append("/dev/video0")		# web camera(logicool C270)

parser = argparse.ArgumentParser()
parser.add_argument("input_URI", type=str, default="", nargs='?')
parser.add_argument("output_URI", type=str, default="", nargs='?')
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2")
parser.add_argument("--overlay", type=str, default="box,labels,conf")
parser.add_argument("--threshold", type=float, default=0.5)

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv)

while True:
	img = input.Capture()
	detections = net.Detect(img, overlay=opt.overlay)
	yen = 0
	for detection in detections:
		if net.GetClassDesc(detection.ClassID)=="coin100yen":
			yen += 100

	output.Render(img)
	output.SetStatus("TOTAL:"+str(yen)+" yen!")
	if not input.IsStreaming() or not output.IsStreaming():
		break

