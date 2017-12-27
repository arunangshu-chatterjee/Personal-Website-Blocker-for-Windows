# Personal-Website-Blocker-for-Windows
This program helps you block certain websites during work hours to enhance productivity

### Word of Caution:
Please take a backup of your hosts file present at: C:\Windows\System32\drivers\etc\hosts
Even if you forget to do that don't worry, I've got you covered. 
There will be a file hosts_backup created in the same directory. 
If for some reason, the original hosts file gets corrupt, you can replace it with the hosts_backup file by deleting the corrupt hosts file and renaming the hosts_backup file as hosts.

### Scheduling the python program to run on Windows:
To run python as a background process on Windows, you would need pythonw.exe.

This file will be present in the Scripts folder in the python installation directory where python.exe is present.

So we change the file extension as .pyw instead of .py.

To run the file: open command prompt as administrator and run the website_blocker.pyw file.

You can see it running in the task manager.

### To automate this process, you can schedule a task as follows:
Go to Task Manager -> Under Actions, Create Task ->

In the General Section -> Name: Website Blocker, Check run with highest privileges, Configure for: Select the Windows version that you are using.

In the Trigger Section -> Click New -> Begin the task: At Startup.

In the Actions Section -> Click New -> Start a program -> Program/Script: The location of the website_blocker.pyw file -> Click Ok.

In the Conditions Section -> Uncheck the power option

Click Ok
