import pyautogui
import time
import os
import sys

time.sleep(1.8)

button_images = [
    'create_button.png'
]

max_attempts = 20

for image in button_images:
    if not os.path.isfile(image):
        print(f"Error: The image file '{image}' does not exist.")
        sys.exit(1)

for attempt in range(max_attempts):
    print(f"Attempt {attempt + 1} of {max_attempts}: Attempting to detect verification buttons...")
    time.sleep(2)

    for image in button_images:
        try:
            print(f"Trying to detect: {image}")
            location = pyautogui.locateOnScreen(image, confidence=0.8)
        except Exception as e:
            print(f"Error while detecting '{image}': {e}")
            location = None

        if location:
            print(f"'{image}' detected at {location}, clicking...")
            time.sleep(1.5)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(1)
            sys.exit(0)  # Success: button detected

    print("No buttons detected in this attempt. Pressing Down Arrow key to continue...")
    time.sleep(1)

print("Maximum detection attempts reached. Exiting...")
time.sleep(1)
pyautogui.hotkey('ctrl', 't')
time.sleep(1)
pyautogui.write('www.deepnote.com')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(6)
pyautogui.hotkey('ctrl', 'shift', 'tab')
time.sleep(1)
pyautogui.hotkey('ctrl', 'w')
time.sleep(1.5)
sys.exit(1)  # Failure: max attempts reached
