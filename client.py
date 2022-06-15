from socket import *
from threading import Thread
import pygame

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 5500))

dec = client.recv(1024).decode()
if dec == 'Go':
    WIDTH, HEIGHT = 900, 500
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    x, y = WIDTH // 2, HEIGHT // 2
    speed = 5

    def Enemy():
        EnemyPosition = client.recv(1024).decode()
        EnemyPosition = eval(EnemyPosition)
        pygame.draw.rect(screen, 'red', pygame.Rect(EnemyPosition[0], EnemyPosition[1], 50, 50))

    def PlayerPositionSends():
        Player_Position = f'{str(x)}, {str(y)}'
        Player_Position_Final = str(Player_Position)
        client.send(Player_Position_Final.encode())

    def Player():
        global x, y
        pygame.draw.rect(screen, 'blue', pygame.Rect(x, y, 50, 50))
        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:
            y += speed

        if key[pygame.K_UP]:
            y -= speed
        if key[pygame.K_LEFT]:
            x -= speed

        if key[pygame.K_RIGHT]:
            x += speed


    run = True
    clock = pygame.time.Clock()

    while run:
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            Player()
            PlayerPositionSends()
            Enemy()
            
            pygame.display.update()            

    pygame.quit()