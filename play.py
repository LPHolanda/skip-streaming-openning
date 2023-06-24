from ast import Break
import pyautogui
import time
# from pynput import keyboard
import keyboard

count = 0
run = True

# def on_release(self, key, *args):
#     if keyboard.Key.f4 in args:
#         print("pedi pra parar parou")
#         global run
#         run = False

# def create_listener():
#     listener = keyboard.Listener(on_release=lambda key, *args: self.on_release(self, key, *args))
#     listener.start()

# if keyboard.read_key() == "f4":
#     print("======================================")
#     run = False

pyautogui.useImageNotFoundException()

def autoplay():
    global run
    while run:
        global count 
        count = count+1
        print("autoplay", count)
        try:
            play = pyautogui.locateOnScreen('spotify-play.png')
            pyautogui.click(play)
            time.sleep(10)
            autoplay()
        except pyautogui.ImageNotFoundException:
            print('ImageNotFoundException: image not found')
        

autoplay()