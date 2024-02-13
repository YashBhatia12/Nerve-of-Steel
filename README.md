#This is the nerve of steel game, where players stand up and then after a certain random time set by the computer, players have a seat, last to sit down wins

Libraries used/Required
Time --> library used for 'sleeping' the script 
PIL import ImageTk --> this is used to display images form the Plilow library
Random --> used to gnerate the random time that the program sleeps for 
Tkinter --> Creates a GUI so we can display our image
Urllib.request import urlopen --> reads Image URLs

What's _def__timesUp()_?
This function prints out a message indicating that times Up and then display the image in a TKinter (GUI) window
It reads an imageURL from the web, this way anyone can use the code withut having to add the image to their Laptop and modifying the code to search for the file

The Main Program:
Tells users when to stand up 
Generates a random time interval (in seconds) using 'rd.randint()' and pauses the script execution for that amount of time using 'time.sleep()'
Calls the 'timesUP()' function when the timer runs out

Notes:
The ImageURL can be replaced to any imageURL on the web with a valid URL, think of it as a placeholder

To learn more about the libraries:

Tkinter: https://camo.githubusercontent.com/333875621ea27c95dd039e480184dbead1c93e095f94582c44e10231472a6a4a/68747470733a2f2f6d656469612e6d616b65616d656d652e6f72672f637265617465642f74696d65732d75702d3539323365302e6a7067

Urllib: https://docs.python.org/3/library/urllib.html

