import pyautogui
import time
import random
import subprocess
import string

def human_type(text, interval_range=(0.05, 0.15)):
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(*interval_range))

def random_click(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.moveTo(x + random.uniform(-2, 2), y + random.uniform(-2, 2), duration=random.uniform(0.1, 0.4))
    pyautogui.click()

def generate_patterned_name(length=6, with_digits=False):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    name = ''
    for _ in range(length // 2):
        name += random.choice(consonants) + random.choice(vowels)
    if len(name) < length:
        name += random.choice(vowels)
    if with_digits:
        name += f"{random.randint(10, 99)}"
    return name[:length] + (name[length:] if with_digits else '')

def generate_password(length=10):
    chars = string.ascii_letters + string.digits + ",;!:@."
    return ''.join(random.choice(chars) for _ in range(length))

# Start the automation
pyautogui.write("https://login.inbox.lv/signup?go=portal")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(7)

# Run oki.py
subprocess.run(["python", "oki.py"])
time.sleep(1)
random_click((77, 234), (281, 505))
time.sleep(random.uniform(0.5, 1.0))

for _ in range(random.randint(6, 8)):
    pyautogui.press("up")
    time.sleep(0.35)

time.sleep(1)
# 1st Click
random_click((675, 298), (754, 311))
time.sleep(random.uniform(0.5, 1.0))

# 2nd Click
random_click((661, 340), (779, 352))
time.sleep(random.uniform(1.0, 1.5))

# 3rd Click
random_click((488, 298), (622, 314))
time.sleep(random.uniform(0.7, 1.0))

# Random name + 2 digits
name_with_digits = generate_patterned_name(random.randint(6, 8), with_digits=True)
human_type(name_with_digits)
time.sleep(random.uniform(1.0, 2.0))

# 4th Click
random_click((488, 465), (753, 476))
time.sleep(random.uniform(0.7, 1.0))

# Random name
name1 = generate_patterned_name(random.randint(6, 8))
human_type(name1)
time.sleep(random.uniform(1.2, 2.3))

# 5th Click
random_click((489, 517), (747, 524))
time.sleep(random.uniform(0.7, 1.0))

# Random name
name2 = generate_patterned_name(random.randint(6, 8))
human_type(name2)
time.sleep(random.uniform(1.2, 2.3))

# 6th Click
random_click((491, 567), (678, 578))
time.sleep(random.uniform(0.7, 1.0))

# Random password
password = generate_password(random.randint(9, 11))
human_type(password)
time.sleep(random.uniform(1.0, 2.0))

# 7th Click
random_click((92, 250), (361, 529))
time.sleep(random.uniform(0.5, 1.0))

# Press down arrow 68 times
for _ in range(random.randint(6, 8)):
    pyautogui.press("down")
    time.sleep(0.35)

time.sleep(1)

# Click (478,479) then (477,446)
pyautogui.click(478, 479)
time.sleep(1)
pyautogui.click(477, 446)
time.sleep(1.9)

# Hold down arrow key for 2734 seconds
pyautogui.keyDown('down')
time.sleep(random.uniform(20, 25))
pyautogui.keyUp('down')
time.sleep(random.uniform(1, 2))

# 8th Click
random_click((1063, 547), (1111, 561))
time.sleep(random.uniform(2.0, 2.6))

# 9th Click
random_click((648, 510), (694, 526))
time.sleep(random.uniform(5.0, 7.0))
