#!/usr/bin/env python
"""
Author: Carl-Be
Created: 8/13/2020
Updated: 8/15/2020
Version: 1

Run: ./pomtimer.py 

Description: This is a cli Linux pomodoro technique timer
"""
from time import sleep 
import subprocess as sp
from pydub import AudioSegment
from pydub.playback import play 
from asciiArt import asciiArt

# gets the time input from the user  
def askForInput(logicalMode, breakType):
    
    if logicalMode == 1:

        time = input('\nFocus Mode: Type 1-60 or 0 to exit\nHow many minutes: ')
        return time

    elif logicalMode == 0:

        if breakType == 0: # long break
            time = input('\nDefuse Mode Long Break: Type 1-60 or 0 to exit\nHow many minutes: ')
        elif breakType != 0: # short break 
            time = input('\nDefuse Mode Short Break: Type 1-60 or 0 to exit\nHow many minutes: ')
            
        return time

# resets the timer after goal time is meet
def resetTimer(timeModeList):
    
    print(asciiArt(63) + asciiArt(timeModeList[1]))
    playAudio()
    timeModeList[1] = getMoreTime(timeModeList[0]) 
    clearScreen()
    
    return 

def printFoucus(timeModeList, time):

    print(asciiArt(61) + asciiArt(timeModeList[1]))
    sleep(time) # sleep program for 5 seconds  

    return

def printDefuse(timeModeList, time): 
   
    print(asciiArt(62) + asciiArt(timeModeList[1]))
    sleep(time) # sleep program for 5 seconds  

    return
    
# display the timer 
def displayController(timeModeList):
    
    time = 60 # seconds to pause screen  

    # finish message display 
    if timeModeList[1] == 0: # print the finish message  
        resetTimer(timeModeList)

    # focus mode discplay 
    if timeModeList[1] > 0 and timeModeList[0] % 2 == 1: 
        printFoucus(timeModeList, time)
        return

    # defuse mode display 
    elif timeModeList[1] > 0 and timeModeList[0] % 2 == 0:
        printDefuse(timeModeList, time)
        return

# Function clears the screen before the next display
def clearScreen():
    
    command = "clear"
    sp.call(command, shell=True)

    return

#gets more time from user 
def getMoreTime(modeCount):

    logicalMode = modeCount % 2 # if mode is odd its focus mode if mode count if even its defuse mode
    breakType = modeCount % 8 # If Remainder is 0 long break. Long break every 4th break.
    time = askForInput(logicalMode, breakType) 
    
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

        displayController(timeModeList) # get the display 
        timeModeList[1] -= 1 # subtract one from time
        clearScreen() # clear the screen from the previous time 
        checkModeChange(timeModeList) # check to see if time is up or not

#plays aduio sound 
def playAudio():
    mp3File = "./alarmsound.mp3"
    alarmsound = AudioSegment.from_mp3(mp3File)
    lastTenSeconds = alarmsound[:10000]
    play(lastTenSeconds)
    
    
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
    time = askForInput(modeCount, None) # get intial time 
    checkIntialTime(modeCount, time)

if __name__ == '__main__':
    main()




