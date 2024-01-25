
--------------------------Copy and Auto Shutdown Script--------------------------


Description
This Python script, packaged as a Windows 10 executable named copy-shutdown.exe, provides a convenient and user-friendly way to copy files from an external storage device to a PC, and then automatically shuts down the computer after a predetermined time interval. This tool now includes a Graphical User Interface (GUI), enhancing ease of use and interaction.

Prerequisites
Operating System: Designed specifically for Windows 10.
Administrator Privileges: The executable must be run with administrator privileges to enable system shutdown functionality.

Initial Setup
Download the Executable: Download the copy-shutdown.exe file to your Windows 10 computer.

Script Execution
Open the Executable: Double-click on copy-shutdown.exe to start the program.
Using the Graphical Interface: The GUI will guide you to select a USB/CD device and a destination folder for copying the files.

Copy and Shutdown Process:
Select the source (external storage) and destination (folder on your PC) for copying files.
Confirm the file copying operation in the GUI.
After the file transfer, the PC will display a countdown and shut down automatically after 10 seconds (or a specified interval).

Features
User-Friendly Interface: A simple and intuitive GUI for all operations.
Selective Copying: Users can choose specific files or folders for copying.
Automatic Shutdown: The PC will shut down automatically, making it convenient for backup operations before leaving the computer.

Additional Notes
Data Security: Be cautious with the files you choose to copy. Ensure they do not contain sensitive or confidential information, as the program does not filter file types.
Script Testing: Test the executable in a controlled environment to verify its functionality.
Emergency Stop: If you need to halt the shutdown process after initiating, there is an option within the GUI to cancel the shutdown.

Technical Details
-Language: Python
-External Libraries: Tkinter for GUI, os and shutil for file operations
-Executable Creation: The script is converted into an executable using PyInstaller, a Python file manager, ensuring compatibility and ease of distribution for Windows 10 systems.