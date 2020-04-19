import pyautogui
import time

comments = [ "Text","Text","Text","Text","Text","Text","Text" ]

time.sleep(5)

for i in range(2000):
    pyautogui.typewrite(comments[i%7])
    pyautogui.typewrite("\n")
    time.sleep(2)