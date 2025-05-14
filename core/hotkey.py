from PyQt6.QtCore import QThread, pyqtSignal
from pynput import keyboard

class GlobalHotkeyListener(QThread):
    toggle_signal = pyqtSignal()

    def __init__(self, hotkey: str = 'f6'):
        super().__init__()
        self.hotkey = hotkey.lower()

    def set_hotkey(self, key_name: str):
        self.hotkey = key_name.lower()

    def run(self):
        def on_press(key):
            try:
                key_name = key.name if hasattr(key, 'name') else key.char
                if key_name.lower() == self.hotkey:
                    self.toggle_signal.emit()
            except AttributeError:
                pass

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
