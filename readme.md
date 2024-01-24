=====Copy and Auto Shutdown Script=====

//
Description
This Python script detects the insertion of a USB device, copies specific files from that device to the PC, and then automatically shuts down the computer.

Previous requirements
Python: It must be installed on your Windows 10 system. You can download it from https://www.python.org/downloads/release/python-3121/
Choose the version according to your system (Windows installer (32-bit), Windows installer (64-bit), Windows install (ARM64))


Administrator Privileges: In order for the script to shutdown your system, it needs to be run with administrator privileges.

Initial setup
Download the Script: Download the shutdown.py script to your computer.

Modify the Destination Directory (Optional): If you want to change the directory where the files will be copied, edit the destination_directory variable in the script.


//
Script Execution
Open Command Prompt with Administrator Privileges:

-Find "cmd" in the start menu, right-click "Command Prompt" and select "Run as administrator".
Navigate to the Script Directory:

-Use the cd command to change to the directory where you saved shutdown.py.
For example: 'cd C:\Users\YourName\Downloads'
Run the Script:

-Run the script with the command from the root folder: 'python3 shutdown.py' or 'python3 shutdown.py'
Follow the on-screen instructions to enter the USB/CD device path.
Ending:

-After copying the files, the script will wait 10 seconds (or however long you have set) and then shut down the computer.
Additional notes


//
Data Security: Make sure that the files you want to copy do not contain sensitive or confidential information, since the script does not discriminate file type.
Testing the Script: It is advisable to first test the script in a safe environment to ensure that it works as expected.


//
Emergency Stop: If you need to stop the shutdown after running the script, you can cancel it by running 'shutdown -a' in a command window.










                                                                             --Mathias Santos