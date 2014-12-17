# Matter.py

Matter.py is an underwater-themed educational game targeted towards 4th grade students interested 
in learning about different states of matter and their behaviors. It was built originally with the
XOPC from the One Laptop Per Child program in mind.

# License

The MIT License

# Dependencies

Python (2.8.7)
Pygame (1.9.1)

Code was loosely started using the Sugar quickstart (https://github.com/FOSSRIT/sugar-quickstart), 
however that aspect of it is slightly broken currently. Sprite drawing (although currently broken as well) is based on
this spritesheet iterator (http://www.pygame.org/wiki/Spritesheet?parent=CookBook),

# Building & Running

For now, the game opens from command line, by running Matter.py. Switch to the correct directory and run "python matter.py".
Python must be installed on the target machine, with Pygame as well.

In the event they are not installed, you can get them here:
https://www.python.org/downloads/
http://www.pygame.org/download.shtml

-XO build process here-

# Controls

Your mouse speed changes type of matter. No motion causes the piece of matter to become a solid and cause the matter to fall. 
Moving the mouse slowly with form a liquid, and moving it even faster will create a gas, which will effectively rise to the 
top of the screen.

#Sugar Wiki

http://wiki.sugarlabs.org/go/Matter.py