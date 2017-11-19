import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("Metal_Trash_Can_Filled.wav")
pygame.mixer.music.load("So_Far_Away.wav")
gameover_sound = pygame.mixer.Sound("you_suck.wav")

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
bright_blue = (0,0,250)
bright_red = (255,0,0)
bright_green = (0,255,0)
street_color = (50,50,50)
side_walk = (204,204,204)
yellow = (221,255,0)


block_color = (53,115,255)

car_width = 95

highscore = 0

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Race Game')
clock = pygame.time.Clock()

carImg = pygame.image.load('game_car.png')
carImg = pygame.transform.scale(carImg, (150, 160))

pause = False

def sidewalk_lines(startr, endr, startl, endl):
    pygame.draw.line(gameDisplay, black, startr, endr, 4)
    pygame.draw.line(gameDisplay, black, startl, endl, 4)

def street_lines(streetlinex, streetliney, streetlineh, streetlinew, color):
    pygame.draw.rect(gameDisplay, color, [streetlinex, streetliney, streetlineh, streetlinew])

def sidewalk(color):
    pygame.draw.rect(gameDisplay, color, [0,0,125,600])
    pygame.draw.rect(gameDisplay, color, [675,0,125,600])

def things_dodged(count):
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render("Dodged: "+str(count), True, white)
    gameDisplay.blit(text, (0,0))

def high_score(big_score):
    font = pygame.font.Font("freesansbold.ttf", 25)
    text = font.render("Highscore: " + str(big_score), True, white)
    gameDisplay.blit(text, (630,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x,y):
    gameDisplay.blit(carImg,(x,y))


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text):
    # largeText = pygame.font.Font('freesansbold.ttf',60)
    # TextSurf, TextRect = text_objects(text, largeText)
    # TextRect.center = ((display_width/2), (display_height/2))
    # gameDisplay.blit(TextSurf, TextRect)
    #
    # pygame.display.update()
    #
    # time.sleep(2)
    #
    # game_loop()

    stime = time.localtime(time.time())[5]
    largeText = pygame.font.Font('freesansbold.ttf',70)
    textsurf,textrect = text_objects(text, largeText, black)
    textrect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(textsurf, textrect)

    pygame.display.update()

    if time.localtime(time.time())[5]>stime:
        game_loop()


