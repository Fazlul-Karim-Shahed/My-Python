
import pyautogui
import time
count = 18


while True:
    time.sleep(1)

    pyautogui.write("Oiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    pyautogui.press("enter")
    pyautogui.write("koiiiiiii")
    pyautogui.press("enter")
    count = count + 2

    print(count)




