import pygame
import random
import time
from pathlib import Path


# Initialize pygame mixer once
pygame.mixer.init()

def countFiles():
    musicPath = Path('music')
    numberOfFiles = len(list(musicPath.glob("*")))
    return numberOfFiles

def randomNumb():
    return random.randint(1, countFiles())

# Function to play the audio
def play_audio(passedIn=None):
    if not passedIn:
        randomNumber = randomNumb()
    else:
        randomNumber=passedIn
    pygame.mixer.music.load(f"music/{randomNumber}.mp3")
    with open('currentPlaying.txt', 'r+') as currentTrack:
        currentTrack.seek(0)
        currentTrack.truncate()
        currentTrack.write(str(randomNumber))
    pygame.mixer.music.play()

# Function to pause the audio
def pause_audio():
    pygame.mixer.music.pause()

# Function to resume audio
def resume_audio():
    pygame.mixer.music.unpause()

# Function to restart audio
def restart_audio():
    pygame.mixer.music.stop()
    pygame.mixer.music.play()

# Check if audio is playing
def isPlaying():
    return pygame.mixer.music.get_busy()

def skipSong():
    with open('currentPlaying.txt', 'r+') as currentPlaying:
        currentIndex = currentPlaying.readline().strip()
        
        if currentIndex.isdigit():
            currentIndex = int(currentIndex)
        else:
            currentIndex = 0  # Default to 0 if file is empty/invalid

        newIndex = (currentIndex + 1) % countFiles()

        currentPlaying.seek(0)
        currentPlaying.truncate() 
        currentPlaying.write(str(newIndex))

    play_audio(newIndex)

def stopSong():
    pygame.mixer.music.stop()




# Select and perform an operation based on the message
def selectOperation(message):
    match message:
        case "play":
            if not isPlaying():
                play_audio()
        case "pause":
            if isPlaying():
                pause_audio()
        case "resume":
            if not isPlaying():
                resume_audio()
        case "restart": 
            if isPlaying():
                restart_audio()
        case "stop":
            if isPlaying():
                stopSong()
        case "skip":
            if isPlaying():
                skipSong()
        case _:
            print("Keyword not found")

# Continuous loop to check for commands
while True:
    try:
        with open("music.txt", 'r') as file:
            message = file.readline().strip().lower()

        if message:
            selectOperation(message)

            with open("music.txt", 'w') as file:
                file.truncate(0)

        time.sleep(1)  
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)  
