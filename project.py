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

random_click_in_area((1334, 103), (1348, 119))
time.sleep(random.uniform(1, 1.5))

random_click_in_area((1129, 179), (1314, 191))
time.sleep(random.uniform(4, 5.5))

random_click_in_area((1189, 106), (1282, 119))
time.sleep(random.uniform(4, 5.5))

subprocess.run(["python3", "ready.py"])
time.sleep(3.5)

random_name = generate_random_name(random.randint(6, 8))
human_typing(random_name)
time.sleep(random.uniform(0.5, 1))

pyautogui.press('enter')
time.sleep(random.uniform(2, 2.6))
subprocess.run(["python3", "clip.py"])
time.sleep(1.5)
subprocess.run(["python3", "nootebook.py"])
time.sleep(1)
random_click_in_area((29, 577), (165, 590))
time.sleep(random.uniform(7, 8.5))

random_click_in_area((215, 578), (229, 590))
time.sleep(random.uniform(1.3, 1.9))
random_click_in_area((153, 590), (222, 599))
time.sleep(random.uniform(1.3, 1.9))

pyautogui.click(64, 551)
time.sleep(random.uniform(1.3, 1.9))

random_click_in_area((154, 593), (219, 601))
time.sleep(random.uniform(1.3, 1.9))

random_click_in_area((213, 480), (229, 495))
time.sleep(random.uniform(1.3, 1.9))
pyautogui.click(92, 63)
time.sleep(3)
subprocess.run(["python3", "ready.py"])
time.sleep(1)
random_click_in_area((1285, 106), (1298, 118))
time.sleep(random.uniform(1.3, 1.9))
random_click_in_area((1104, 223), (1241, 230))
time.sleep(random.uniform(1.6, 1.9))
subprocess.run(["python3", "save.py"])
time.sleep(1)
