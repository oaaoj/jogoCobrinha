#Projeto Jogo da Cobrinha

import pygame
import time
import random

#iniciando a biblioteca (tela)

pygame.init()

green = (0,128,0)
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,102)
blue = (50,153,213)

#tela

d_height = 600
d_width = 800
displ_ay = pygame.display.set_mode((d_width,d_width))
pygame.display.set_caption('Cobrinha')

snake_sqr = 10 # largura da cobrinha
snake_move = 20 # velocidade da cobrinha

clock = pygame.time.Clock()

font_type = pygame.font.SysFont(None, 20)
font_score_type = pygame.font.SysFont(None, 30)

def cobrinha(snake_sqr, snake_tail):
    for x in snake_tail:
        pygame.draw.rect(displ_ay, green, [x[0], x[1], snake_sqr, snake_sqr])

def message(msg, color):
    messeger = font_type.render(msg,True,color)
    displ_ay.blit(messeger, [d_width/3, d_width/3])


def game_loop():
    game_over = False
    game_close = False

    x1 = d_width/2
    y1 = d_height/2
    x1_loc = 0
    y1_loc = 0

    snake_Tail = []
    tail_of_snake = 1

    food_x = round(random.randrange(0, d_width - snake_sqr)/10.0) * 10.0
    food_y = round(random.randrange(0, d_width - snake_sqr)/10.0) * 10.0


    while not game_over:

        while game_close == True:
            displ_ay.fill(black)
            message("Você perdeu! Aperte S para sair ou R para reiniciar", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_s:
                        game_over = True
                        game_close = False
                    elif event.key==pygame.K_r:
                        game_loop()        

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over = True

            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_loc = -snake_sqr
                    y1_loc = 0
                elif event.key == pygame.K_RIGHT:
                    x1_loc = snake_sqr
                    y1_loc = 0
                elif event.key == pygame.K_UP:
                    y1_loc = -snake_sqr
                    x1_loc = 0
                elif event.key == pygame.K_DOWN:
                    y1_loc = snake_sqr
                    x1_loc = 0

     

        x1 += x1_loc
        y1 += y1_loc

        displ_ay.fill(white)
        pygame.draw.rect(displ_ay, red,[food_x,food_y,snake_sqr,snake_sqr])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_Tail.append(snake_head)

        if len(snake_Tail) > tail_of_snake:
            del snake_Tail[0]    
        
        for x in snake_Tail[:-1]:
            if x == snake_head:
                game_close = True

        cobrinha(snake_sqr, snake_Tail)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, d_width - snake_sqr)/10.0) * 10.0
            food_y = round(random.randrange(0, d_width - snake_sqr)/10.0) * 10.0

            tail_of_snake += 1
            
        clock.tick(snake_move)
    
    pygame.quit()
    quit()

game_loop()