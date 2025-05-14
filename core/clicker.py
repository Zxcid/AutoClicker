from PyQt6.QtCore import QThread
import pyautogui
import time

class ClickerThread(QThread):
    def __init__(self):
        super().__init__()
        self._running = False

    def run(self):
        self._running = True
        while self._running:
            pyautogui.click()
            time.sleep(1)

    def stop(self):
        self._running = False
