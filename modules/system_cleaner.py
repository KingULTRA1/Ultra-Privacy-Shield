# system_cleaner.py
# Cleans system temporary files, browser caches, and cookies

import os
import shutil
import platform

def clear_temp():
    temp_dir = os.getenv("TEMP") if platform.system() == "Windows" else "/tmp"
    for root, dirs, files in os.walk(temp_dir):
        for f in files:
            try: os.remove(os.path.join(root, f))
            except: pass
        for d in dirs:
            try: shutil.rmtree(os.path.join(root, d))
            except: pass
    print(f"[INFO] Cleared temp files in {temp_dir}")

def clear_browser_cache():
    paths = []
    if platform.system() == "Windows":
        paths.append(os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache"))
        paths.append(os.path.expandvars(r"%APPDATA%\Mozilla\Firefox\Profiles"))
    else:
        paths.append(os.path.expanduser("~/.cache/google-chrome/Default"))
        paths.append(os.path.expanduser("~/.mozilla/firefox"))

    for path in paths:
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                print(f"[INFO] Cleared cache: {path}")
            except: pass
