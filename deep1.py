import pyautogui
import subprocess
import time
import random
import string
import pyperclip

def random_click(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.moveTo(x + random.uniform(-2, 2), y + random.uniform(-2, 2), duration=random.uniform(0.1, 0.4))
    pyautogui.click()

def human_type(text, interval_range=(0.05, 0.15)):
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(*interval_range))

def generate_random_two_char_name():
    # You can tweak this logic to use only letters or include digits
    return ''.join(random.choices(string.ascii_lowercase, k=2))

# Loop until create.py succeeds
while True:
    # Step 1: Sleep for 1.5 seconds
    time.sleep(1.5)

    # Step 2: Run start.py
    subprocess.run(["python", "start.py"])

    # Step 3: Sleep for 8 seconds
    time.sleep(8)

    # Step 4: Generate and type a random 2-character name
    random_name = generate_random_two_char_name()
    human_type(random_name)

    # Step 5: Sleep for 2 seconds
    time.sleep(2)

    # Step 6: Run oki.py
    subprocess.run(["python", "oki.py"])

    time.sleep(1)

    random_click((72, 254), (287, 522))
    time.sleep(random.uniform(0.5, 1.0))

    for _ in range(random.randint(6, 8)):
        pyautogui.press("down")
        time.sleep(0.35)

    time.sleep(1)

    random_click((516, 313), (822, 323))
    time.sleep(random.uniform(0.5, 1.0))
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)

    clipboard_text = pyperclip.paste()
    if clipboard_text:
        human_type(clipboard_text)
    else:
        print("Clipboard is empty.")

    time.sleep(random.uniform(0.5, 1.0))

    random_click((521, 358), (812, 373))
    time.sleep(random.uniform(6.0, 8.0))

    # Run create.py and check return code
    result = subprocess.run(["python", "create.py"])
    if result.returncode == 0:
        print("create.py succeeded. Continuing with remaining steps...")
        break  # Exit loop and continue with final step
    else:
        print("create.py failed. Restarting deep1.py...")
        continue  # Restart the loop

# Final step after create.py succeeds
time.sleep(1)
print("deep1.py finished successfully.")
