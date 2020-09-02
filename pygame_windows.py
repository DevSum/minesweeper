import pygame
import sys


pygame.init()
bg = (117, 214, 251)
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("扫雷")
pygame.display.set_icon(pygame.image.load("resources/icon.jpg"))

black = pygame.image.load("resources/black.png")
black = pygame.transform.smoothscale(black, (30, 30))
white = pygame.image.load("resources/white.png")
white = pygame.transform.smoothscale(white, (30, 30))

board = pygame.image.load("resources/board.jpg")
board_size = board.get_size()
board = pygame.transform.smoothscale(board, (int(size[1]), int(size[1])))

def print_pieces(screen, pieces_state):
    for row in range(15):
        for col in range(15):
            if pieces_state[row][col] == 1:
                screen.blit(black, (int(15 + row * 38.75), int(15 + col * 38.75)))
            if pieces_state[row][col] == 2:
                screen.blit(white, (int(15 + row * 38.75), int(15 + col * 38.75)))

while True:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            place = (int((event.pos[0] - 12) / 38.75), int((event.pos[1] - 12) / 38.75))
            print(event.pos)

        if event.type == pygame.QUIT:
            sys.exit(0)

    screen.fill(bg)
    screen.blit(board,(0,0))

    pygame.display.flip()
