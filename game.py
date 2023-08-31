import pygame as pg
import sys

class Game:
    def __init__(self):
        pg.init()
        self.FPS = 10
        self.DIMENSIONS = [500,500]
        self.clock = pg.time.Clock()
        pg.display.set_caption('snake game')
        self.screen = pg.display.set_mode(self.DIMENSIONS)
        self.font = pg.font.SysFont('Verdana', 20)
        self.fpsText = self.font.render(str(round(self.clock.get_fps())), True, (0,0,0))

    def renderFPStext(self):
        self.fpsText = self.font.render(str(round(self.clock.get_fps(),2)), True, (127,127,127))
        self.screen.blit(self.fpsText, (0,0))

    def processInput(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

    def run(self):
        running = True
        while running:
            #check input
            self.processInput()

            self.screen.fill('black')

            #Render here
            self.renderFPStext()

            pg.display.flip()
            self.clock.tick(self.FPS)

Game().run()


