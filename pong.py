import pygame
from pygame.locals import *
import random

pygame.init()


WIDTH = 800
HEIGHT = 400
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

ball_pos = [int(WIDTH / 2), int(HEIGHT / 2)]
ball_vel = [4, 4]

paddle_pos = [20, int(HEIGHT / 2 - 40)]
paddle_vel = [0, 0]
paddle_speed = 5

robot_pos = [WIDTH - 40, int(HEIGHT / 2 - 40)]
robot_vel = [0, 0]
robot_speed = 4

score_player = 0
score_robot = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                paddle_vel[1] = -paddle_speed
            elif event.key == K_DOWN:
                paddle_vel[1] = paddle_speed
        elif event.type == KEYUP:
            if event.key == K_UP or event.key == K_DOWN:
                paddle_vel[1] = 0


    paddle_pos[1] += paddle_vel[1]
    if paddle_pos[1] < 0:
        paddle_pos[1] = 0
    if paddle_pos[1] > HEIGHT - 80:
        paddle_pos[1] = HEIGHT - 80

    # Update robot position
    if ball_pos[1] < robot_pos[1] + 40:
        robot_vel[1] = -robot_speed
    elif ball_pos[1] > robot_pos[1] + 40:
        robot_vel[1] = robot_speed
    else:
        robot_vel[1] = 0

    robot_pos[1] += robot_vel[1]
    if robot_pos[1] < 0:
        robot_pos[1] = 0
    if robot_pos[1] > HEIGHT - 80:
        robot_pos[1] = HEIGHT - 80


    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]


    if ball_pos[1] < 0 or ball_pos[1] > HEIGHT - 20:
        ball_vel[1] = -ball_vel[1]

 
    if ball_pos[0] < 40 and paddle_pos[1] < ball_pos[1] < paddle_pos[1] + 80:
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[0] > WIDTH - 60 and robot_pos[1] < ball_pos[1] < robot_pos[1] + 80:
        ball_vel[0] = -ball_vel[0]
    else:
        if ball_pos[0] < 0:
            score_robot += 1
            ball_pos = [int(WIDTH / 2), int(HEIGHT / 2)]
            ball_vel = [4, 4]
            robot_speed = min(8, robot_speed + 1)
        elif ball_pos[0] > WIDTH - 20:
            score_player += 1
            ball_pos = [int(WIDTH / 2), int(HEIGHT / 2)]
            ball_vel = [-4, 4]
            paddle_speed = min(8, paddle_speed + 1)

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), Rect(ball_pos[0], ball_pos[1], 20, 20))
    pygame.draw.rect(screen, (255, 255, 255), Rect(paddle_pos[0], paddle_pos[1], 20, 80))
    pygame.draw.rect(screen, (255, 255, 255), Rect(robot_pos[0], robot_pos[1], 20, 80))

    font = pygame.font.Font(None, 36)
    text_player = font.render("Player: " + str(score_player), 1, (255, 255, 255))
    text_robot = font.render("Robot: " + str(score_robot), 1, (255, 255, 255))
    screen.blit(text_player, (10, 10))
    screen.blit(text_robot, (WIDTH - text_robot.get_width() - 10, 10))

    pygame.display.flip()

    clock.tick(FPS)

# Quit the game
pygame.quit()
