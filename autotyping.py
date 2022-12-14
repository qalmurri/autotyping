import pyautogui
from pynput.keyboard import *
import time

delay = 1
message = 'wh'
resume_key = Key.home
pause_key = Key.end
exit_key = Key.esc

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print('======SETTING======')
    print("message = " + message)
    print("delay = " + str(delay))
    print("Home = Resume")
    print("End = Pause")
    print("Esc = Exit")

def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.typewrite(message)
            pyautogui.press('enter') 
            time.sleep(delay)

    lis.stop()


if __name__ == "__main__":
    main()
