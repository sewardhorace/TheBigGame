import pygame

# define colors

BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()

#screen size
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Gamma, baby")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #game logic goes here

    #drawing code here, starting with
    screen.fill(WHITE)
    for y_offset in range(0,100,10):
        pygame.draw.line(screen, BLACK, [0,0+ y_offset], [100, 110+y_offset],5)

    #update screen
    pygame.display.flip()

    clock.tick(40) #fps

pygame.quit()

    
