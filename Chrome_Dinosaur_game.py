import my_image
import random

def crouch():
    my_image.pygame.K_DOWN


def jumping():
    my_image.pygame.K_UP

def KeyV():
    jumping()

    crouch()


def game(q):

    my_image.pygame.init() #초기화

    #전역 상수 선언
    SCREEN_HEIGHI = 600
    SCREEN_WIDTH = 1100

    my_image.pygame.display.set_caption("Dinosaur Game")
    SCREEN = my_image.pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHI))


    class Dinosaur():
        X_POS = 80
        Y_POS = 310
        Y_POS_DUCK = 340
        JUMP_VEL = 8.5

        def __init__(self):
            # 이미지 가져오기
            self.duck_img = my_image.DUCKING
            self.run_img = my_image.RUNNING
            self.jump_img = my_image.JUMPING

            # 초기값
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
            
            self.step_index = 0
            self.jump_vel = self.JUMP_VEL
            self.image = self.run_img[0]
            self.dino_rect = self.image.get_rect() #피격범위 설정
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS

        def update(self, userInput):
            if self.dino_duck:
                self.duck()
            if self.dino_run:
                self.run()
            if self.dino_jump:
                self.jump()

            if self.step_index >= 10:
                self.step_index = 0

            #    
            if q.get()=='Jump' and not self.dino_jump:
                self.dino_duck = False
                self.dino_jump = True
                self.dino_run = False
            elif q.get()=='Duck' and not self.dino_jump:
                self.dino_duck = True
                self.dino_jump = False
                self.dino_run = False
            elif q.get()=='Run' and not q.get()=='Duck' and not q.get()=='Jump' and not self.dino_jump:
                self.dino_duck = False
                self.dino_jump = False
                self.dino_run = True

        def duck(self):
            self.image = self.duck_img[self.step_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS_DUCK
            self.step_index += 1

        def run(self):
            self.image = self.run_img[self.step_index // 5] # 0 0 0 0 1 1 1 1 1
            self.dino_rect = self.image.get_rect() # 피격범위 설정
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS
            self.step_index += 1 # 0부터 9까지 반복 중에 5로 나눈 몫을 사용함

        def jump(self):
            # 제어, 제어계측
            self.image = self.jump_img
            if self.dino_jump:
                self.dino_rect.y -= self.jump_vel * 4 #8.5에서 4를 곱한것을 빼면 점프가됨 # 8.5 * 4 = 34만큼 상승 
                self.jump_vel -= 0.8 # 착지를 위한 -
            if self.jump_vel < -self.JUMP_VEL:
                self.dino_jump = False
                self.jump_vel = self.JUMP_VEL #초기화

        def draw(self, SCREEN):
            SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        
    class Cloud():
        def __init__(self):
            self.x = SCREEN_WIDTH + random.randint(800 ,1000)
            self.y = random.randint(50, 100)
            self.image = my_image.CLOUD
            self.width = self.image.get_width()

        def update(self):
            self.x -= game_speed
            if self.x < -self.width:
                self.x = SCREEN_WIDTH + random.randint(2600, 3000)
                self.y = random.randint(50 ,100)

        def draw(self, SCREEN):
            SCREEN.blit(self.image, (self.x, self.y))

    class Obstacle: #장애물
        def __init__(self, image, type):
            self.image = image
            self.type = type
            self.rect = self.image[self.type].get_rect()
            self.rect.x = SCREEN_WIDTH

        def update(self):
            self.rect.x -= game_speed
            if self.rect.x < -self.rect.width:
                obstacles.pop() #리스트의 마지막 요소를 반환하고 제거한다.

        def draw(self, SCREEN):
            SCREEN.blit(self.image[self.type], self.rect)

    class SmallCactus(Obstacle):
        def __init__(self, image):
            self.type = random.randint(0, 2)
            super().__init__(image, self.type)
            self.rect.y = 325

    class LargeCactus(Obstacle):
        def __init__(self, image):
            self.type = random.randint(0, 2)
            super().__init__(image, self.type)
            self.rect.y = 300

    class Bird(Obstacle):
        def __init__(self, image):
            self.type = 0
            super().__init__(image, self.type)
            self.rect.y = 250
            self.index = 0

        def draw(self, SCREEN):
            if self.index >= 9:
                self.index = 0
            SCREEN.blit(self.image[self.index//5], self.rect)
            self.index += 1
            


    def main():
        global game_speed, x_pos_bg, y_pos_bg, points, obstacles
        running = True
        clock = my_image.pygame.time.Clock()
        player = Dinosaur()
        cloud = Cloud()
        game_speed = 14
        x_pos_bg = 0
        y_pos_bg = 380
        points = 0
        font = my_image.pygame.font.Font('freesansbold.ttf', 20)
        obstacles = []
        death_count = 0

        def score():
            global points, game_speed
            points += 1
            if points % 100 == 0:
                game_speed += 1
            
            text = font.render("points: " + str(points), True, (0,0,0))
            textRect = text.get_rect()
            textRect.center = (1000, 40)
            SCREEN.blit(text, textRect)

        def background():
            global x_pos_bg, y_pos_bg
            image_width = my_image.BACKGROUND.get_width()
            SCREEN.blit(my_image.BACKGROUND, (x_pos_bg, y_pos_bg))
            SCREEN.blit(my_image.BACKGROUND, (image_width + x_pos_bg, y_pos_bg))

            if x_pos_bg <= -image_width:
                SCREEN.blit(my_image.BACKGROUND, (image_width + x_pos_bg, y_pos_bg))
                x_pos_bg = 0

            x_pos_bg -= game_speed

        while running:
            for event in my_image.pygame.event.get():
                if event.type == my_image.pygame.QUIT: # X 표시를 눌러 게임 종료 시 루프 탈출
                    running = False

            SCREEN.fill((255,255,255))
            userInput = my_image.pygame.key.get_pressed()

            player.draw(SCREEN)
            player.update(userInput)

            if len(obstacles) == 0:
                if random.randint(0, 2) == 0:
                    obstacles.append(SmallCactus(my_image.SMALL_CACTUS))
                elif random.randint(0, 2) == 1:
                    obstacles.append(LargeCactus(my_image.LARGE_CACTUS))
                elif random.randint(0, 2) == 2:
                    obstacles.append(Bird(my_image.BIRD))

            for obstacle in obstacles: # 리스트 요소를 반복한다.
                obstacle.draw(SCREEN)
                obstacle.update()
                if player.dino_rect.colliderect(obstacle.rect): #장애물에 부딫히면
                    my_image.pygame.time.delay(2000)
                    death_count += 1
                    menu(death_count)

            background()
            cloud.draw(SCREEN)
            cloud.update()

            score()


            clock.tick(30)
            my_image.pygame.display.update()

        my_image.pygame.quit()


    def menu(death_count):
        global points
        running = True

        while running:
            SCREEN.fill((255,255,255))
            font = my_image.pygame.font.Font('freesansbold.ttf', 30)

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
            SCREEN.blit(my_image.RUNNING[0], (SCREEN_WIDTH//2 - 20, SCREEN_HEIGHI // 2 - 140))
            my_image.pygame.display.update()

            for event in my_image.pygame.event.get():
                if event.type == my_image.pygame.QUIT: # X 표시를 눌러 게임 종료 시 루프 탈출
                    running = False
                    
                if event.type == my_image.pygame.KEYDOWN:
                    main()


    menu(death_count=0)
