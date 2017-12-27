__author__      = "Arunangshu Chatterjee"

import os
import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"                     # raw string containing the hosts file path
hosts_bkp = r"C:\Windows\System32\drivers\etc\hosts_backup"               # raw string containing the hosts_backup file path
redirect = "127.0.0.1"                                                    # Distracting websites will be routed here
website_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com", "www.linkedin.com", "linkedin.com"]

# Create a backup of the hosts file if none exists:
if not os.path.isfile(hosts_bkp):
    infile = open(hosts_path,'r')                                         # Open hosts file in read mode
    content = infile.read()                                               # Read and store the contents of the file
    infile.close()                                                        # Close the hosts file
    outfile = open(hosts_bkp,'w')                                         # Open or create the output backup file
    for line in content:                                                  # Iterate through the contents of the file
        outfile.write(line)                                               # Write the output to the file line by line
    outfile.close()                                                       # Close the hosts_backup file

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):       # If current time is between 8 am to 5 pm
		file = open(hosts_path,'r+')                                	  # Open hosts file
		content = file.read()                                             # Read and store the contents of the file
		for website in website_list:                                      # For every website in the website_list do
			if website in content:                                        # Check if the website exists in the file
				pass                                                      # If True, Do nothing
			else:                                                         # else, the website doesn't exist in the file
				file.write("\n" + redirect + "     " + website + "\n")    # Add the website along with proper formatting in the hosts file
	else:                                                                 # Else, the current time is not between 8 am to 5 pm
		file = open(hosts_path,'r+')                                      # Open the hosts file in read write mode
		content = file.readlines()                                        # Reads the lines and stores them as a list. File pointer is at the end of the file.
		file.seek(0)                                                      # To append new lines at the beginning of the file, move the cursor to the beginning of file.
		for line in content:                                              # For every line in the file do
			if not any(website in line for website in website_list):      # Check if the line contains website from website_list 
				file.write(line)                                          # If True, Add existing content from list excluding the website_list URLs
			file.truncate()                                               # Delete everything from the current file position that used to be the previous content for the file		
	file.close()
	time.sleep(60)