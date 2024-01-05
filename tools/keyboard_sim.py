from pynput.keyboard import Key, Controller
import time

if __name__ == '__main__':
    keyboard = Controller()

    time.sleep(2)
    # for char in "qrqrqr":
    keyboard.press("a")
    time.sleep(2)
    keyboard.release("a")
    # time.sleep(0.12)
