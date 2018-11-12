from PIL import ImageGrab, ImageOps, Image, ImageDraw
import pyautogui
import time
from numpy import *
import os
import tempfile
import subprocess 

class Cordinates():
    def __init__(self, x, y):
        # retina issue
        self.x = x / 2
        self.y = y / 2

    # def __getattr__(self, coord):
        # return self.coord / 2

    def pil_oords(self):
        return (self.x, self.y)

replayBtn = Cordinates(950,750)
dinosaur = Cordinates(490,770)

def restartGame():
    pyautogui.click(replayBtn.pil_oords(), clicks=2)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.23)
    pyautogui.keyUp('space')

def imageGrab():
    box = (dinosaur.x+69, dinosaur.y - 20, 40, 30)
    image = grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    # print(a.sum())
    return a.sum() 


def grab(bbox=None):
    f, file = tempfile.mkstemp('.png')
    os.close(f)
    if bbox:
        subprocess.call(['screencapture', '-R{}'.format(','.join(map(str, map(int, bbox)))), file])
    else:
        subprocess.call(['screencapture', '-x', file])
    im = Image.open(file)
    im.load()
    # im.show()
    # im.close()
    os.unlink(file)
    return im

def main():
    restartGame()
    jumps = 0
    while True:
        if(imageGrab() != 5045):
            jumps += 1
            print(jumps)
            pressSpace()
            

main()

# os.system("screencapture -R175,280,600,175 filename.png")
# im = Image.open("filename.png")
# im.show()

# import pyscreenshot
# screenshot=pyscreenshot.grab(bbox=(175,280,600,175))
# # screenshot.show()
# pyscreenshot.grab_to_file('screenshot.png')

