import pygame
import random
import time
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,152,0)


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Slither: Henry's first pygamegame")

clock = pygame.time.Clock()

block_size = 10
FPS = 30
font = pygame.font.SysFont(None, 25)
#snake function
def snake(block_size,snakeList):
    #XnY is a temporary element that we use to refer to our function
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])


#text function
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width / 2  # Leader of group, number one block
    lead_y = display_height / 2  # snake built in sections

    lead_x_change = 0  # more placeholders
    lead_y_change = 0
    snakeList = [] #Creates a list in a list, body of the snake
    snakeLength = 1
#This gives us an apple in a random place
    randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
#However, we need to ROUND the random number to a tenth by using the round func.
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over! Press C to play again or Q to Quit!", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit= True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                 lead_x_change = -block_size
                 lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
    #The following line of code is dictating what a boundary is and calling a gameOver
        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY,block_size,block_size])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
        #If the length of the list is more than 1, delete the first element.
        #Next, we will determine a crash with the snakes body
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        snake(block_size, snakeList)
        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            print("Om nom nom nom")
            randAppleX = round(random.randrange(0, display_width - block_size)/10.0) * 10.0
            randAppleY = round(random.randrange(0, display_height - block_size)/10.0) * 10.0
            snakeLength += 1
        clock.tick(FPS)#built in fps system
        pygame.display.update()

    pygame.quit()
    quit()

gameLoop()
