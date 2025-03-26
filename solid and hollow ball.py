import pygame

pygame.init()

window=pygame.display.set_mode((500,500))

window.fill((255,255,255))

purple=(194,156,223)

pygame.draw.circle(window,purple,(300,300),50)

pygame.draw.circle(window,purple,(100,100),50,4)

pygame.display.update()

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
pygame.quit()            