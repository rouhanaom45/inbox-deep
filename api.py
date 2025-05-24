import pyautogui
import time
import random
import string
import subprocess

time.sleep(2)

def human_typing(text):
    """Simulate human-like typing."""
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.15))

def random_click_in_area(top_left, bottom_right):
    """Perform a random click within a rectangular area."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.click(x, y)

def generate_random_name(length=6):
    """Generate a random name with alternating consonant and vowel."""
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))
    name = ""
    for _ in range(length):
        name += random.choice(consonants) + random.choice(vowels)
    return name[:length]


subprocess.run(["python3", "ready.py"])
time.sleep(3.5)
subprocess.run(["python3", "stop.py"])
time.sleep(2)
subprocess.run(["python3", "down.py"])
time.sleep(2)

random_click_in_area((1334, 103), (1348, 119))
time.sleep(random.uniform(1, 1.5))

random_click_in_area((1129, 179), (1314, 191))
time.sleep(random.uniform(4, 5.5))

random_click_in_area((21, 215), (169, 229))
time.sleep(random.uniform(4, 5.5))

random_click_in_area((456, 245), (542, 254))
time.sleep(random.uniform(3, 3.8))

random_click_in_area((264, 242), (290, 503))
time.sleep(random.uniform(1, 1.5))

for _ in range(random.randint(8, 10)):
    pyautogui.press('down')
    time.sleep(random.uniform(0.5, 0.8))

time.sleep(1)

random_click_in_area((1213, 400), (1285, 416))
time.sleep(random.uniform(2, 2.5))

random_name = generate_random_name(random.randint(6, 8))
human_typing(random_name)
time.sleep(random.uniform(0.5, 1))

random_click_in_area((813, 424), (869, 437))
time.sleep(random.uniform(2, 2.5))

random_click_in_area((862, 387), (869, 393))
time.sleep(random.uniform(1, 1.5))

random_click_in_area((831, 465), (866, 477))
time.sleep(random.uniform(2, 2.5))

subprocess.run(["python3", "save.py"])
