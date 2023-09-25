This repository contains an implementation of Connect 4 utilizing the Monte Carlo Tree Search (MCTS) algorithm. This algorithm intelligently evaluates possible moves by simulating random games and strategically building a game tree based on the results.

How It Works
The MCTS algorithm takes the current state of the Connect 4 game. For each possible move, it simulates the game until a terminal state (game end) is reached. Using the outcome of these simulations (win, loss, or draw), the algorithm constructs the game tree, storing statistics about the favorability of each position at every node.

When transitioning from the root of the tree to a specific node, the algorithm employs the Upper Confidence Bound (UCB) approach. This allows for the exploration of unseen positions and moves while also favoring moves that have proven successful in prior simulations.

Files
mcts.py: Contains the implementation of the Monte Carlo Tree Search algorithm.
play.py: Allows you to run the program on the paper games website .
grid.png: Required for OpenCV to identify the location of Connect 4 pieces on the website.

Dependencies
keyboard: This library provides functions to listen for and send keyboard events. It allows your program to interact with the keyboard.

pyautogui: This library enables you to programmatically control the mouse and keyboard. It's particularly useful for automating tasks that involve GUI interactions.

mouse: This library is used for capturing and simulating mouse events. It allows your program to interact with the mouse.

time: This is a standard Python library for handling time-related operations. It's used for functions like time.sleep() to introduce delays in your program.

webbrowser: This library provides a high-level interface to display web-based documents to users. In your code, it's likely used to open a web browser to interact with a Connect 4 game.

connect4: This seems to be a custom module or class for handling the Connect 4 game logic. This is likely a part of your project, and you might have implemented it yourself.

mcts: This seems to be another custom module or class that implements the Monte Carlo Tree Search (MCTS) algorithm for your Connect 4 game.

Acknowledgments
Monte Carlo Tree Search explanation:https://www.cs.swarthmore.edu/~mitchell/classes/cs63/f20/reading/mcts.html
reference video : https://www.youtube.com/watch?v=XRVA5PMSKKE
