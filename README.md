Coursework Analysis

I decided to build a video game as my coursework assignment. The purpose of this project was to sharpen my Python skills and teach me how to utilize the "Pygame" Python module, which is intended for creating video games. I made the decision to create a platformer-style video game using this module. The popular TV show "Braking Bad" is the basis for the game. This is the reason the game is called "Walt's adventure," as the show's lead character shares the same name. Any IDE (pycharm, visual code, etc.) that supports Python can be used to run the game. The start button is one of two buttons that appear when you run the code, making the game simple to use. Press the start button and enjoy this masterpiece.

All four pillars of object-oriented programming are implemented in the program. Line 195 made use of inheritance. The built-in Pygame class "sprite.Sprite" was utilized to create the Enemy class. The "sprite.Sprite" built-in class serves as the basis for making game objects. It serves as a basic class from which you may inherit and construct any visual element in your game, including backdrops, objects, and characters.  I have also utilized overriding, a polymorphism, because this class is meant to be overwritten. I've utilized encapsulation in the Button class that is located on line 44.  This class's methods are the only ways to access and modify its characteristics; none of them are directly available from outside the class. I have also utilized abstraction in my code because it is one of the fundamental tenets of object-oriented programming. Parts of the code that are not important are hidden via abstraction. It is in line 212 of my code, which is where the Exit class is found. The details of what an exit is (an image at a given position) are contained in the Exit class. The rest of the application only needs to build an Exit object at the specified place; it doesn't need to know these details.

After going over each of the "OPP" pillars, let's move on to the remaining assignment that needs to be completed. My code complies with the coursework requirement of having at least two design patterns. In my code, I've employed the decorator and singleton design patterns. There is a Decorator design pattern at line 29. This design pattern was created for the Button class. Additional methods are added to the Button class using this Decorator class. I have used Singleton in line 57, which is where the Player class is located. This design pattern makes it so only one object of the Player class can be created. Reading from and writing to the file was one additional task that needed to be completed. Data containing the game's level is read from the file. The information is written as a matrix, or more accurately, as a list within a list. What kind of object should appear in the game is represented by each digit in this matrix. The date when a player ends their game session is written to the file. The "X" button in the window's corner is not tracked; it only functions when the player hits the quit button on the screen.

There were numerous challenges I had to overcome when building this code. I needed help using "pygame," so I turned to YouTube tutorials for guidance. I discovered that my code was having trouble understanding that the data in the file was a list. It wasn't until the following day that I realized the code most likely reads the data as a string rather than a list. This discovery led me to fix the code. Further stages and new enemy types could be added to the code in the future. Having covered every facet of the code and the problems I encountered while developing it, I can conclude that my coursework was successful in its goal of enhancing my abilities because it forced me to pick up a lot of new knowledge and solidify what I had learned in lab assignments and lectures.