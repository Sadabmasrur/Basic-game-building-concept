import pygame

pygame.init()

screen_width, screen_height=600,600
screen= pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('Color changing squareee')

colors={
    'red': pygame.Color('red'),
    'blue': pygame.Color('blue'),
    'green': pygame.Color('green'),
    'purple': pygame.Color('purple'),
    'white': pygame.Color('white')
}

current_color=colors['white']

x,y=40,40
sprite_width,sprite_height=80,80

clock=pygame.time.Clock()
done=False

while not done:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

            done=True
           

    pressed=pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]: x-=3            

    if pressed[pygame.K_RIGHT]: x+=3     

    if pressed[pygame.K_UP]: y-=3     

    if pressed[pygame.K_DOWN]: y+=3     

    x = min(max(0, x), screen_width - sprite_width)
    y = min(max(0, y), screen_height - sprite_height)
                
                
    if x==0:current_color=colors["blue"]            
                
    elif x==screen_width-sprite_width:current_color=colors["red"]   
            
    elif y == 0:current_color=colors["green"]               
    elif y == screen_height-sprite_height:current_color=colors["purple"]    

    else: current_color= colors["white"]     

    screen.fill((194,156,233)) 

    pygame.draw.rect(screen,current_color,(x,y,sprite_width,sprite_height)) 

    pygame.display.flip()
    clock.tick(90)   
                