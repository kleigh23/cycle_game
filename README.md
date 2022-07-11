# Cycle
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them. Think of a multiplayer version of the old Snake game. If this doesn't go to #1 on Twitch then I don't know what will!

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.

```
python3 cycle 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- cycle               (source code for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (general values that are referenced through the classes)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Kelley Robertson (creator of repository, figured out how to add the second player, master of red colored snakes!)
* Shanny López (Made the snakes grows over time, added food so the score increase if one snake hits it)
* Cristian Avendaño (Fixed frame rate and other details, is scared of snakes...)
