#! python3
# easySearch.py - Launches a search in the browser using an address from the
# command line

import webbrowser, sys, pyperclip

website = 0
def type(x):
    x = x.lower()
    return {
        'go': 1,
        'yt': 2,
        'weather': 3,
        'map': 4,
        'news': 5
    }.get(x, 0)

if len(sys.argv) > 1:
    # Get address from command line.
    website = type(sys.argv[1])
    address = ' '.join(sys.argv[2:])

if website != 0:
    if website == 1:
        webbrowser.open("https://www.google.com.tr/search?q={}".format(address))
    elif website == 2:
        webbrowser.open("https://www.youtube.com/results?search_query={}".format(address))
    elif website == 3:
        webbrowser.open("https://weather.com")
    elif website == 4:
        webbrowser.open('https://www.google.com/maps/place/' + address)
    elif website == 5:
        webbrowser.open("https://www.reuters.com/")
        webbrowser.open("https://www.bloomberg.com/asia")
        webbrowser.open("https://www.forbes.com")
        webbrowser.open("http://fortune.com/")
        webbrowser.open("https://www.wsj.com/asia")
else:
    print("Valid commands are: \nsearch go\nsearch yt\nsearch weather\n search map\n search news")
        
