import pygame
import time
import random
import sys
pygame.init()

#to set resolution
display_width=600
display_height=600

black=(0,0,0)
red =(255,0,0)
green=(0,255,0)
silver=(150,150,150)
random_color=(120,60,190)


gameDisplay=pygame.display.set_mode((display_width,display_height))

#to set title
pygame.display.set_caption("Tic Tac Toe")
#
clock=pygame.time.Clock()

tictacimage=pygame.image.load("tictactoe.png")


def text_objects(text,font):
    textSurface=font.render(text,True,silver)
    return textSurface,textSurface.get_rect()

def text_objects_final(text,font):
    textSurface=font.render(text,True,random_color)
    return textSurface,textSurface.get_rect()

def background_image():
    gameDisplay.blit(tictacimage,(0,0))

def message_display(text,x,y):
    largeText=pygame.font.Font('freesansbold.ttf',120)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=(x,y)
    gameDisplay.blit(TextSurf,TextRect)

def show(text,*place):
    x,y=place
    message_display(text,x,y)

ximage=pygame.image.load("tictactoe.png")
def background_image1(x,y):
    gameDisplay.blit(ximage,(x,y))

def final_message(text):
    largeText=pygame.font.Font('freesansbold.ttf',75)
    TextSurf,TextRect=text_objects_final(text,largeText)
    TextRect.center=(300,300)
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(3)


#setting resolution for all nine blocks to place text as centered
resolution=[(100,100),(300,100),(500,100),(100,307),(300,307),(500,307),(100,510),(300,510),(500,510)]
#initially setting the positions to -100 to look board as empty
coordinate=[(-100,-100),(-100,-100),(-100,-100),(-100,-100),(-100,-100),(-100,-100),(-100,-100),(-100,-100),(-100,-100)]

#initially all the X or O are empty in the block
t=[" "," "," "," "," "," "," "," "," "]

board=[0,1,2,3,4,5,6,7,8]
def checkforallpositions(char):
    if checkforwin(char,0,1,2):
        return True
    if checkforwin(char,1,4,7):
        return True
    if checkforwin(char,2,5,8):
        return True
    if checkforwin(char,6,7,8):
        return True
    if checkforwin(char,3,4,5):
        return True
    if checkforwin(char,2,4,6):
        return True
    if checkforwin(char,0,3,6):
        return True
    if checkforwin(char,0,4,8):
        return True

def checkforwin(char,spot1,spot2,spot3):
    if board[spot1]==char and board[spot2]==char and board[spot3]==char:
        return True

def draw():
    flag=True
    for i in range(0,9):
        if board[i]!='O' and board[i]!='X':
            flag=False
    return flag

#AI using minimax
def minimax(char):
    if char=='X':
          if checkforallpositions('X'):
            return 1
    else:
          if checkforallpositions('O'):
            return 1
    move=-1
    score=-2
    for i in range(0,9):
        if board[i]!='O' and board[i]!='X':
            board[i]=char
            if char=='X':
                thisscore=-minimax('O')
            else:
                thisscore=-minimax('X')
            if thisscore>score:
                score=thisscore
                move=i
            board[i]=i
    if move==-1:
        return 0
    return score

#function to decide computer move which calls minimax to decide the move
def computer_move():
    move=-1
    score=-2
    for i in range(0,9):
        if board[i]!='O' and board[i]!='X':
            board[i]='O'
            tempscore=-minimax('X')
            board[i]=i
            if tempscore > score:
                score=tempscore
                move=i
    return move


