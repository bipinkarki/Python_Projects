import pyautogui
from PIL import Image, ImageGrab
import time


def hit(key):
    pyautogui.press(key)
    return


def isCollide(data):
    # Draw a rectangle for cactus:
      for i in range(350, 400):
        for j in range(595, 710):
            if data[i,j]<100:
                hit("up")
                return
    # Draw a rectangle for bird:
      for i in range(300, 320):
        for j in range(500, 595):
            if data[i,j]<171:
                hit("down")
                return
      return
        

if __name__ == '__main__':
    time.sleep(5)
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

 
        
