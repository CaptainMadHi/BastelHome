import picamera
import time
import io
import socketserver
from threading import Condition
from http import server

#----Cam Stuff from https://randomnerdtutorials.com/video-streaming-with-raspberry-pi-camera/----#
class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()
        
    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)
    
camera = picamera.PiCamera()
camera.resolution = (1920,1080)
camera.framerate = 30
camera.exposure_mode = 'night'
camera.rotation = 180
output = StreamingOutput()
camera.start_recording(output, format='mjpeg')

t = time.strftime("%d.%m.%Y-%H%M%S")
#----Functions----#
def get():
    global output
    frame = output.frame
    return frame

def capturePhoto(): #Take a snapshot and save it with timestamp
        t = time.strftime("%d.%m.%Y-%H%M%S")
        camera.capture(t + '.jpg')
        return "saved image"
