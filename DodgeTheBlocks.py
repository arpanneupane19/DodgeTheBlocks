''' Code written by Arpan Neupane on 8/26/2020 '''
''' Copyright ©️ Arpan Neupane 2020 '''
''' Copyright ©️ DodgeTheBlocks 2020 '''
''' For more information, refer to the README.md file. '''

import pygame
import sys
import time
import random

pygame.init()
pygame.mixer.init()



''' Setting up the window '''
displayWidth = 800
displayHeight = 600

win = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("DodgeTheBlocks")
background = (0,0,0)
clock = pygame.time.Clock()

''' Colors for the buttons '''
bright_green = (0,255,0)
green = (0,128,0)

bright_red = (255,0,0)
red = (128,0,0)

bright_yellow = (200,200,0)
yellow = (128,128,0)

bright_blue = (0,0,255)
blue = (0,0,128)

font = pygame.font.SysFont('agencyfb', 40, bold=True)
crash_sound = pygame.mixer.Sound('sfx_hit.wav')

def text_objects(text, font):
    white = (255,255,255)
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def buttons(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(win, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(win, ic, (x,y,w,h))
    smallText = pygame.font.SysFont("agencyfb", 35, bold=True)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(textSurf, textRect)


def pause():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pause = False
                if event.key == pygame.K_q:
                    sys.exit()

        pause_game_text = font.render("Game Paused", True, (255,255,255))
        pause_game_contd = font.render("Press c to resume", True, (255,255,255))
        pause_game_exit = font.render("Press q to exit", True, (255,255,255))
        win.blit(pause_game_text, (300, 400))
        win.blit(pause_game_contd, (270, 450))
        win.blit(pause_game_exit, (290, 500))
        pygame.display.update()
        clock.tick(15)


def song1():
    pygame.mixer.music.load('HumbleMatch.wav')
    pygame.mixer.music.play(-1)

def song2():
    pygame.mixer.music.load('Chiptronical.wav')
    pygame.mixer.music.play(-1)


def music():
    global default
    black = (0,0,0)
    white = (255,255,255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                if event.key == pygame.K_q:
                    sys.exit()


        win.fill(black)
        select_music_text = pygame.font.SysFont("agencyfb", 60, bold=True)
        music_text = select_music_text.render("Select Music", True, white)
        win.blit(music_text,(250, 200))
        buttons("Song 1", 150,300,150,50, red, bright_red, song1)
        buttons("Song 2", 500,300,150,50, blue, bright_blue, song2)
        buttons("Back", 10,10,150,50, yellow, bright_yellow, main_menu)
        pygame.display.update()

        
    

def main_menu():
    black = (0,0,0)
    white = (255,255,255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                if event.key == pygame.K_q:
                    sys.exit()


        win.fill(black)
        main_men_text = pygame.font.SysFont("agencyfb", 60, bold=True)
        main_men_text_welcome = main_men_text.render("Welcome to DodgeTheBlocks!", True, white)
        main_men_text_render = main_men_text.render('PRESS SPACE TO PLAY', True, white)
        win.blit(main_men_text_render,(100, 300))
        win.blit(main_men_text_welcome,(50, 200))
        buttons("Help?", 150,450,150,50, yellow, bright_yellow, help)
        buttons("Music", 500,450,150,50, blue, bright_blue, music)
        pygame.display.update()


def help():
    black = (0,0,0)
    white = (255,255,255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    main_menu()
                if event.key == pygame.K_q:
                    sys.exit()

        win.fill(black)
        help_text = pygame.font.SysFont("agencyfb", 40, bold=True)
        help_text_render = help_text.render('Keybinds', True, white)
        help_text_keys_c = help_text.render('c: Continue', True, white)
        help_text_keys_q = help_text.render('q: Exit', True, white)
        help_text_keys_p = help_text.render('p: Pause', True, white)
        help_text_keys_right = help_text.render("Right arrow: move right", True, white)
        help_text_keys_left = help_text.render("Left arrow: move left", True, white)
        help_src_code = help_text.render("Code: github.com/arpanneupane19/DodgeTheBlocks", True, white)
        win.blit(help_text_render, (325, 50))
        win.blit(help_text_keys_c, (325, 100))
        win.blit(help_text_keys_q, (325, 150))
        win.blit(help_text_keys_p, (325, 200))
        win.blit(help_text_keys_right, (325, 250))
        win.blit(help_text_keys_left, (325, 300))
        win.blit(help_src_code, (0, 350))

        buttons("Back", 20,20,150,50, yellow, bright_yellow, main_menu)
        pygame.display.update()
        clock.tick(15)
        


def crash():
    crash_sound.play()
    crashed = True
    while crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    main()
                if event.key == pygame.K_q:
                    sys.exit()

        crashed_game_text = font.render("Game Over", True, (255,255,255))
        win.blit(crashed_game_text, (325, displayHeight/2))
        buttons("Play Again", 150,350,150,50, green, bright_green, main)
        buttons("Menu", 325,350,150,50, yellow, bright_yellow, main_menu)
        buttons("Exit", 500,350,150,50, red, bright_red, exit)
        pygame.display.update()
        clock.tick(15)

def exit():
    sys.exit()



def main():
    ''' Main game loop'''

    ''' Enemy block '''
    e_height = 50
    e_width = 100
    e_startx = random.randrange(0, displayWidth-e_width)
    e_starty = -5
    e_speed = 8

    ''' Player block '''
    p_height = 50
    p_width = 50
    p_x = displayWidth/2
    p_y = displayHeight/2
    p_speed = 11
    score = 0

    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if keys[pygame.K_RIGHT]:
            p_x += p_speed
        if keys[pygame.K_LEFT]:
            p_x -= p_speed
        if keys[pygame.K_q]:
            sys.exit()
        if keys[pygame.K_p]:
            pause()

        ''' Detect collision between player block and wall '''
        if p_x > displayWidth-p_width or p_x < 0:
            crash()
            p_x = displayWidth/2

        ''' Updating the score and spawning a new enemy block '''
        e_starty = e_speed + e_starty  
        if e_starty > displayHeight:
            e_startx = random.randrange(0, displayWidth-e_width)
            e_starty = -5
            score += 1
            e_speed += 1
            p_speed += 1

        score_text = "Score: " + str(score)
        score_text_draw = font.render(score_text, True, bright_green)        
        win.fill(background)
        enemy = pygame.draw.rect(win, (255,0,0), (e_startx, e_starty, e_width, e_height))
        player = pygame.draw.rect(win, (0,0,255), (p_x, p_y, p_width, p_height))
        win.blit(score_text_draw,(0,0))

        ''' Check for collision between player and enemy '''
        if enemy.colliderect(player):
            crash()

        clock.tick(60)
        pygame.display.update()


main_menu()
