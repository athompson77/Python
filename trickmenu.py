#Alexandra Thompson
#athompson77@gatech.edu
#CS 1301-Section B01
#I worked on the homework assignment alone using only this semester's course materials.

from Myro import*
init()

def shake(): #helper function
    for t in timer(5):
        turnBy(20,"deg")
        turnBy(-20, "deg")

def rollOver(): #helper function
    forward(1,2)#backward, spins, forward, spins
    turnLeft(1,3.2)
    backward(1,2)
    turnRight(1,3.2)

def chaseTail(): #helper function
    import random
    for t in timer(10): #spins randomly
        turnBy(random.randint(-350,350),"deg")
        motors(1,.2)
        wait(2)
        stop()

def star(): #helper function
    for t in timer(10): #makes a criss cross star
        forward(1,2)
        turnBy(45,"deg")
        backward(1,2)
        turnBy(45,"deg")

def tune(): #helper function
    turnLeft(1)
    beep(.2,1318.51)#plays first measure of fur elise
    beep(.2,1244.51)
    beep(.2,1318.51)
    beep(.2,1244.51)
    beep(.2,1318.51)
    beep(.2,987.77)
    beep(.2,1174.66)
    beep(.2,1046.50)
    beep(.5,880)
    stop()

def morningRoutine(tricks):
    if tricks <1:
        return None
    elif tricks == 1:
        shake()
    elif tricks == 2:
        shake()
        rollOver()
    elif tricks == 3:
        shake()
        rollOver()
        chaseTail()
    elif tricks == 4:
        shake()
        rollOver()
        chaseTail()
        star()
    else:
        shake()
        rollOver()
        chaseTail()
        star()
        tune()

def potato(): #helper function
    forward(.5,1)
    backward(.5,1)
    beep(.5,523.25) #cbA#a
    beep(.5,493.88)
    beep(.5,466.16)
    beep(1,440)

def fish(): #helper function
    shake()
    beep(.3, 587.33) #low-pitch yellow submarine
    beep(.3, 587.33)
    beep(.3, 587.33)
    beep(.2, 587.33)
    beep(.2, 659.25)
    beep(.2, 440)
    beep(.1, 440)
    beep(.2, 440)
    beep(.1, 440)
    beep(.4, 440)

def scooby(): #helper function
    chaseTail()
    beep(.2, 1318.51) #scooby doo theme
    beep(.25, 1318.51)
    beep(.2, 1174.66)
    beep(.25, 1174.66)
    beep(.6, 1046.50)
    wait(.2)
    beep(.2, 1174.66)
    beep(.5, 1396.91)
    beep(.5, 880)

def cat():  #helper function
    rollOver()
    beep(.4, 783.99) #the lion sleeps tonight
    beep(.2, 880)
    beep(.4, 987.77)
    beep(.3, 880)
    beep(.2, 987.77)
    beep(.4, 1046.50)
    beep(.2, 987.77)
    beep(.3, 880)
    beep(.4, 783.99)

def dragon(): #helper function
    star()
    beep(.4, 1046.50) #puff the magic dragon
    beep(.2, 1046.50)
    beep(.3, 1046.50)
    beep(.3, 1046.50)
    beep(.6, 987.77)
    beep(.5, 783.99)
    beep(.5, 880)
    beep(.2, 1046.50)
    beep(.2, 1046.50)
    beep(.5, 783.99)

def greetMenu():
    def menu():
        print ("1) Potato")
        print ("2) Fish Treats...")
        print ("3) Scooby Snacks?")
        print ("4) Cat Treats!")
        print ("5) Dragon Treats!!!")
        print ()
        print ("0) Exit")
    run = True
    while run == True:
        menu()
        choice = int(input("Give Trapper some treats"))
        if choice == 1:
            potato()
            print()
        elif choice == 2:
            fish()
            print()
        elif choice ==3:
            scooby()
            print()
        elif choice == 4:
            cat()
            print()
        elif choice == 5:
            dragon()
            print()
        elif choice ==0:
            print()
            print ("Bye! Thank you!")
            run = False
        else:
            askQuestion("Don't be mean. Please choose some treats.",["Sorry"])
            print()