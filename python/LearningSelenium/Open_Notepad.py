import subprocess
import pyautogui
subprocess.Popen([r"C:\Windows\System32\notepad.exe"])
pyautogui.hotkey("ctrl", "t")  # Example shortcut for "New Tab"
# app = Application(backend="uia").connect(title="Untitled - Notepad")
# app.Notepad.TypeText("Hello World")