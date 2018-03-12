# -*- coding: utf-8 -*-
#/usr/bin/python2.7
from datetime import datetime
#from neopixel import *
import ConfigParser
import time
import os.path



# LED strip configuration:
#LED_COUNT      = 114            # Number of LED pixels.
#LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
#LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
#LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
#LED_BRIGHTNESS = 20     # Set to 0 for darkest and 255 for brightest
#LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)



#def clock(color, wait_ms=5000):
def clock(wait_ms=5000):

    try:
        color4 = 0
        colorFile = ConfigParser.ConfigParser()
        colorFile.read('color.ini')
        DEFAULT = colorFile.get('COLOR', 'ccolor')
        print (DEFAULT)
    except:
        print ("color.ini not found")
        DEFAULT = '255, 0, 0'
        print (DEFAULT)


    colorFile = DEFAULT.split(",")
    color0 = colorFile[0]
    color1 = colorFile[1]
    color2 = colorFile[2]
    color0 = int(color0)
    color1 = int(color1)
    color2 = int(color2)
    
    
    
    
    #color = (int(color0), int(color1), int(color2))
    #print ("color = " + str(color))
    #print ("color0 = " +color0)
    #print ("color1 = " +color1)
    #print ("color2 = " +color2)    

    # get time from system
    minute = datetime.now().strftime('%M')
    hour = datetime.now().strftime('%I')
    hour24 = datetime.now().strftime('%H')
    hourint = int(hour)


    # umschalten der Modis
    modi = 2
    if modi == 1:
        config = ConfigParser.RawConfigParser()
        config.read('deutsch_hour.ini')
        hourplus = hour
    if modi == 2:
        config = ConfigParser.RawConfigParser()
        config.read('deutsch_viertel.ini')
        if minute >= 21:
            hourplus = int(hour) + 1
            hourplus = str(hourplus)
            print ("stunde plus eins " + hourplus)
    if modi == 3:
        config = ConfigParser.RawConfigParser()
        config.read('deutsch_hour.ini')



    hour = config.get('HOUR', hourplus)
    h = hour.split(",")

    # get value from ini file

    print ("############### START ################")
    es = config.get('HOUR', 'es')
    e = es.split(",")
    print ("pixel Aufruf")
    print ("es: ")
    for e in e:
        print (e)
    print ("##########################################")
    ist = config.get('HOUR', 'ist')
    ist = ist.split(",")
    print ("pixel Aufruf")
    print ("ist: ")
    for ist in ist:
        print (ist)
    print ("##########################################")
    uhr = config.get('HOUR', 'uhr')
    uhr = uhr.split(",")
    print ("pixel Aufruf")
    print ("uhr: ")
    for uhr in uhr:
        print (uhr)



    print ("Ansteuerung der Stunden")
    print ("Stunde " + str(hourint))
    print ("Stunde 24 " + str(hour24))
    for h in h:
        try:
            print (h)
        except:
            print ("Fehler")
    print ("############")


    mi = config.get('MIN', minute)
    min = mi.split(",")
    print ("Minute " + minute)
    #print (min)

    print ("pixel Aufruf Minute")
    for min in min:
        try:
            print (min)
        except:
            print ("Fehler")


    if mi >= 1:
        print ("Display Minute als Wort")
        minute = config.get('MIN', 'minuten')
        dis_minute = minute.split(",")
        print ("pixel Aufruf")
        for dis_minute in dis_minute:
            print (dis_minute)


    time.sleep(wait_ms/1000.0)

# Main program:
if __name__ == '__main__':
	
    #strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    #strip.begin()

    print ('Press Ctrl-C to quit.')
    while True:
        #clock(strip, Color(255, 255, 0))  # rot wipe
        clock ()
