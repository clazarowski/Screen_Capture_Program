import sys
import os
import keyboard
from PIL import ImageGrab
from datetime import datetime

def create_folder_if_not_exists():
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
        print("Folder screenshots create")

def screen_capture():
    #Capture Screen
    screenshot = ImageGrab.grab()

    #Screen save
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    filename = f"screenshots/{timestamp}.png"
    screenshot.save(filename)

    #Close Screen capture
    screenshot.close()
    print(f"Screenshot save as {filename}")

create_folder_if_not_exists()
keyboard.add_hotkey('F9', screen_capture)
keyboard.wait('esc')
print("Program Close")