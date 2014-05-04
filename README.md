# NewEgg Daily Deal Finder


## Initial Setup Instructions
1. Install Beautfiul Soup 4 for Python using Pip
```
pip install beautifulsoup4
```
2. Install the Google Voice Python Library
Download this:
[pygooglevoice](https://bwpayne-pygooglevoice-auth-fix.googlecode.com/archive/56f4aaf3b1804977205076861e19ef79359bd7dd.zip)

And extract the contents of the archive and run:
```
python setup.py install
```

### List all daily deals from NewEgg
```
python NewEggDailyDeals.py
```

### Search for a keyword to see if it's in the deals list
Search with arguments in command line:
```
python checkforDeals.py [keyword] [phone number]
``` 
OR be prompted for it
```
python checkforDeals.py
```