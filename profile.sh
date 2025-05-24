#!/bin/bash

# Server URL to fetch the Chrome profile ZIP file link
SERVER_URL="https://fe38ebf6-c57e-4ba5-b241-eef83b85ea53.deepnoteproject.com/get_item"

# Fetch the JSON response
response=$(curl -s "$SERVER_URL")

# Extract the download URL using jq
item=$(echo "$response" | jq -r .assigned_item)

# Ensure a valid URL was received
if [[ "$item" == "null" || -z "$item" ]]; then
    echo "No valid item received from server."
    exit 1
fi

echo "Received item: $item"

# Extract the filename from the URL
filename=$(basename "$item")

# Download the file
if curl -L -O "$item"; then
    echo "Downloaded: $filename"
else
    echo "Download failed!"
    exit 1
fi

# Ensure a valid ZIP file was downloaded
if [ ! -f "$filename" ]; then
    echo "No ZIP file found after download."
    exit 1
fi

echo "Downloaded ZIP file: $filename"

# Extract the ZIP file
UNZIPPED_FOLDER="${filename%.zip}"  # Strip .zip extension
mkdir -p "$UNZIPPED_FOLDER"
unzip -o "$filename" -d "$UNZIPPED_FOLDER"

# Save the extracted folder path for the Python script
echo "$UNZIPPED_FOLDER" > chrome_profile_path.txt

echo "Extraction complete. Chrome profile is in: $UNZIPPED_FOLDER"
