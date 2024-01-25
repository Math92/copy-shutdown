# Copy and Auto Shutdown Script

## Description
This Windows executable, `copy-shutdown.exe`, detects the insertion of a USB device, copies specific files from that device to the PC, and then automatically shuts down the computer. It is built for Windows 10 systems and does not require Python to be installed, as it is a standalone executable.

## Prerequisites
- **Windows 10 System:** The executable is designed to run on Windows 10.
- **Administrator Privileges:** To enable the script to shut down your system, it must be run with administrator privileges.

## Initial Setup
1. **Download the Executable:** Download `copy-shutdown.exe` to your computer.
2. **No Installation Required:** Since it's an executable file, no additional installation or setup is needed.

## Execution
1. **Run as Administrator:**
   - Right-click on `copy-shutdown.exe` and select "Run as administrator."
2. **Follow the On-screen Instructions:**
   - The executable will guide you through selecting the USB/CD device path for copying files.
3. **Completion:**
   - After the files are copied, the executable will wait for a predefined duration (default is 10 seconds) before shutting down the computer.

## Additional Notes
- **Data Security:** Be cautious with the files you choose to copy. Ensure they do not contain sensitive or confidential information.
- **Testing:** It is advisable to test the executable in a safe environment to ensure it functions as expected.
- **Emergency Stop:** If you need to halt the shutdown process initiated by the script, you can cancel it by running 'shutdown -a' in a command window.
