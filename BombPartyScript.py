# Script that plays bombpary on jklm.fun 
# works with fullscreen chrome on 1080p
# by Andrew Van Hoveln

from pynput.keyboard import Controller, Key
import time
import os
import keyboard
import pyautogui
import pytesseract
import cv2
import random
from PIL import ImageFilter

keyboard2 = Controller()

def parseImage():
    myScreenshot = pyautogui.screenshot(region=(700, 470, 200, 200))
   
    width, height = myScreenshot.size
    
    # debugging purposes
    # myScreenshot.save('before.png')

    for x in range(0, width):
        for y in range(0, height):
            r,g,b = myScreenshot.getpixel((x,y))
            if r < 210 or b < 210 or g < 210:
                myScreenshot.putpixel((x,y), (255, 255, 255, 255))
            else:
                myScreenshot.putpixel((x,y), (0, 0, 0, 255))

    # debugging purposes
    myScreenshot.save('img.png')

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    text = pytesseract.image_to_string(myScreenshot, lang="eng", config='--psm 6')
    
    #print(text)
    return text
    
def remove_end_spaces(string):
    return "".join(string.rstrip()).replace('1', 'I').replace('l', 'I').replace('(', 'I').replace(')', 'I').replace('uI', 'LI')

while True:
    while True:
        if(keyboard.is_pressed('F8')):
            break
    
    t = parseImage()

    t = remove_end_spaces(t)
    print(t)
    
    
    words = []
    fileLocation = os.path.dirname(os.path.realpath(__file__))
    with open(fileLocation + "\\wordlist", "r") as file:
        for line in file:
            if(t.upper() in line[:len(line) - 1]):
                words.append(line[:len(line) - 1])

    words.sort(reverse=True)

    if(len(words) == 0):
        print("none found\n")
        continue
    
    num = random.randint(0, len(words))
    topWord = words[num]

    for char in topWord:
        keyboard2.press(char)
        keyboard2.release(char)
        time.sleep(0.1)
    keyboard2.press(Key.enter)
    keyboard2.release(Key.enter)
