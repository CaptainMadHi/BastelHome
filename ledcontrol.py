import time
from rpi_ws281x import *
import argparse
import threading

# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels in use. Change as Necessary.
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
current_brightness = 255 # Default Brightness at Start
isGRB             = False
current_color      = off # Tuple format for RGB values, e.g.: (255,255,255)
current_animation  = "static"
animation_thread  = None

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

status = "off" #used for requests
prevStatus = status
#                   Status Codes                        #
#'off'       0-> use when light is turned off| Default  #
#'on'        1-> use when light is turned on            #
#'animation' 2-> use when animation is running          #

####Functions####
def increaseBrightness(stip, amount=1):
    global current_brightness
    
    if current_brightness < 255:
        current_brightness = current_brightness+amount
        strip.setBrightness(current_brightness)
    else:
        print ('Max brightness reached')
    strip.show()
    time.sleep(0.005)

def decreaseBrightness(stip, amount=1):
    global current_brightness
    
    if current_brightness > 10:
        current_brightness = current_brightness-amount
        strip.setBrightness(current_brightness)
    else:
        print ('Min brightness reached')
    strip.show()
    time.sleep(0.005)

def setBrightness(strip, brightness):           #Überladen, fades into wanted brightness over short period. 
    global current_brightness
    
    if current_brightness < brightness:
        for i in range(current_brightness,brightness):
            increaseBrightness(strip)
    
    if current_brightness > brightness:
        for i in range(current_brightness,brightness,-1):
            decreaseBrightness(strip)
    print('Setting Brightness to ', brightness)
    strip.show()
    current_brightness=brightness

def setColor(strip, rgb):
    global current_brightness, current_color, isGRB
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
    current_color=rgb
    
def getColor():
    global current_color
    r = current_color[0]
    g = current_color[1]
    b = current_color[2]
    
    if isGRB:
        print ('Current color is GRB(',g,',', r,',', b, ')')
    else:
        print ('Current color is RGB(',r,',', g,',', b, ')')  
    return current_color
    
####LED Animation Functions####
#Selfmade#
def test1(strip, color, wait_ms=50):
    """Flash all LEDs at ONCE"""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(0.5)

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
        if not getattr(animation_thread, "do_run", True): return
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        if not getattr(animation_thread, "do_run", True): return
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            if not getattr(animation_thread, "do_run", True): return
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
def get():
    global current_color, current_brightness, current_animation 
    return {"red": current_color[0], "green": current_color[1], "blue": current_color[2], "brightness": current_brightness, "animation": current_animation} 

def change_rgb(color):
    global current_color, current_animation, strip
    stop_animation()
        
    r = (color & 0xff0000) >> 16
    print(r)
    g = (color & 0x00ff00) >> 8
    print(g)
    b =  color & 0x0000ff
    print(b)
    setColor(strip, (r,g,b))
    return{"RGB": (r,g,b)}

def change_brightness(brightness):
    global stop
    if(brightness >= 0 and brightness <= 255):
        setBrightness(strip, brightness)
        return{"Brightness" : brightness}
    else:
        return{"Wrong Input" : "Brightnesslevel must be between 0-255" }

def change_toWarm():
    global current_animation, warm, strip
    stop_animation()
    setColor(strip, warm)
    return{"Preset Color": warm }

def change_toWhite():
    global current_animation, white, strip
    stop_animation()
    setColor(strip, white)
    return{"Preset Color": white }

def change_turnOff():
    global current_animation, off, strip
    stop_animation()
    setColor(strip, off)
    return{"Turned off: " : "true"}

def start_animation_theaterChaseRainbow():
    global current_animation, animation_thread
    stop_animation()
    animation_thread = threading.Thread(target=theaterChaseRainbow, args=(strip,))
    current_animation = "theaterChaseRainbow"
    animation_thread.start()
    return{"Animation: " : current_animation}

def start_animation_rainbowCycle():
    global current_animation, animation_thread
    stop_animation()
    animation_thread = threading.Thread(target=rainbowCycle, args=(strip,))
    current_animation = "rainbowCycle"
    animation_thread.start()
    return{"Animation: " : current_animation}

def start_animation_theaterChase():
    global current_animation, animation_thread, current_color
    stop_animation()
    animation_thread = threading.Thread(target=theaterChase, args=(strip, current_color))
    current_animation = "theaterChase"
    animation_thread.start()
    return{"Animation: " : current_animation}
    
def stop_animation():
    global current_animation, animation_thread, current_color
    if animation_thread is not None:
        animation_thread.do_run = False
        animation_thread.join()     
    animation_thread = None
    setColor(strip, current_color)
    current_animation = "static"
    return{"Animation: " : "stopped"}

# Main program #
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    change_brightness(90)

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        t = 0.5
        while True:
            print("Testing change_RGB")
            change_rgb(0xff0000)
            time.sleep(2)
            
            print("Testing change_turnOff()")
            change_turnOff()
            time.sleep(2)
            
            print("Testing change_toWarm()")
            change_toWarm()
            time.sleep(2)
            
            print("Testing start_animation_theaterChaseRainbow()")
            start_animation_theaterChaseRainbow()
            time.sleep(5)
            stop_animation()
            time.sleep(2)

           # print("Testing start_animation_theaterChase()")
           # start_animation_theaterChase()
           # time.sleep(5)
           # stop_animation()
           # time.sleep(2)

            print("Testing start_animation_rainbowCycle()")
            start_animation_rainbowCycle()
            time.sleep(5)
            stop_animation()
            time.sleep(20)
    
    except KeyboardInterrupt:
            stop_animation()
            colorWipe(strip, Color(0,0,0), 10)
            