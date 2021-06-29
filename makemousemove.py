import pyautogui
import time
time.sleep(2)
print(pyautogui.position())
pyautogui.click(15, 10, 1, 1, pyautogui.PRIMARY)
pyautogui.click(368, 158, 1, 1, pyautogui.PRIMARY)
time.sleep(2)
pyautogui.typewrite("Me Idiot !")