def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    if dodged == highscore:
        scoreboard(highscore)

    if dodged <= highscore:
        largeText = pygame.font.Font('freesansbold.ttf',80)
        textsurf,textrect = text_objects("You Crashed Loser!!", largeText, black)
        textrect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(textsurf, textrect)

        pygame.mixer.Sound.play(gameover_sound)

        while True:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #gameDisplay.fill(white)

            button("Play Again",150,450,125,50, green, bright_green,game_loop)
            button("Quit",550,450,100,50, red, bright_red,quitgame)

            pygame.display.update()
            clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def scoreboard(score):

    pygame.mixer.music.stop()
    # gameDisplay.fill(white)

    midText = pygame.font.Font("freesansbold.ttf", 80)
    textsurfa, textrecta = text_objects("HIGHSCORE: " + str(score), midText, white)
    textrecta.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textsurfa, textrecta)

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)

        button("Play Again",150,450,125,50, green, bright_green,game_loop)
        button("Quit",550,450,100,50, red, bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_intro():

    intro= True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',70)
        textsurf,textrect = text_objects("Wanna Play A Game?", largeText, black)
        textrect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(textsurf, textrect)

        # smallText = pygame.font.Font("freesansbold.ttf", 60)
        # textSufac, textRectan = text_objects("Highscore: " + str(highscore), smallText, red)
        # textRectan.center = ((display_width/2), 200)
        # gameDisplay.blit(textSufac, textRectan)

        button("GO!",150,450,100,50, green, bright_green,game_loop)
        button("Quit?",550,450,100,50, red, bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)


def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():

    pygame.mixer.music.pause()

    largeText = pygame.font.Font('freesansbold.ttf',100)
    textsurf,textrect = text_objects("Paused", largeText, white)
    textrect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(textsurf, textrect)

    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)

        button("Continue",150,450,100,50, green, bright_green,unpause)
        button("Restart", 350,450,100,50, blue, bright_blue, game_loop)
        button("Quit",550,450,100,50, red, bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    global dodged
    global highscore

    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.7)

    x_change = 0

    sidewalk_lineSr1 = [675,0]
    sidewalk_lineEr1 = [800,0]
    sidewalk_lineSl1 = [0,0]
    sidewalk_lineEl1 = [125,0]

    sidewalk_lineSr2 = [675,150]
    sidewalk_lineEr2 = [800,150]
    sidewalk_lineSl2 = [0,150]
    sidewalk_lineEl2 = [125,150]

    sidewalk_lineSr3 = [675,300]
    sidewalk_lineEr3 = [800,300]
    sidewalk_lineSl3 = [0,300]
    sidewalk_lineEl3 = [125,300]

    sidewalk_lineSr4 = [675,450]
    sidewalk_lineEr4 = [800,450]
    sidewalk_lineSl4 = [0,450]
    sidewalk_lineEl4 = [125,450]

    sidewalk_lineSr5 = [675,600]
    sidewalk_lineEr5 = [800,600]
    sidewalk_lineSl5 = [0,600]
    sidewalk_lineEl5 = [125,600]


    streetline_startx = display_width/2
    streetline_starty5 = -100
    streetline_starty4 = 50
    streetline_starty3 = 200
    streetline_starty2 = 350
    streetline_starty1 = 500
    #streetline_speed = 1
    streetline_height = 30
    streetline_width = 70

    #sidewalk_linespeed = streetline_speed

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 100
    thing_height = 100

    sidewalk_linespeed = thing_speed
    streetline_speed = thing_speed

    dodged = 0
    #previous_score = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                if event.key == pygame.K_RIGHT:
                    x_change = 7
                if event.key == pygame.K_p:
                    pause = True
                    paused()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(street_color)
        sidewalk(side_walk)

        #sidewalk_lines(startr, endr, startl, endl)
        sidewalk_lines(sidewalk_lineSr1, sidewalk_lineEr1, sidewalk_lineSl1, sidewalk_lineEl1)
        sidewalk_lineSr1[1] += sidewalk_linespeed
        sidewalk_lineEr1[1] += sidewalk_linespeed
        sidewalk_lineSl1[1] += sidewalk_linespeed
        sidewalk_lineEl1[1] += sidewalk_linespeed
        sidewalk_lines(sidewalk_lineSr2, sidewalk_lineEr2, sidewalk_lineSl2, sidewalk_lineEl2)
        sidewalk_lineSr2[1] += sidewalk_linespeed
        sidewalk_lineEr2[1] += sidewalk_linespeed
        sidewalk_lineSl2[1] += sidewalk_linespeed
        sidewalk_lineEl2[1] += sidewalk_linespeed
        sidewalk_lines(sidewalk_lineSr3, sidewalk_lineEr3, sidewalk_lineSl3, sidewalk_lineEl3)
        sidewalk_lineSr3[1] += sidewalk_linespeed
        sidewalk_lineEr3[1] += sidewalk_linespeed
        sidewalk_lineSl3[1] += sidewalk_linespeed
        sidewalk_lineEl3[1] += sidewalk_linespeed
        sidewalk_lines(sidewalk_lineSr4, sidewalk_lineEr4, sidewalk_lineSl4, sidewalk_lineEl4)
        sidewalk_lineSr4[1] += sidewalk_linespeed
        sidewalk_lineEr4[1] += sidewalk_linespeed
        sidewalk_lineSl4[1] += sidewalk_linespeed
        sidewalk_lineEl4[1] += sidewalk_linespeed
        sidewalk_lines(sidewalk_lineSr5, sidewalk_lineEr5, sidewalk_lineSl5, sidewalk_lineEl5)
        sidewalk_lineSr5[1] += sidewalk_linespeed
        sidewalk_lineEr5[1] += sidewalk_linespeed
        sidewalk_lineSl5[1] += sidewalk_linespeed
        sidewalk_lineEl5[1] += sidewalk_linespeed

        if sidewalk_lineSr1[1] > display_height:
            sidewalk_lineSr1[1] = -150
            sidewalk_lineEr1[1] = -150
            sidewalk_lineSl1[1] = -150
            sidewalk_lineEl1[1] = -150
            sidewalk_linespeed = thing_speed
        if sidewalk_lineSr2[1] > display_height:
            sidewalk_lineSr2[1] = -150
            sidewalk_lineEr2[1] = -150
            sidewalk_lineSl2[1] = -150
            sidewalk_lineEl2[1] = -150
            sidewalk_linespeed = thing_speed
        if sidewalk_lineSr3[1] > display_height:
            sidewalk_lineSr3[1] = -150
            sidewalk_lineEr3[1] = -150
            sidewalk_lineSl3[1] = -150
            sidewalk_lineEl3[1] = -150
            sidewalk_linespeed = thing_speed
        if sidewalk_lineSr4[1] > display_height:
            sidewalk_lineSr4[1] = -150
            sidewalk_lineEr4[1] = -150
            sidewalk_lineSl4[1] = -150
            sidewalk_lineEl4[1] = -150
            sidewalk_linespeed = thing_speed
        if sidewalk_lineSr5[1] > display_height:
            sidewalk_lineSr5[1] = -150
            sidewalk_lineEr5[1] = -150
            sidewalk_lineSl5[1] = -150
            sidewalk_lineEl5[1] = -150
            sidewalk_linespeed = thing_speed


        #street_lines(streetlinex, streetliney, streetlineh, streetlinew, color)
        street_lines(streetline_startx, streetline_starty5, streetline_height, streetline_width, yellow)
        streetline_starty5 += streetline_speed
        street_lines(streetline_startx, streetline_starty4, streetline_height, streetline_width, yellow)
        streetline_starty4 += streetline_speed
        street_lines(streetline_startx, streetline_starty3, streetline_height, streetline_width, yellow)
        streetline_starty3 += streetline_speed
        street_lines(streetline_startx, streetline_starty2, streetline_height, streetline_width, yellow)
        streetline_starty2 += streetline_speed
        street_lines(streetline_startx, streetline_starty1, streetline_height, streetline_width, yellow)
        streetline_starty1 += streetline_speed

        if streetline_starty1 > display_height:
            streetline_starty1 = -150
            streetline_speed = thing_speed
        if streetline_starty2 > display_height:
            streetline_starty2 = -150
            streetline_speed = thing_speed
        if streetline_starty3 > display_height:
            streetline_starty3 = -150
            streetline_speed = thing_speed
        if streetline_starty4 > display_height:
            streetline_starty4 = -150
            streetline_speed = thing_speed
        if streetline_starty5 > display_height:
            streetline_starty5 = -150
            streetline_speed = thing_speed

        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
        high_score(highscore)

        if x > display_width - car_width or x < - 50:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.6
            thing_width += (dodged * 1.1)

        if y < thing_starty + thing_height - 45:
            #print('y crossover')

            if x + 50 > thing_startx and x + 50 < thing_startx + thing_width or \
                x + car_width > thing_startx and \
                x + car_width < thing_startx + thing_width:
                    #print('x crossover')
                    crash()

        if dodged > highscore:
            highscore = dodged

        pygame.display.update()
        clock.tick(80)

game_intro()
game_loop()
pygame.quit()
quit()
