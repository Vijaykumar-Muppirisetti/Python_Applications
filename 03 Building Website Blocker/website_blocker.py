# Import the necessary modules
import time
from datetime import datetime as dt

# Define the temporary host file and the actual host file path
host_temp = "hosts"
host_path = "C:\Windows\System32\drivers\etc\hosts"
# For Mac and Linux host PATH: /etc/hosts

# Define the redirect IP address
redirect = "127.0.0.1"

# Define the list of websites to block
website_list = ["www.facebook.com", "facebook.com", "www.youtube.com"]

# Run the script in an infinite loop
while True:
    # Check the current time is within working hours (8am - 4pm)
    if (
        dt(dt.now().year, dt.now().month, dt.now().day, 8)
        < dt.now()
        < dt(dt.now().year, dt.now().month, dt.now().day, 16)
    ):
        # Print a message indicating that it's working hours
        print("Working hours...")

        # Open the host file in read and write mode
        with open(host_path, "r+") as file:
            # Read the content of the file
            content = file.read()

            # Iterate over the list of websites to block
            for website in website_list:
                # Check if the website is already in the file
                if website in content:
                    # If it is, doing nothing
                    pass
                else:
                    # If it's not, add the website to the file
                    file.write(redirect + " " + website + "\n")
    else:
        # Open the host file in read and write mode
        with open(host_path, "r+") as file:
            # Read the content of the file
            content = file.readlines()

            # Move the file pointer to the beginning of the file
            file.seek(0)

            # Iterate over the lines in the file
            for line in content:
                # Check if any of the websites to block are in the line
                if not any(website in line for website in website_list):
                    # If not, write the line to the file
                    file.write(line)

            # Truncate the file to remove any remaining content
            file.truncate()

        # Print a message indicating that it's fun hours
        print("Fun hours...")

    # Pause the script for 5 seconds
    time.sleep(5)


# Description: This script will block websites for a specified period of time (Working Hours) in a day.
# Author: @vijaykumar.muppirisetti
# Date: 2024-08-25
# Version: 1.0
