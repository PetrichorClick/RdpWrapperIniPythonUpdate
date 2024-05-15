# RdpWrapperIniPythonUpdate
A Python script to update RdpWrap.ini file from the git hub repositry, this will run as admin using powershell.

Script Breakdown
* is_admin(): This function checks if the script is running with administrative privileges using ctypes.windll.shell32.IsUserAnAdmin().
* download_file(url, save_path): This function downloads the file from the specified URL and saves it to the given path.
  * It sends a GET request to the URL.
  * If the request is successful (status code 200), it writes the content to the specified file path.
  * If the request fails, it prints an error message with the status code.
* main(): This is the main function where the URL and save path are defined, and the download_file function is called.
* if name == "main":: This block checks if the script is being run directly (not imported). If not running as admin, it re-runs the script with elevated privileges.
