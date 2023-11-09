from modules.application.build import Build
from pygame import init, display, time, event, QUIT, DOUBLEBUF, OPENGL, GL_DEPTH_SIZE
from random import uniform, randint



class App():

    def __init__(self) -> None:
        self.build = Build()
        self.spheres = []
        self.initialisation = self.build.set_dictionary()
        # dimensions
        self.width, self.height = self.initialisation["Dimensions"]["maximum_width"],self.initialisation["Dimensions"]["maximum_height"]
        # initialisation de pygame
        init()
        # creation d'une window
        self.screen = display.set_mode((self.width,self.height),flags=DOUBLEBUF | OPENGL | GL_DEPTH_SIZE) # self.initialisation["Initialisation"]["user_flags"]


    def event_listener(self) -> None:
        for events in event.get():
            if events.type == QUIT:
                self.running = False
        
    
    def gameLoop(self) -> None:
        pass