#!/bin/bash

# Run the install.py script and wait for it to complete

python3 google.py
if [ $? -ne 0 ]; then
    echo "google.py encountered an error. Exiting."
    exit 1
fi



# Run the profile.sh script and wait for it to complete
bash profile.sh
if [ $? -ne 0 ]; then
    echo "profile.sh encountered an error. Exiting."
    exit 1
fi

# Run the Python script to launch Chrome in the background
nohup python3 launch_chrome.py > chrome.log 2>&1 &

# Wait longer for Chrome to fully load
sleep 5

# Ensure Chrome is running before proceeding
if ! pgrep -x "chrome" > /dev/null; then
    echo "Chrome failed to start. Exiting."
    exit 1
fi

# Perform automated clicks using xdotool
python3 click.py
if [ $? -ne 0 ]; then
    echo "click.py encountered an error. Exiting."
    exit 1
fi


# Ensure Chrome is still running before executing the next scripts
if ! pgrep -x "chrome" > /dev/null; then
    echo "Chrome closed unexpectedly. Exiting."
    exit 1
fi
