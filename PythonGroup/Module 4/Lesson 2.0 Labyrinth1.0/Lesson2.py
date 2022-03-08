birdSprite = "clumsy.png"
bird_velocity_y = -9  
bird_flap_velocity = -8
bird_flapped = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
            if vertical > 0:
                bird_velocity_y = bird_flap_velocity
                bird_flapped = True