#game loop
game=True
while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
        if event.type==pygame.MOUSEBUTTONDOWN:          #to get cursor position on pressing of mousing
            x,y=event.pos
            if x>=0 and x<=180 and y>=0 and y<=180:      #deciding the block position on the basis of curson's position on clicking
                if board[0]!='X' and board[0]!='O':
                    board[0]='X'
                    t[0]="X"
                    coordinate[0]=resolution[0]          #go for user's move and check for win and draw situations
                    if checkforallpositions('X'):
                        m,n=coordinate[0]
                        show('X',m,n)
                        final_message("You win!!")
                        quit()
                    if draw():
                        m,n=coordinate[0]
                        show('X',m,n)
                        final_message("It is a Draw!!")
                        quit()
                                                                                    #now computer will move
                    opponent=computer_move()
                    board[opponent]='O'
                    t[opponent]='O'
                    coordinate[opponent]=resolution[opponent]
                    if checkforallpositions('O'):
                        m,n=coordinate[opponent]
                        a,b=coordinate[0]
                        show('X',a,b)
                        show('O',m,n)
                        final_message("Ha Ha Ha!!")
                        quit()

            elif x>=225 and x<=376 and y>=0 and y<=180:
                if board[1]!='X' and board[1]!='O':
                    board[1]='X'
                    t[1]="X"
                    coordinate[1]=resolution[1]
                    if checkforallpositions('X'):
                        m,n=coordinate[1]
                        show('X',m,n)
                        final_message("You win!!")
                        quit()
                    if draw():
                        m,n=coordinate[1]
                        show('X',m,n)
                        final_message("It is a Draw!!")
                        quit()
                    opponent=computer_move()
                    board[opponent]='O'
                    t[opponent]='O'
                    coordinate[opponent]=resolution[opponent]
                    if checkforallpositions('O'):
                        m,n=coordinate[opponent]
                        a,b=coordinate[1]
                        show('X',a,b)
                        show('O',m,n)
                        final_message("Ha Ha Ha!!")
                        quit()

            elif x>=415 and x<=600 and y>=0 and y<=180:
                if board[2]!='X' and board[2]!='O':
                    board[2]='X'
                    t[2]="X"
                    coordinate[2]=resolution[2]
                    if checkforallpositions('X'):
                        m,n=coordinate[2]
                        show('X',m,n)
                        final_message("You win!!")
                        quit()
                    if draw():
                        m,n=coordinate[2]
                        show('X',m,n)
                        final_message("It is a Draw!!")
                        quit()
                    opponent=computer_move()
                    board[opponent]='O'
                    t[opponent]='O'
                    coordinate[opponent]=resolution[opponent]
                    if checkforallpositions('O'):
                        m,n=coordinate[opponent]
                        a,b=coordinate[2]
                        show('X',a,b)
                        show('O',m,n)
                        final_message("Ha Ha Ha!!")
                        quit()

            elif x>=0 and x<=180 and y>=231 and y<=370:
                if board[3]!='X' and board[3]!='O':
                    board[3]='X'
                    t[3]="X"
                    coordinate[3]=resolution[3]
                    if checkforallpositions('X'):
                        m,n=coordinate[3]
                        show('X',m,n)
                        final_message("You win!!")
                        quit()
                    if draw():
                        m,n=coordinate[3]
                        show('X',m,n)
                        final_message("It is a Draw!!")
                        quit()
                    opponent=computer_move()
                    board[opponent]='O'
                    t[opponent]='O'
                    coordinate[opponent]=resolution[opponent]
                    if checkforallpositions('O'):
                        m,n=coordinate[opponent]
                        show('O',m,n)
                        a,b=coordinate[3]
                        show('X',a,b)
                        final_message("Ha Ha Ha!!")
                        quit()

            elif x>=226 and x<=376 and y>=231 and y<=370:
                if board[4]!='X' and board[4]!='O':
                    board[4]='X'
                    t[4]="X"
                    coordinate[4]=resolution[4]
                    if checkforallpositions('X'):
                        m,n=coordinate[4]
                        show('X',m,n)
                        final_message("You win!!")
                        quit()
                    if draw():
                        m,n=coordinate[4]
                        show('X',m,n)
                        final_message("It is a Draw!!")
                        quit()
                    opponent=computer_move()
                    board[opponent]='O'
                    t[opponent]='O'
                    coordinate[opponent]=resolution[opponent]
                    if checkforallpositions('O'):
                        m,n=coordinate[opponent]
                        a,b=coordinate[4]
                        show('X',a,b)
                        show('O',m,n)
                        final_message("Ha Ha Ha!!")
                        quit()
               
            elif x>=415 and x<=600 and y>=231 and y<=370:
                if board[5]!='X' and board[5]!='O':
                    board[5]='X'
                    t[5]="X"
                    coordinate[5]=resolution[5]
                    if checkforallpositions('X'):
                        m,n=coordinate[5]
                        show('X',m,n)
                        final_message("You win!!")
                        quit()
                    if draw():
                        m,n=coordinate[5]
                        show('X',m,n)
                        final_message("It is a Draw!!")
                        quit()
                    opponent=computer_move()
                    board[opponent]='O'
                    t[opponent]='O'
                    coordinate[opponent]=resolution[opponent]
                    if checkforallpositions('O'):
                        m,n=coordinate[opponent]
                        a,b=coordinate[5]
                        show('X',a,b)
                        show('O',m,n)
                        final_message("Ha Ha Ha!!")
                        quit()

            elif x>=0 and x<=180 and y>=420 and y<=600:
                if board[6]!='X' and board[6]!='O':
                    board[6]='X'
                    t[6]="X"
                    coordinate[6]=resolution[6]
                    if checkforallpositions('X'):
                        m,n=coordinate[6]
                        show('X',m,n)
                        final_message("You win!!")
                        quit()
                    if draw():
                        m,n=coordinate[6]
                        show('X',m,n)
                        final_message("It is a Draw!!")
                        quit()
                    opponent=computer_move()
                    board[opponent]='O'
                    t[opponent]='O'
                    coordinate[opponent]=resolution[opponent]
                    if checkforallpositions('O'):
                        m,n=coordinate[opponent]
                        a,b=coordinate[6]
                        show('X',a,b)
                        show('O',m,n)
                        final_message("Ha Ha Ha!!")
                        quit()

            elif x>=225 and x<=376 and y>=420 and y<=600:
                if board[7]!='X' and board[7]!='O':
                    board[7]='X'
                    t[7]="X"
                    coordinate[7]=resolution[7]
                    if checkforallpositions('X'):
                        m,n=coordinate[7]
                        show('X',m,n)
                        final_message("You win!!")
                        quit()
                    if draw():
                        m,n=coordinate[7]
                        show('X',m,n)
                        final_message("It is a Draw!!")
                        quit()
                    opponent=computer_move()
                    board[opponent]='O'
                    t[opponent]='O'
                    coordinate[opponent]=resolution[opponent]
                    if checkforallpositions('O'):
                        m,n=coordinate[opponent]
                        a,b=coordinate[7]
                        show('X',a,b)
                        show('O',m,n)
                        final_message("Ha Ha Ha!!")
                        quit()

            elif x>=415 and x<=600 and y>=420 and y<=600:
                if board[8]!='X' and board[8]!='O':
                    board[8]='X'
                    t[8]="X"
                    coordinate[8]=resolution[8]
                    if checkforallpositions('X'):
                        m,n=coordinate[8]
                        show('X',m,n)
                        final_message("You win!!")
                        quit()
                    if draw():
                        m,n=coordinate[8]
                        show('X',m,n)
                        final_message("It is a Draw!!")
                        quit()
                    opponent=computer_move()
                    board[opponent]='O'
                    t[opponent]='O'
                    coordinate[opponent]=resolution[opponent]
                    if checkforallpositions('O'):
                        m,n=coordinate[opponent]
                        a,b=coordinate[8]
                        show('X',a,b)
                        show('O',m,n)
                        final_message("Ha Ha Ha!!")
                        quit()

    pygame.display.update()
    gameDisplay.fill(black)
    background_image()

    x,y=coordinate[0]
    show(t[0],x,y)                      #calling all the show function for each block continusly in the loop 

    x,y=coordinate[1]
    show(t[1],x,y)

    x,y=coordinate[2]
    show(t[2],x,y)

    x,y=coordinate[3]
    show(t[3],x,y)
    
    x,y=coordinate[4]
    show(t[4],x,y)

    x,y=coordinate[5]
    show(t[5],x,y)

    x,y=coordinate[6]
    show(t[6],x,y)
    
    x,y=coordinate[7]
    show(t[7],x,y)


    x,y=coordinate[8]
    show(t[8],x,y)
    pygame.display.update()


pygame.quit()
quit()

