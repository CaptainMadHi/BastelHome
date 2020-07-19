import cv2
import time
from threading import Thread
#import atexit
import sys
from flask import render_template, Response

t = time.strftime("%d.%m.%Y-%H%M%S")

class WebcamVideoStream:
    def __init__(self, src = 0):
        print("init")
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        time.sleep(2.0)
    
    def start(self):
        print("start thread")
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self
    
    def update(self):
        print("read")
        while True:
            if self.stopped:
                return
            
            (self.grabbed, self.frame) = self.stream.read()
    
    def read(self):
        return self.frame
    
    def stop(self):
        self.stopped = True


def gen(camera):
    while True:
        if camera.stopped:
            break
        frame = camera.read()
        ret, jpeg = cv2.imencode('.jpg',frame)
        if jpeg is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
        else:
            print("frame is none")

stream = WebcamVideoStream()

def get():
    return (gen(stream.start()), 'multipart/x-mixed-replace; boundary=frame')

