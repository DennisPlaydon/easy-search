## easy-earch
Easy Search is a simple script to make everyday searching easier. It allows you to use the command line to search google, youtube, maps and find the weather.

## Gettings started
To use this program you will have to clone the repository
```
git clone https://github.com/DennisPlaydon/easySearch.git
```
## Running
Before you can run easy search you will have to open the search.bat file into a text editor
Currently the bash script is looking for the easySearch python file in:
```
C:\MyPythonScripts\
```
Replace this path with the path of the easySearch.py file.
```
@py.exe pathWhereFileIsInstalled\easySearch.py %*
@pause
```
To execute the program open the command prompt and type one of the five commands or type search to show all commands 
*You will need to cd into the file where the batch file is store in order to run from the cmd prompt*
```
search go google search
search yt youtube search
search weather
search map address
```

## Debugging possible issues
Sometimes pyperclip will not be installed. Type the command below to install it
```
pip intall pyperclip
```

## Customising
You can add your own functionality by editing parts of the python dictionary

## Author
* **Dennis Playdon**

## Acknowledgments
* Inspired by Al Sweigart's *Automate the Boring Stuff*
