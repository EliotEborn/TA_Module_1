# Example file showing a basic pygame "game loop"
import pygame
import random

WIDTH = 1280
HEIGHT = 720
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0 #deltatime

class Boid:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x,y)

    def draw (self, screen):
        top = pygame.Vector2(self.position.x, self.position.y)
        right = pygame.Vector2(self.position.x+2,self.position.y+2)
        left = pygame.Vcetor2(x-2,)
        pygame.draw.polygon(screen, "black", )

def create_boids(total_num_boids):
    boids_list = []
    boids_list.append(Boid(random.uniform(0, WIDTH), random.uniform(0, HEIGHT)))

    boids_list = [Boid(random.uniform(0, WIDTH), random.uniform(0, HEIGHT)) for _ in range (total_num_boids)]

    return boids_list
        

def main():

    boids = create_boids(100)
    running = True


    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000  # limits FPS to 60

#pygame.quit()