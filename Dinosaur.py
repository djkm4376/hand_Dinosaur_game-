import my_G_img

class Dinosaur():
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        # 이미지 가져오기
        self.duck_img = my_G_img.DUCKING
        self.run_img = my_G_img.RUNNING
        self.jump_img = my_G_img.JUMPING

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
        if userInput[my_G_img.pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_jump = True
            self.dino_run = False
        elif userInput[my_G_img.pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
        elif not (self.dino_jump or userInput[my_G_img.pygame.K_DOWN]):
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