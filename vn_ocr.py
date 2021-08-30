from glob import glob
from PIL import Image, ImageGrab
import pytesseract
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import pyautogui
from pynput import mouse
import time
import image_util as iu
import copy
import win32clipboard

#end python program with CTRL+C

#Settings

#number of areas, min. 1
n = 1 
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

###############################################################
#Setup rectangular screenshot areas by clicking in upper left corner, drag to lower right corner, and release
areas = []

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    areas.append((x, y))
    if not pressed:
        # Stop listener by returning false
        return False

for x in range(n):
  # Collect events until released
    with mouse.Listener(
        on_click=on_click) as listener:
        listener.join()

print(areas)

#Methods
images = []
images_old = [] #for comparison
text = []

def take_screenshots():
    global images, images_old
    images_old = copy.deepcopy(images)
    images.clear()
    for x in range(0,2*n,2):
        images.append(ImageGrab.grab(bbox =(areas[x][0], areas[x][1],areas[x+1][0], areas[x+1][1])))
    
def compare_screenshots():
    for x in range(len(images)):
        norm = iu.compare_images_manhatten(np.asarray(images[x]), np.asarray(images_old[x]))
        time.sleep(1)
        print(norm)
        if (norm < 2000):
            return False #no changes

    # print("change!")
    # images[0].save('out.bmp')

    return True #areas have changed

def ocr(images):
    global text
    text.clear()
    for x in range(n):
        text.append(pytesseract.image_to_string(images[x], lang='jpn'))
    
    
def paste_to_clipboard():
    for x in range(n):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        print(text[x])
        win32clipboard.SetClipboardText(text[x])
        win32clipboard.CloseClipboard()


#looped until user stops by pressing CTRL+C
try:
    take_screenshots() #init the old array somehow
    while True:
        take_screenshots()
        changes = compare_screenshots()
        if(changes):
            #optional preprocessing is missing
            ocr(images)
            paste_to_clipboard()
except KeyboardInterrupt:
    pass




