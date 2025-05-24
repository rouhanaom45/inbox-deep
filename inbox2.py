import pyautogui
import time
import random
import subprocess
import string

def random_click(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.moveTo(x + random.uniform(-2, 2), y + random.uniform(-2, 2), duration=random.uniform(0.1, 0.4))
    pyautogui.click()

# Start with 1 second delay
time.sleep(1)

# Run load.py
subprocess.run(["python", "load.py"])
time.sleep(1)

# Click fixed point
pyautogui.click(1139, 365)
time.sleep(1)
random_click((110, 215), (303, 386))
time.sleep(random.uniform(1.0, 2.0))
# Perform random click in given rectangle
random_click((887, 384), (948, 402))

# Wait between 4 to 5 seconds
time.sleep(random.uniform(7.0, 8.5))

random_click((81, 211), (351, 535))
time.sleep(random.uniform(1.0, 2.0))

for _ in range(random.randint(6, 8)):
    pyautogui.press("down")
    time.sleep(0.35)

time.sleep(1)

random_click((804, 516), (873, 532))
time.sleep(random.uniform(7.0, 8.5))

random_click((470, 574), (507, 588))
time.sleep(random.uniform(4.0, 5.5))

random_click((478, 553), (506, 561))
time.sleep(random.uniform(4.0, 5.5))

random_click((64, 170), (348, 524))
time.sleep(random.uniform(1.0, 1.5))

for _ in range(random.randint(6, 8)):
    pyautogui.press("down")
    time.sleep(0.35)

time.sleep(1)


random_click((477, 259), (824, 273))
time.sleep(random.uniform(1.0, 1.5))


random_click((485, 323), (767, 484))
time.sleep(random.uniform(1.0, 1.5))

random_click((480, 437), (764, 450))
time.sleep(random.uniform(1.0, 1.5))

pyautogui.hotkey('ctrl', 'a')
time.sleep(0.5)

# Generate a name with 68 letters, alternating consonant and vowel, followed by two digits
consonants = ''.join(set(string.ascii_lowercase) - set('aeiou'))
vowels = 'aoiu'

length = random.randint(3, 4)  # Because each consonant-vowel pair is 2 chars
name = ''.join(random.choice(consonants) + random.choice(vowels) for _ in range(length))
name += ''.join(random.choices(string.digits, k=2))

# Type like a human
for char in name:
    pyautogui.write(char)
    time.sleep(random.uniform(0.08, 0.2))

time.sleep(random.uniform(1, 1.6))

random_click((834, 517), (877, 533))
time.sleep(random.uniform(1.0, 1.5))
