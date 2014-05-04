##############################
#                            #
# NewEgg Daily Deals Checker #
# Created by: Rishi Goomar   #
#                            #
##############################
import sys
import subprocess
from googlevoice import Voice

# Check if both arguments are given
if len(sys.argv) > 2:
	# Get the command line arguments for what they want to search for and the phone number to send a text to
	search_string = sys.argv[1]
	phone_number = sys.argv[2]
# Otherwise, ask them.
else:
	search_string = input("What do you want to find?")
	phone_number = input("Where would you like the text to go to?")
# Check for emptys and exit 
if (search_string == ""):
	print ("Enter a search string!")
	sys.exit()
if (phone_number == ""):
	print ("Enter in a phone number!")
	sys.exit()

print ("Getting deals")

# Run the script in another process and check for the search string
items_found = subprocess.Popen('python NewEggDailyDeals.py | grep "' + search_string + '"', shell=True, stdout=subprocess.PIPE)
item_found = items_found.stdout.read().strip()
print (item_found)

# Nothing found. :(
if (items_found == ""):
	print ("No deals found")
	sys.exit()

# We found a deal!
print ("Deal was found! Sending message...")
# Initialize the Google Voice object
voice = Voice()
#voice.login()
voice.login("username","password")
# Send the message to the number
voice.send_sms(phone_number,"A deal has been found! Search string used: ",search_string)
# Show which number it was sent to
print "Message sent to " + str(phone_number)

