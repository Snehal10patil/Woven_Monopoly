# Woven_Monopoly

Woven Monopoly Game

The Woven Monopoly game simulator is a command-line application that simulates a game of Monopoly with predefined dice rolls. 
The game follows specific rules, including:
1.Four players take turns in a fixed order.
2.Players start with $16 and must buy properties they land on.
3.Rent is paid if a player lands on an owned property.
4.If a player owns all properties of the same color, rent is doubled.
5.The game ends when a player goes bankrupt, and the winner is the player with the most money.
6.The application loads the game board and dice rolls from JSON files, simulates the game, and outputs the results.

Features
Modular Code: The code is organized into separate files for players, the board, and the game logic.
JSON Support: The game board and dice rolls are loaded from JSON files.
Deterministic Simulation: The game is simulated using predefined dice rolls, ensuring reproducibility.
Extensible Design: The code is designed to be easily extended with new features (e.g., chance cards, stations).

Project Structure

woven_monopoly/

 board.py            # Contains the Board class
 player.py           # Contains the Player class
 game.py             # Contains the Game class and game logic 
 main.py             # Main script to load data and run the game
 board.json          # JSON file defining the game board
 rolls1.json         # JSON file containing the first set of dice rolls
 rolls2.json         # JSON file containing the second set of dice rolls
 README.md           # Project documentation
 
Setup Instructions
Python 3.7 or higher.
Link to download the python(Consider downloading the latest version)
https://www.python.org/
The json module (included in Python's standard library).

Pycharm
Pycharm editor also can be used for this program(Consider downloading the latest version)
https://pycharm-community-edition.en.softonic.com/

Steps
 1.Clone the repository or download the project files.
 2.Navigate to the project directory:
Ensure the following files are present in the directory:
    1.board.json 
    2.rolls_1.json
    3.rolls_2.json

Running the Code
  For Command Prompt
        1.On command prompt cd (path for woven directory) for eg.C:\Users\sneha\woven
        2.then type - python main.py
  For PyCharm
        1.In PyCharm editor copy all files under PycharmProjects\pythonProject\ woven
        2.Open the main.py file in the editor.
        3.Right-click anywhere in the editor and select Run 'main'.

Output will look like this
Results for combined rolls:
Peter ends with $45 on YOMG
Billy ends with $6 on YOMG
Charlotte ends with $0 on Gami Chicken
Sweedal ends with $0 on Gami Chicken
The winner is Peter

Testing
The code includes basic functionality for simulating the game. To test the code:
Unit Tests: Write unit tests for individual components (e.g., Player, Board, Game) using a testing framework like unittest or pytest.
Edge Cases: Test edge cases, such as:
A player landing on the same property multiple times.
A player going bankrupt.]
All properties of a color being owned by one player.
Manual Testing: Run the script with different dice rolls and verify the results.

Design Decisions
Modularity
The code is divided into separate files (player.py, board.py, game.py) to ensure modularity and reusability. Each class has a single responsibility, making the code easier to maintain and extend.

Game Logic
The Game class handles the core game logic, including player turns, property transactions, and rent calculation. The logic is designed to be deterministic, ensuring consistent results for the same input.

Extensibility
The code is designed to be extensible. For example:
New types of spaces (e.g., chance cards, stations) can be added by extending the Space class.
Additional rules (e.g., jail, auctions) can be implemented by modifying the Game class.

Future Improvements
Add More Features:
    Implement chance cards, stations, and jail.
    Add support for auctions when a player cannot afford to buy a property.

Improve Testing:
    Add unit tests for all classes and methods.
    Use a testing framework like pytest for better test organization.

User Interface:
    Create a graphical user interface (GUI) using a library like tkinter or PyQt.

Performance Optimization:
    Optimize the game logic for large datasets (e.g., thousands of dice rolls).

Error Handling:
    Add error handling for invalid JSON files or unexpected input.

