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
    
#class StreamingHandler(server.BaseHTTPRequestHandler):
   # def do_GET(self):
print("üsch setze die cam auf picam")
camera = picamera.PiCamera()
camera.resolution = (1920,1080)
camera.framerate = 30
camera.exposure_mode = 'night'
t = time.strftime("%d.%m.%Y-%H%M%S")
output = StreamingOutput()
#Uncomment the next line to change your Pi's Camera rotation (in degrees)
camera.rotation = 180
camera.start_recording(output, format='mjpeg')
#   finally:
#       camera.stop_recording()

#----Functions----#
def get():
    global output
    #output.condition.wait()
    frame = output.frame
    return frame

def capturePhoto(): #Take a snapshot and save it with timestamp
        t = time.strftime("%d.%m.%Y-%H%M%S")
        camera.capture(t + '.jpg')
        return "saved image as", t , ".jpg"
