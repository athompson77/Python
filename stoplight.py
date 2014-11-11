#Alex Thompson, Kayla Kelly, and Aldrick Palad
#athompson77@gatech.edu, kkelly65@gatech.edu, and apalad3@gatech.edu
#We worked on this assignment alone, using only this semester's course materials.

from Myro import *
#init()
setPicSize("small")

def findColor(aPic):
    r,g,b = 0,0,0
    for x in range (100,200):
        for y in range (90,110):
            pix = getPixel(aPic,x,y)
            red,green,blue = getRGB(pix)
            r+=red
            g+=green
            b+=blue
    if r-b>20000 and g-b>20000:
        picColor = "yellow"
    elif g>b and g>r and r<b+40000:
        picColor = "green"
    elif r-g<10000 and b-g<10000 and g-r<10000:
        picColor="white"
    elif r-b>20000 and r-g>20000:
        picColor = "red"
    else:
        picColor="white"
    return picColor

def turn():
    result = heads()
    if result == True:
        setLED("right",1)
        turnBy(90, "deg")
        setLED("right",0)
    else:
        setLED("left",1)
        turnBy(-90, "deg")
        setLED("left",0)

def stopLight():
    a = True
    while a==True:
        p = takePicture()
        show(p)
        c = findColor(p)
        if c == "green":
            forward(1,2)
        elif c == "yellow":
            forward(.5,2)
        elif c == "white":
            turn()
        else:
            beep(1,800)
            return None
stopLight()