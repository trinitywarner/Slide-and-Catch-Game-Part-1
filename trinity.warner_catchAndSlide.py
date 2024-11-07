import pygame, simpleGE, random

""" slide and catch pt. 1 """

class Pickle(simpleGE.Sprite):
    def __init__(self, scene):
        super()__init__(scene)
        self.setImage("pickle.png")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        #move to top of screen
        self.y = 10
        
        #x random 0 - screen width
        self.x = random.randit(0, self.screenWidth)
        
        #dy is random minSpeed to maxSpeed
        self.dy = random.randit(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
        
class Burger(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("burger#7.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5

    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed        
        if self.isKeyPressed(pygame.L_RIGHT):
            self.x += self.moveSpeed
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("background2.png")
        
        self.numPickles = 5
        
        self.burger = Burger(self)
        #self.pickle = Pickle(self)
        
        self.pickles = []
        for i in range(self.numPickles):
            self.pickles.append(Pickle(self))
            
        self.sprites = [self.burger,
                        self.pickles]
        
    def process(self):
        for pickle in self pickles:
            if coin.collidesWith(self.burger):
                coin.reset()
        
        
def main():
    game = Game()
    game.start()
        
if __name__ == "__main__":
    main()