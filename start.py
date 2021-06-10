import threading
import os

def print_cube(num):
	os.system("cd yolov4-deepsort && python object_tracker.py --weights ./checkpoints/yolov4-tiny-416 --model yolov4 --video ./data/video/test.mp4 --output ./outputs/tiny.avi --tiny" )
	print("Cube: {}".format(num * num * num))

def print_square(num):
	os.system("cd Face-Track-Detect-Extract && python start.py")
	print("Square: {}".format(num * num))

if __name__ == "__main__":
	t1 = threading.Thread(target=print_square, args=(10,))
	t2 = threading.Thread(target=print_cube, args=(10,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print("Done!")
