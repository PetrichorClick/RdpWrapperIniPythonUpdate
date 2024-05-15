import os
import sys
import ctypes
import requests
from pathlib import Path

def is_admin():
    """
    Check if the script is running with administrative privileges.
    Returns True if it is, otherwise False.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def download_file(url, save_path):
    """
    Download the file from the specified URL and save it to the given path.
    
    Parameters:
    url (str): The URL of the file to download.
    save_path (Path): The path where the file will be saved.
    """
    # Fetch the content from the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Open the file in write-binary mode and write the content
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded and saved to {save_path}")
    else:
        # Print an error message if the request failed
        print(f"Failed to download file. Status code: {response.status_code}")

def main():
    """
    Main function to handle the downloading of the file.
    """
    # URL of the file to be downloaded
    url = "https://raw.githubusercontent.com/affinityv/INI-RDPWRAP/master/rdpwrap.ini"

    # Local path where the file will be saved
    save_path = Path(r"C:\Program Files\RDP Wrapper\rdpwrap.ini")

    # Download the file
    download_file(url, save_path)

if __name__ == "__main__":
    # Check if the script is running with administrative privileges
    if is_admin():
        # If running as admin, proceed with the main function
        main()
    else:
        # If not running as admin, re-run the script with elevated privileges
        script = os.path.abspath(sys.argv[0])  # Get the absolute path of the script
        params = ' '.join([script] + sys.argv[1:])  # Prepare the script parameters
        # Request to run the script with administrative privileges
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
