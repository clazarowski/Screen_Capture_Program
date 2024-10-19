import sys
from PIL import ImageGrab
from datetime import datetime

def screen_capture():
    #Capture Screen
    screenshot = ImageGrab.grab()

    #Screen save
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    filename = f"screenshots\\{timestamp}.png"
    screenshot.save(filename)

    #Close Screen capture
    screenshot.close()

screen_capture()