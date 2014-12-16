import pygame.display, pygame.time, pygame.event, pygame.rect, math, sys
from itertools import ifilter
from random import randint
from player import Player
from boundary import Boundary
from object import Object


class MatterGame:

        def __init__(self):
                #self.screen = pygame.display.set_mode((1024, 768))
                self.screen = pygame.display.get_surface()
                self.clock = pygame.time.Clock()
#                self.camera_translation = 0
#                self.spawn_rate = 300
#                self.score = 0
                self.score_check = False #prevent double obstacles from giving 2 points
#                self.spawn_timer = 0
#                self.player = Player(self.screen.get_width() / 2, self.screen.get_height() / 2, 'solid')
#                self.objects = []
#                self.objects.append(self.player)
#                _floor = Boundary(-2 * self.screen.get_width(), self.screen.get_height(), 4 * self.screen.get_width(), 100)
#                _ceiling = Boundary(-2 * self.screen.get_width(), -100, 4 * self.screen.get_width(), 100)
#                self.objects.append(_floor)
#                self.objects.append(_ceiling)

                self.init_game()

                self.running = 1
                self.game_running = 0
                self.add_random_obstacle()
                self.paused = False

        def init_game(self):
                self.camera_translation = 0
                self.spawn_rate = 300
                self.score = 0
                self.score_check = False #prevent double obstacles from giving 2 points
                self.spawn_timer = 0
                self.player = Player(self.screen.get_width() / 2, self.screen.get_height() / 2, 'solid')
                self.objects = []
                self.objects.append(self.player)
                _floor = Boundary(-2 * self.screen.get_width(), self.screen.get_height(), 4 * self.screen.get_width(), 100)
                _ceiling = Boundary(-2 * self.screen.get_width(), -100, 4 * self.screen.get_width(), 100)
                self.objects.append(_floor)
                self.objects.append(_ceiling)


        #Adds a random obstacle to self.obstacles
        def add_random_obstacle(self):
                #Select random allowed state for obstacle
                _rnd_state_index = randint(0, 3)
                if(_rnd_state_index == 0): 
                        #Set state
                        _rnd_state = 'solid'
                        #Create obstacle
                        self.objects.append(Object(self.screen.get_width() + self.camera_translation, 0, 200, self.screen.get_height() - 300))
                elif(_rnd_state_index == 1):
                        #Set state
                        _rnd_state = 'liquid'
                        #Create obstacle
                        self.objects.append(Object(self.screen.get_width() + self.camera_translation, 0, 200, self.screen.get_height() / 2 - 150))
                        self.objects.append(Object(self.screen.get_width() + self.camera_translation, self.screen.get_height() / 2 + 150, 200, self.screen.get_height() / 2 - 150))
                        
                else: 
                        #Set state
                        _rnd_state = 'gas'
                        #Create obstacle
                        self.objects.append(Object(self.screen.get_width() + self.camera_translation, 300, 200, self.screen.get_height() - 300))

        #Runs the game
        def run(self):
                while self.running:                     #Start the game loop
                        self.clock.tick(30)             #Allow game to run at a maximum of 30 loops per second
                        
                       

                        #if the game is running
                        if self.game_running:                           #Game Update
                                #Input management
                                for event in pygame.event.get():
                                        #Keyboard                                       
                                        if hasattr(event, 'key'):
                                                if event.key == pygame.K_ESCAPE: self.game_running = 0

                                #Update game logic
                                #Spawn obstacles
                                self.spawn_timer += 1
                                if(self.spawn_timer >= self.spawn_rate):
                                        self.spawn_timer = 0
                                        self.add_random_obstacle()
        
                                #Just in case the player goes off the top of the screen
                                if(self.player.position[1] < 1):
                                        self.player.position[1] = 1

                                #Apply global forces to player
                                self.player.velocity[1] += 0.1          #Gravity

                                #Update objects
                                for _object in self.objects:
                                        _object.update()
                                        #Collision detection for player
                                        if(self.player.is_colliding(_object)):
                                                #If player is colliding with something, set player
                                                #Back to previous position
                                                _colliding_side = self.player.get_colliding_side(_object)
                                                self.player.resolve_collision(_colliding_side)


                                #Screen bounds check
                                self.objects[:] = ifilter(lambda e: self.is_on_screen(e), self.objects)
                                if(self.player not in self.objects):
                                        print("Game over")
                                        self.game_running = 0

                                #bool check from off the screen method to prevent double score incrementation
                                if(self.score_check):
                                        self.score += 1
                                        self.score_check = False

                                # Set up score and clear space so score doesn't overlap itself
                                font = pygame.font.Font(None, 36)
                                text = font.render("SCORE: "+str(self.score), 1, (255, 255, 255))
                                textpos = text.get_rect()
                                textpos.center = (100,100)
                                #self.screen.fill(pygame.Color("black"), (20, 50, 200, 100)) # erase a rectangle behind the text(x,y,width,height)
                                instruct = font.render("Move mouse quickly to go up", 1, (255, 255, 255))
                                instruct2 = font.render("Release mouse to descend", 1, (255,255,255))
                        

                                #Draw Code
				#Refresh screen above water
				self.screen.fill(pygame.Color("black"), (0, 0, self.screen.get_width(), 168))

                                for _object in self.objects:
                                        _object.draw(self.screen, self.camera_translation)

                                # display score in front of other objects
                                self.screen.blit(text, textpos)
                                if(self.score < 3):
                                        self.screen.blit(instruct, (10,180))
                                        self.screen.blit(instruct2, (10,210))
                                

                                #Create transparent surface
                                _alpha_surface = pygame.Surface((self.screen.get_width(), 600))
                                _alpha_surface.set_alpha(100)
                                _alpha_surface.fill((0, 0, 255))
                                self.screen.blit(_alpha_surface, (0, 168))

                                pygame.display.update()                 #Update display

                                #Slide camera
                                self.camera_translation += 3
                        else:                                   #Menu update
                                bounds = pygame.Rect((495, 400),(100,100))
                                titleFont = pygame.font.SysFont("Arial", 60)
                                startFont = pygame.font.SysFont("Arial", 30)

                                #Input management
                                for event in pygame.event.get():
                                        #Keyboard                                       
                                        if hasattr(event, 'key'):
                                                if event.key == pygame.K_ESCAPE: self.running = 0
                                        if event.type == pygame.MOUSEBUTTONUP:
                                                pos = pygame.mouse.get_pos()
                                                if bounds.collidepoint(pos):
                                                        self.init_game()
                                                        self.game_running = 1


                                #Clear screen
                                screen_bounds = pygame.Rect((0,0),(self.screen.get_width(),self.screen.get_height()))
                                pygame.draw.rect(self.screen,(0,0,0), screen_bounds)
                                #Draw green square
                                pygame.draw.rect(self.screen, (0,255,0), bounds)
                                #draw title
                                label = titleFont.render("MATTER", 1, (255,255,0))
                                self.screen.blit(label, (420, 200))
                                startLabel = startFont.render("Start", 1, (255,255,255))
                                self.screen.blit(startLabel, (510,430))
                                pygame.display.update()
                                



        #returns whether or not the object is to the right of the left side of the screen.
        #True if the object has not fallen off the screen
        #False if the object has falled off the screen
        def is_on_screen(self, _object):
                #return (_object.position[0] + _object.dimension[0] > self.camera_translation)
                if(_object.position[0] + _object.dimension[0] > self.camera_translation):
                        return True
                else:
                        #self.score += 1
                        self.score_check = True
                        return False

        def read_file(self, file_path):
                pass

        def write_file(self, file_path):
                pass
        


#Program starts here if this file is ran from command line
def main():
        pygame.init()
        pygame.display.set_mode((1024, 768), pygame.RESIZABLE)
                #test resize for my laptop (Josh)
        #pygame.display.set_mode((768, 512), pygame.RESIZABLE)
        game = MatterGame()
        game.run()
        print("closing")

#In case of name mangling
if __name__ == '__main__':
        main()
