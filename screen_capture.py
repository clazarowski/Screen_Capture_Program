import os
import keyboard
import mss
from datetime import datetime

def create_folder_if_not_exists():
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
        print("Folder screenshots created")

def screen_capture():
    with mss.mss() as sct:
        monitor = sct.monitors[2]  # 0 - all, 1 - first monitor, 2 - second monitor 
        screenshot = sct.grab(monitor)

        # Save screeen
        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        filename = f"screenshots/{timestamp}.png"
        mss.tools.to_png(screenshot.rgb, screenshot.size, output=filename)

        print(f"Screenshot saved as {filename}")

create_folder_if_not_exists()
keyboard.add_hotkey('F9', screen_capture)
keyboard.wait('esc')
print("Program closed")