import pygame #imported module

pygame.init() #initialises the module <---- load everything we need

screen = pygame.display.set_mode((1280, 720)) # <---- the numbers are width and height of the window
clock = pygame.time.Clock()
running = True
dt = 0 #delta time

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "red", player_pos, 69) #<----- circle(surface, colour, centre, radius)

    keys = pygame.key.get_pressed() #checking what keys have been pressed and moving the circle we created with the WASD keys
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt #can also be wrriten player_pos.y = player_pos.y - 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt #real time vs frames on pc, dt is the time between frames

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()