# AutoClicker

**AutoClicker** is a lightweight desktop application written in Python that simulates automatic mouse clicks. The tool provides a minimal GUI with a simple **Start/Stop** button and can be triggered using a global hotkey (F6). It's ideal for testing, automation, or repetitive tasks requiring fast and continuous mouse interaction.

## 📦 Project Structure

```
autoclicker/
├── main.py                  # Application entry point
├── core/
│   ├── clicker.py           # ClickerThread logic (PyAutoGUI)
│   ├── hotkey.py            # Global hotkey listener (pynput)
├── gui/
│   └── main_window.py       # GUI built with PyQt6
```

## 🛠️ Tech Stack

- **Python** 3.13
- **PyQt6** 6.9.0 – GUI toolkit
- **PyAutoGUI** 0.9.54 – Automated mouse control
- **pynput** 1.8.1 – Global hotkey listening
- **PyInstaller** 6.13.0 – For creating standalone executables

## 🚀 Features

- Start/Stop button to control the clicker manually
- Global hotkey support (F6) to toggle the clicker in the background
- Thread-based implementation for responsive UI and background execution
- Minimal and distraction-free layout

## 🖥️ How to Use

### Run from source

1. Install the dependencies (preferably in a virtual environment):

   ```bash
   pip install -r requirements.txt
   ```

   Or manually:

   ```bash
   pip install pyqt6==6.9.0 pyautogui==0.9.54 pynput==1.8.1
   ```

2. Run the application:

   ```bash
   python main.py
   ```

3. Click the **Start** button or press **F6** to begin auto-clicking.
4. Click **Stop** or press **F6** again to halt the process.

### Build an executable

To package the application into a standalone executable:

```bash
pyinstaller --onefile --noconsole main.py
```

> Adjust paths and settings in the PyInstaller configuration if using `ui_main_window.ui` or other external resources.

## 🛑 Hotkey Behavior

- Default hotkey: **F6**
- Works globally (even if the application window is not focused)
- You can change the hotkey in the `hotkey.py` file

## 📋 Notes

- On Windows, some systems may require the app to be run as **Administrator** to properly capture global hotkeys.
- Ensure the PyAutoGUI has access to control the mouse. On macOS, it may require Accessibility permissions.

## 📄 License

MIT License – see [LICENSE](LICENSE) for details.

---

Developed with ❤️ using Python & Qt.