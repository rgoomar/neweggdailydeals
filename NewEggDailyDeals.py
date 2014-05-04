#############################
#                           #
# NewEgg Daily Deals Lister #
# Created by: Rishi Goomar  #
#                           #
#############################
from bs4 import BeautifulSoup
import urllib
import re

# Get to the deals list
newegg = BeautifulSoup(urllib.urlopen("http://www.newegg.com/Product/ProductList.aspx?Submit=DailyDeals&IsNodeId=1&bop=And&Order=PRICED&LayoutView=list&PageSize=100"))

price = []
title = []
price_before = []

# Grab all the titles
for deal in newegg.find_all(class_=re.compile("itemDescription")):
	# Some of them don't have a specific id and others have 2 of them. So, manipulate to get only one title
	# for each item
	if (deal.has_attr('id')):
		newdeal = re.compile("titleDescription").search(deal['id'])
		# Remove the extra title name so you don't get duplicate listings
		if (newdeal):
			del newdeal
		else:
			title.append(deal.string)
	else:
		title.append(deal.text)
# Get all of the current prices. Some have a "see in cart", so the price may not be listed
for item_price in newegg.find_all("li", re.compile("price-current")):
	if (item_price.strong):
		price.append("$" + item_price.strong.get_text() + item_price.sup.get_text())
	else:
		price.append("No Price Listed")

# Get the original price before the sale
for item_price_before in newegg.find_all("span", re.compile("price-was-data")):
    price_before.append(item_price_before.text)

print ("Price Now" + "\t Price Was" + "\t\t\t\t\t" + "Item")

# Loop through the items and list them out in a sort-of table
for i in range(len(title)):
    print (price[i] + "\t" + price_before[i] + "\t" + title[i])