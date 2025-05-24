#!/bin/bash


scripts=(
  "google.py"
  "capcha.py"
  "inbox1.py"
  "inbox2.py"
  "inbox3.py"
  "deep1.py"
  "confirm.py"
  "deep2.py"
  "api.py"
  "create-project.py"

  
)

# Run each script in order
for script in "${scripts[@]}"; do
  echo "Running $script..."
  python3 "$script"
  if [ $? -ne 0 ]; then
    echo "Error: $script failed. Exiting."
    exit 1
  fi
  echo "$script finished successfully."
done

sleep 2.5

bash upload.sh
sleep 2
echo "stop now" > /root/failure.txt
sleep 1
