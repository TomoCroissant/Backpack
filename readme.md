# Team Crab

Ian Turner: Product Manager

Tomo Sato: Developer

Henry Miller: UX/UI Designer 

Reid Nguyen: Multimedia and Tester


## Alptraum von James

Class Diagram

![ClassDiagram](https://github.com/TomoCroissant/Crab/blob/main/Images/UML.png?raw=true)

Made by Tomo Sato

Active Gameplay

![ActiveGameplay](https://github.com/TomoCroissant/Crab/blob/main/Images/frontierScreenshot.png?raw=true)

Made by all

# Instructions for running the program

In Terminal type:

  pip3 install pygame
  
Then open the .zip file containing the game. Search for main.py and run the file.

# Update History

* Basic skeleton created by making classes and functions from class diagram.
* Player was drawn to screen with WASD controls.
* Inventory and Item classes removed.
* Basic save logic was created by writing to a .txt file and then retrieving data from that file when designated key pressed.
* Basic room logic created to record and display the current room (background).
* Bullet class created.
* Bullet logic created using vectors.
* Bullet drawn and animated to screen whenever the mouse was clicked.
* Room class removed.
* Bullet converted to a boomerang by inverting vectors once bullet reached desired position.
* Bullet limited by waiting until the boomerang returned to the player before shooting again.
* Sprites of characters, objects, and maps drawn to screen.
* Project broke because Replit no longer runs pygame on our devices.
* Replit came back to life.
* Hitboxes and collision detection created for player, NPC, and bullet
* Created and implemented room and sprite art
* Implemented score and file saving systems
