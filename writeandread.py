#Alex Thompson and Eleanor Eason
#athompson77@gatech.edu and e.eason@gatech.edu
#We worked on this assignment alone, using only this semester's course materials.

from Myro import *
init()

from Graphics import *
win = Window("box", 200, 200)           #open window
record = open("myMovements.txt","w")    #create and close file first
record.close()

def move(win, command):
    record = open("myMovements.txt", "a")   #append so it adds on each time
    sensorValue = (getLight("left")/(getLight("right") + getObstacle("right")))
    #assign movements to directions
    if command.key == "Up":
        forward(1,.1)
        record.write("forward\t.1\t{:.3f}\n".format(sensorValue))
    elif command.key == "Down":
        backward(1,.1)
        record.write("backward\t.1\t{:.3f}\n".format(sensorValue))
    elif command.key == "Left":
        turnLeft(1,.1)
        record.write("left\t.1\t{:.3f}\n".format(sensorValue))
    elif command.key == "Right":
        turnRight(1,.1)
        record.write("right\t.1\t{:.3f}\n".format(sensorValue))
    elif command.key == "b":
        beep(.1,800)
        record.write("beep\t.1\t \n")
    record.close()

#each keypress calls the function
onKeyPress(move)

def collectData(filename, direction):   #direction has to be a string
    temp = open(filename, "r")          #Ex: "forward", "backward"
    jaywalk = temp.readlines()          #otherwise it prints <built-in function>
    temp.close()
    seconds,totalmove,beeps = [0,0,0]   #initializes counter variables
    for line in jaywalk:                #reads file one line/movement at a time
        movements, s, v = line.split("\t")  #each element in line assigned to variable
        if movements != "beep":
            if movements == direction:
                totalmove += 1
            seconds += float(s)
        else:
            beeps += 1
    return ("The robot traveled for {0} seconds total, beeping {1} times. This robot moved {2} a total of {3} times.".format(seconds,beeps,direction,totalmove))

#collectData("myMovements.txt", "forward")
#have to call function from shell after writing file/running hw
    #cannot call from hw as it reads file before movements are written

def replay(filename):
    temp = open(filename, "r")
    jaywalk = temp.readlines()
    temp.close()
    for line in jaywalk:
        movements, s, v = line.split("\t")  #same as collectData()
        if movements == "forward":
            forward(1, float(s))
        elif movements == "backward":
            backward (1, float(s))
        elif movements == "left":
            turnLeft(1, float(s))
        elif movements == "right":
            turnRight(1, float(s))
        else:
            beep (float(s), 800)

#replay("myMovements.txt")
    #have to call from shell after writing file