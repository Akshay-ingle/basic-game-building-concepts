import pygame 
pygame.init()
window=pygame.display.set_mode((400, 400))

window.fill((255, 255, 255))
GREEN=(184, 109, 52)
 
pygame.draw.circle(window,GREEN, (300,300),50)
pygame.draw.circle(window, GREEN,(100,100),50,3)
pygame.display.update()
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()             