import subprocess
import time
import pyautogui

print("Launching Google Chrome...")

# Path to Chrome browser executable
chrome_path = "/usr/bin/google-chrome"

# URL to open
url = "https://www.cloudskillsboost.google/"  # Replace with the URL you want to visit

# Launch Chrome in the background (non-blocking)
subprocess.Popen([
    chrome_path,
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--disable-software-rasterizer",
    "--remote-debugging-port=9222",
    url
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True)

# Allow the browser to launch and stabilize
time.sleep(4)
pyautogui.click(849, 490)
time.sleep(3.4)
pyautogui.click(1125, 567)
time.sleep(2)
pyautogui.click(1125, 567)
time.sleep(4)
