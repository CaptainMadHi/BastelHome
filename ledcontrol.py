import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 8      # Number of LED pixels in use. Change as Necessary.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

####Colors for simple swapping and usage. Add colors with codes as necessary#### 
green   = (0,255,0)
red = (255,0,0)
blue  = (0,0,255)

yellow = (255,150,0)
purple = (255,0,255)
cyan = (0,255,255)
orange = (255,45,0)

warm = (255, 95, 20) # Natural light
white = (255,255,255) 
off = (0,0,0)
#--Global Attributes--#
currentBrightness = 255 # Default Brightness at Start
isGRB = True
rgb = off
currentColor = rgb

status = "off" #used for requests
prevStatus = status
#                   Status Codes                        #
#'off'       0-> use when light is turned off| Default  #
#'on'        1-> use when light is turned on            #
#'animation' 2-> use when animation is running          #

####Functions####
def increaseBrightness(stip, amount=1):
    global currentBrightness
    
    if currentBrightness < 255:
        currentBrightness = currentBrightness+amount
        strip.setBrightness(currentBrightness)
    else:
        print ('Max brightness reached')
    strip.show()
    time.sleep(0.005)

def decreaseBrightness(stip, amount=1):
    global currentBrightness
    
    if currentBrightness > 10:
        currentBrightness = currentBrightness-amount
        strip.setBrightness(currentBrightness)
    else:
        print ('Min brightness reached')
    strip.show()
    time.sleep(0.005)

def setBrightness(strip, brightness):           #Überladen, fades into wanted brightness over short period. 
    global currentBrightness
    
    if currentBrightness < brightness:
        for i in range(currentBrightness,brightness):
            increaseBrightness(strip)
    
    if currentBrightness > brightness:
        for i in range(currentBrightness,brightness,-1):
            decreaseBrightness(strip)
    print('Setting Brightness to ', brightness)
    strip.show()
    currentBrightness=brightness

def setColor(strip, rgb):                             #sets LED-Strip color to input color code
    global currentBrightness, currentColor, isGRB
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    
    if isGRB:
        color = Color(g,r,b)
    else:
        color = Color(r,g,b)
    
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    #setBrightness(strip, currentBrightness)
    currentColor=rgb
    #print('Changing color')
    
def getColor():
    global currentColor
    r = currentColor[0]
    g = currentColor[1]
    b = currentColor[2]
    
    if isGRB:
     print ('Current color is GRB(',g,',', r,',', b, ')')
    else:
     print ('Current color is RGB(',r,',', g,',', b, ')')  
    return currentColor
    
####LED Animation Functions####
#Selfmade#
def test1(strip, color, wait_ms=50):
    """Flash all LEDs at ONCE"""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(0.5)

def cyrcle(strip, color):
    
    r = color[0]
    g = color[1]
    b = color[2]
    color = Color(g,r,b)
   
    pixels = strip.numPixels()
   
    for i in range(0, pixels):
        strip.setPixelColor(i,color)
        strip.setPixelColor((i + (pixels/2)),color)
        
        strip.setPixelColor(i-1, 0)
        strip.setPixelColor(i + pixels/2-1,0)
        strip.show()

#Not own made Methods#   
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/100.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

####Demo Functions to test Functions####
def brightnessDemo(strip):
            global green, red, blue, yellow, orange, purple, cyan, warm, weiß
            spectrum = [green, red, blue, yellow, orange, purple, cyan, warm, weiß]
            
            for i in spectrum:
                pure(strip, i)
                time.sleep(1)
                setBrightness(strip,50)
                time.sleep(1)
                setBrightness(strip, 255)
                time.sleep(1)
                setBrightness(strip,1)
            
    
#--Request Handling--#
status = False

def changeStatus(s):
    global status
    if s = 0:
        status = "off"
    if s = 1:
        status = "on"
    if s = 2:
        status = "animation"
        
def get_status():
  return {"status": status}

def change_status(new_status):
  global status
  status = new_status
  handleRequest(status)
  return {"status": status}

def invert_status():
  global status
  status = not status
  return {"status": status}

#Request Handler#
def handleRequest(s):
    global status, prevStatus
    
    #color request !Has to be changed! Cant address variables from string in that way!
    #if s = "white" or s = "warm" or s = "blue" or s = "purple" or s = "cyan" or s = "yellow" or s = "green" or s = "red"  or s = "orange" :
    #    color = s 
    #    setColor(s)
    #    prevStatus = status
    
    #rgb request
    if len(s) = 11:
        r = int(s[0:3])
        g = int(s[4:7])
        b = int(s[8:11])
        rgb=(r,g,b)
        setColor(rgb)
        prevStatus = status
    
    #brightness request
    if int(s) > 0 and int(s) <= 255:
        setBightness(s)
        prevStatus = status
    
    #Turn off
    if int(s) = 0 or s = "off" :
        setColor(off)
        #stopanimation()
        prevStatus = status
    else:
        status = prevStatus
        
    #animation request

def start_animation(anim):
    #open thread
    #execute animation in thread

def stop_animation():
    #close thread
    #use last color
# Main program #
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        t = 0.5
        while True:
            setBrightness(strip, 255)
            setColor(strip, blue)

    
    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)




