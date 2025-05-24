import os
import subprocess

# Path to Chrome browser executable
chrome_path = "/usr/bin/google-chrome"

# URL to open
url = "https://www.outlook.com"  # Change as needed

# Read the extracted profile folder name
profile_file = "chrome_profile_path.txt"

if os.path.exists(profile_file):
    with open(profile_file, "r") as f:
        profile_dir = f.read().strip()
else:
    print("Profile directory file not found!")
    exit(1)

# Ensure that the extracted profile directory exists
if os.path.exists(profile_dir):
    print(f"Launching Chrome with profile: {profile_dir}")

    # Run Chrome in the background and detach it from the terminal
    subprocess.Popen([
        chrome_path,
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-gpu",
        "--disable-software-rasterizer",
        f"--user-data-dir={profile_dir}",
        "--remote-debugging-port=9222",
        url
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True)

else:
    print(f"Profile directory {profile_dir} does not exist.")
