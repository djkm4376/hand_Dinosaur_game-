from my_G_img import random, pygame, SCREEN_WIDTH, SCREEN_HEIGHI, SCREEN, BACKGROUND, SMALL_CACTUS, LARGE_CACTUS, BIRD, RUNNING, Game_speed, obstacles
from Dinosaur import Dinosaur
from Cloud import Cloud
from Other_Obstacles import SmallCactus, LargeCactus, Bird



pygame.init() #초기화


def main():
    global x_pos_bg, y_pos_bg, points
    running = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    death_count = 0

    def score():
        global points, Game_speed
        points += 1
        if points % 100 == 0:
            Game_speed += 1
        
        text = font.render("points: " + str(points), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BACKGROUND.get_width()
        SCREEN.blit(BACKGROUND, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BACKGROUND, (image_width + x_pos_bg, y_pos_bg))

        if x_pos_bg <= -image_width:
            SCREEN.blit(BACKGROUND, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0

        x_pos_bg -= Game_speed

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # X 표시를 눌러 게임 종료 시 루프 탈출
                running = False

        SCREEN.fill((255,255,255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles: # 리스트 요소를 반복한다.
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect): #장애물에 부딫히면
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        background()
        cloud.draw(SCREEN)
        cloud.update()

        score()


        clock.tick(30)
        pygame.display.update()

    pygame.quit()


def menu(death_count):
    global points
    running = True

    while running:
        SCREEN.fill((255,255,255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
            score = font.render("Your Score : " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHI//2 + 50)
            SCREEN.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHI//2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH//2 - 20, SCREEN_HEIGHI // 2 - 140))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # X 표시를 눌러 게임 종료 시 루프 탈출
                running = False
                
            if event.type == pygame.KEYDOWN:
                main()


menu(death_count=0)


