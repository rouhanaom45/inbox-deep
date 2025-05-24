import pyautogui
import time
import random
import subprocess

def random_click(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.moveTo(x + random.uniform(-2, 2), y + random.uniform(-2, 2), duration=random.uniform(0.1, 0.4))
    pyautogui.click()

def human_type(text, interval_range=(0.05, 0.15)):
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(*interval_range))

# Start script
time.sleep(1)

subprocess.run(["python", "tasks.py"])
time.sleep(1)

# First random click
random_click((714, 439), (778, 450))
time.sleep(random.uniform(0.5, 1.0))

# Type random year between 1985 and 2001
year = str(random.randint(1985, 2001))
human_type(year)
time.sleep(random.uniform(1.0, 2.0))

# Click 2nd area
random_click((470, 435), (510, 454))
time.sleep(random.uniform(1.0, 1.4))

# Click 3rd area
random_click((473, 37), (497, 382))
time.sleep(random.uniform(1.0, 1.3))

# Click 4th area
random_click((560, 436), (666, 453))
time.sleep(random.uniform(1.0, 1.5))
random_click((566, 110), (655, 411))
time.sleep(random.uniform(1.0, 1.5))

# Click 5th area
random_click((473, 552), (542, 569))
time.sleep(random.uniform(1.0, 1.6))

# Click 6th area
random_click((480, 491), (529, 523))
time.sleep(random.uniform(1.0, 1.3))

# Click 7th area
random_click((90, 257), (320, 540))
time.sleep(random.uniform(0.5, 1.0))

for _ in range(random.randint(6, 8)):
    pyautogui.press("down")
    time.sleep(0.35)

time.sleep(1)

random_click((837, 515), (879, 531))
time.sleep(random.uniform(0.5, 1.0))

time.sleep(8)

for _ in range(random.randint(7, 9)):
    pyautogui.press("down")
    time.sleep(0.35)

time.sleep(1)

random_click((833, 514), (875, 530))
time.sleep(random.uniform(0.5, 1.0))
time.sleep(3)
subprocess.run(["python", "finish0.py"])
time.sleep(1)
pyautogui.hotkey('ctrl', 't')
time.sleep(1)
pyautogui.click(438, 61)
time.sleep(0.5)
pyautogui.write('https://email.inbox.lv/mailbox')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(7)
pyautogui.hotkey('ctrl', 'shift', 'tab')
time.sleep(1)
pyautogui.hotkey('ctrl', 'w')
time.sleep(1.5)
subprocess.run(["python", "finish.py"])
time.sleep(1.7)
pyautogui.click(94, 63)
time.sleep(8)

pyautogui.hotkey('ctrl', 't')
time.sleep(1)
pyautogui.write('www.deepnote.com')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(5)
