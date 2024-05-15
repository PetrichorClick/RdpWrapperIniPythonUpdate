import os
import sys
import ctypes
import requests
from pathlib import Path

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def download_file(url, save_path):
    # Fetch the content from the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Write the content to the specified file path
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded and saved to {save_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

def main():
    # URL of the file to be downloaded
    url = "https://raw.githubusercontent.com/affinityv/INI-RDPWRAP/master/rdpwrap.ini"

    # Local path where the file will be saved
    save_path = Path(r"C:\Program Files\RDP Wrapper\rdpwrap.ini")

    # Download the file
    download_file(url, save_path)

if __name__ == "__main__":
    if is_admin():
        main()
    else:
        # Re-run the script with admin privileges
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:])
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
