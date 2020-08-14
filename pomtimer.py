#!/usr/bin/env python
"""
Author: Carl-Be
Created: 8/13/2020
Updated: 8/13/2020
Version: 1

Run: ./pomtimer.py 

Description: This is a cli Linux pomodoro technique timer
"""
from time import sleep 
import subprocess as sp
from playsound import playsound as ps  
from asciiArt import asciiArt


# gets the time input from the user  
def askForInput(logicalMode):
    
    if logicalMode == 1:

        time = input('\nFocus Mode: Type 1-60 or 0 to exit\nHow many minutes: ')
        return time

    elif logicalMode == 0:
        
        time = input('\nDefuse Mode: Type 1-60 or 0 to exit\nHow many minutes: ')
        return time

# resets the timer after goal time is meet
def resetTimer(timeModeList):
    
    print(asciiArt(63) + asciiArt(timeModeList[1]))
    playAudio()
    timeModeList[1] = getMoreTime(timeModeList[0]) 
    clearScreen()
    
    return 

def printFoucus(timeModeList):

    print(asciiArt(61) + asciiArt(timeModeList[1]))
    sleep(1) # sleep program for 5 seconds  

    return

def printDefuse(timeModeList): 
   
    print(asciiArt(62) + asciiArt(timeModeList[1]))
    sleep(1) # sleep program for 5 seconds  

    return
    
# display the timer 
def displayController(timeModeList):

    # finish message display 
    if timeModeList[1] == 0: # print the finish message  
        resetTimer(timeModeList)

    # focus mode discplay 
    if timeModeList[1] > 0 and timeModeList[0] % 2 == 1: 
        printFoucus(timeModeList)
        return

    # defuse mode display 
    elif timeModeList[1] > 0 and timeModeList[0] % 2 == 0:
        printDefuse(timeModeList)
        return

# Function clears the screen before the next display
def clearScreen():
    
    command = "clear"
    sp.call(command, shell=True)

    return

#gets more time from user 
def getMoreTime(modeCount):

    logicalMode = modeCount % 2 # if mode is odd its focus mode if mode count if even its defuse mode
    time = askForInput(logicalMode)  
    return time 

# check to see if the time is 0 or not 
def checkModeChange(timeModeList):

# add one to the mode count 
    if timeModeList[1] == 0:
        timeModeList[0] += 1
    
        return 

    else:
        return

# controls the timer funcuntions 
def timer(modeCount, time):
    timeModeList = [modeCount, time]

    while timeModeList[1] >= 0: # while time is not less than zero. Zero minuets is the end goal   

        displayController(timeModeList) # get the is play 
        timeModeList[1] -= 1 # subtract one from time
        clearScreen() # clear the screen from the previous time 
        checkModeChange(timeModeList) # check to see if time is up or not

#plays aduio sound 
def playAudio():

    return 

def checkIntialTime(modeCount, time):
    # if zero do not start timer
    if time <= 0:
        return 

    # else start timer 
    else: 
        timer(modeCount, time) # start the timer 

def main():
    modeCount = 1 # starts out in focus mode 
    time = askForInput(modeCount) # get intial time 
    checkIntialTime(modeCount, time)

if __name__ == '__main__':
    main()



