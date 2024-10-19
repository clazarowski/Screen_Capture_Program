import os
import keyboard
import mss
from datetime import datetime
import time
import threading
from PyQt5 import QtWidgets, QtCore

class ScreenshotApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.capture_thread = None
        self.is_capturing = False

    def initUI(self):
        self.setWindowTitle("Screenshot Capture Tool")
        self.setGeometry(100, 100, 300, 150)

        self.start_button = QtWidgets.QPushButton("Start Capture", self)
        self.start_button.clicked.connect(self.start_capture)
        self.start_button.setGeometry(50, 30, 200, 30)

        self.stop_button = QtWidgets.QPushButton("Stop Capture", self)
        self.stop_button.clicked.connect(self.stop_capture)
        self.stop_button.setGeometry(50, 70, 200, 30)

        self.status_label = QtWidgets.QLabel("", self)
        self.status_label.setGeometry(50, 110, 200, 30)

    def create_folder_if_not_exists(self):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
            print("Folder screenshots created")

    def screen_capture(self):
        with mss.mss() as sct:
            monitor = sct.monitors[2]  # 0 - all, 1 - first monitor, 2 - second monitor 
            screenshot = sct.grab(monitor)

            # Save screen
            timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            filename = f"screenshots/{timestamp}.png"
            mss.tools.to_png(screenshot.rgb, screenshot.size, output=filename)

            print(f"Screenshot saved as {filename}")

    def capture_screenshots(self):
        self.create_folder_if_not_exists()
        self.status_label.setText("Capturing...")

        while self.is_capturing:
            if keyboard.is_pressed('F9'): 
                self.screen_capture()
                time.sleep(1)
            elif keyboard.is_pressed('F10'):
                break

        self.status_label.setText("Stopped capturing.")
    
    def start_capture(self):
        self.is_capturing = True
        self.capture_thread = threading.Thread(target=self.capture_screenshots)
        self.capture_thread.start()

    def stop_capture(self):
        self.is_capturing = False
        if self.capture_thread is not None:
            self.capture_thread.join()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    screenshot_app = ScreenshotApp()
    screenshot_app.show()
    app.exec_()