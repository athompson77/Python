#Alex Thompson, Kayla Kelly, and Aldrick Palad
#athompson77@gatech.edu, kkelly65@gatech.edu, and apalad3@gatech.edu
#We worked on this assignment alone, using only this semester's course materials.

from Myro import *

def seeingRed(filename):
    p = makePicture(filename)
    for pixel in getPixels(p):
        setRed(pixel, 255)
    show(p)
    savePicture(p,"seeingRed.jpg")

def fade(picList): #supply a premade list of pictures
    final = []
    dark = 1
    for frame in picList:
        for pixel in getPixels(frame):
            r,g,b=getRGB(pixel)
            setRed(pixel,r*dark)
            setBlue(pixel,b*dark)
            setGreen(pixel,g*dark)
        final = final+[frame]
        dark = dark-.12
    savePicture(final,"fade.gif")   #have to open gif in web browser to see

def overlay(filename):
    p = makePicture(filename)
    pHeight=getHeight(p)
    for y in range(pHeight):
        pix=getPixel(p,50,y)
        setRed(pix,0)
        setGreen(pix,0)
        setBlue(pix,255)
    pWidth=getWidth(p)
    for x in range(pWidth):
        pix=getPixel(p,x,50)
        setRed(pix,0)
        setGreen(pix,0)
        setBlue(pix,255)
    pHeight=getHeight(p)
    for y in range(pHeight):
        pix=getPixel(p,-50,y)
        setRed(pix,0)
        setGreen(pix,0)
        setBlue(pix,255)
    pWidth=getWidth(p)
    for x in range(pWidth):
        pix=getPixel(p,x,-50)
        setRed(pix,0)
        setGreen(pix,0)
        setBlue(pix,255)
    show(p)
    savePicture(p,"overlay.jpg")

def greenScreen(filename): #supply image in front of greenscreen
    s = makePicture("background.jpg")     #background is preloaded
    p = makePicture(filename)
    for pixel in getPixels(p):
        r,g,b = getRGB(pixel)
        if g>b and g>r and r<b+10:
            x = getX(pixel)
            y = getY(pixel)
            newPix = getPixel(s,x,y)
            newr,newg,newb = getRGB(newPix)
            setRed(pixel, newr)
            setGreen(pixel, newg)
            setBlue(pixel, newb)
    show(p)
    savePicture(p,"greenScreen.jpg")


def shake(pic):
    p2 = makePicture(pic)
    p = copyPicture(p2)
    for pixel in getPixels(p):
        setRed(pixel, 0)
        setGreen(pixel, 0)
        setBlue(pixel, 0)

    w = getWidth(p)
    h = getHeight(p)

    shiftList = [0, 30, 0, -30, 0, 60, 0, -60, 0]

    gif = []

    for i in range(len(shiftList)):
        shift = shiftList[i]

        for x in range(w):
            for y in range(h):
                xShift = x+shift
                pix = getPixel(p, xShift, y)
                pix2 = getPixel(p2, x, y)
                if shift > 0:
                    if xShift <= w:
                        setRed(pix, getRed(pix2))
                        setGreen(pix,getGreen(pix2))
                        setBlue(pix,getBlue(pix2))
                    else:
                        setRGB(pix, 0, 0, 0)

                elif shift < 0:
                    if xShift >= 0:
                        setRed(pix, getRed(pix2))
                        setGreen(pix,getGreen(pix2))
                        setBlue(pix,getBlue(pix2))
                    else:
                        setRGB(pix, 0, 0, 0)
                else:
                    setRed(pix, getRed(pix2))
                    setGreen(pix,getGreen(pix2))
                    setBlue(pix,getBlue(pix2))

        show(p)

        frame = copyPicture(p)

        gif = gif + [frame]

    savePicture(gif, 'shake.gif')