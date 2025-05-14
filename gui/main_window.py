from core.clicker import ClickerThread
from core.hotkey import GlobalHotkeyListener
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QSizePolicy
from PyQt6.QtCore import pyqtSlot

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutoClicker")
        self.setFixedSize(250, 150)

        self.clicker_thread = ClickerThread()
        self.hotkey_listener = GlobalHotkeyListener()
        self.hotkey_listener.toggle_signal.connect(self.toggle_clicker)
        self.hotkey_listener.start()

        self.button = QPushButton("Start")
        self.button.clicked.connect(self.toggle_clicker)

        self.hotkey_label = QLabel("Press F6 to start/stop the clicker")
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.hotkey_label)
        main_layout.addWidget(self.button)
        self.setLayout(main_layout)

    @pyqtSlot()
    def toggle_clicker(self):
        if not self.clicker_thread.isRunning():
            self.clicker_thread = ClickerThread()  # serve creare nuovo thread ogni volta
            self.clicker_thread.start()
            self.button.setText("Stop")
        else:
            self.clicker_thread.stop()
            self.button.setText("Start")