# RdpWrapperIniPythonUpdate
A Python script to update RdpWrap.ini file from the git hub repositry, this will run as admin using powershell.

<b>Script Breakdown</b>
* <b>is_admin():</b> This function checks if the script is running with administrative privileges using ctypes.windll.shell32.IsUserAnAdmin().
* <b>download_file(url, save_path):</b> This function downloads the file from the specified URL and saves it to the given path.
  * It sends a GET request to the URL.
  * If the request is successful (status code 200), it writes the content to the specified file path.
  * If the request fails, it prints an error message with the status code.
* <b>main():</b> This is the main function where the URL and save path are defined, and the download_file function is called.
* <b>if name == "main":</b> This block checks if the script is being run directly (not imported). If not running as admin, it re-runs the script with elevated privileges.


<b>Required Additional Imports</b>
1) <b>Requests</b><br>
   Install requests Library: This script uses the requests library to download the file. You can install it using pip:

   <code>pip install requests</code>
