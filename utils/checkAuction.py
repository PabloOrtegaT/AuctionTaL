import pyautogui
import time
import pygame
import time
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# For reference
# pyautogui.locateOnScreen receives the image that we want to locate in the -main- screen (if you're using 2 screens be aware about this)
# then we give a threshold of confidence (same as how likely the image needs to be in order to match)
# then, for the region, we give the portion of the screen where we want to look for that image, tiny window means it will run faster

def run():
    referenceFound = None
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.5)

    while referenceFound == None:
        ten = pyautogui.locateOnScreen('.\images\\10.png', confidence=0.90, grayscale=True, region=[3662, 354, 100, 100])
        if ten is not None: 
            referenceFound = True

        preciousLito = pyautogui.locateOnScreen('.\images\\PreciousLitograph.png', confidence=0.70, grayscale=True, region=[2500, 340, 1000, 1750])
        if preciousLito is not None: 
            referenceFound = True
            
        # rareLito = pyautogui.locateOnScreen('.\images\\RareLitograph.png', confidence=0.70, grayscale=True)
        # if rareLito is not None: 
        #     referenceFound = True

        phantom = pyautogui.locateOnScreen('.\images\\Phantom.png', confidence=0.74, grayscale=True, region=[2500, 340, 1000, 1750])
        if phantom is not None: 
            referenceFound = True

        rareLito = pyautogui.locateOnScreen('.\images\\Shadow.png', confidence=0.74, grayscale=True, region=[2500, 340, 1000, 1750])
        if rareLito is not None: 
            referenceFound = True

        shockCommander = pyautogui.locateOnScreen('.\images\\ShockCommander.png', confidence=0.74, grayscale=True, region=[2500, 340, 1000, 1750])
        if shockCommander is not None: 
            referenceFound = True

        queenBella = pyautogui.locateOnScreen('.\images\\QueenBellandir.png', confidence=0.74, grayscale=True, region=[2500, 340, 1000, 1750])
        if queenBella is not None: 
            referenceFound = True

        if referenceFound is None:
            print("Nothing found so far...")

        if referenceFound is not None:
            # Play a sound when a match is found
            print('Found something!')
            pygame.mixer.music.load("bubble.wav")
            pygame.mixer.music.play()
            pygame.mixer.music.fadeout(15000)
            time.sleep(1)
        
    
