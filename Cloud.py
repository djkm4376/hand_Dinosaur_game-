import my_G_img

class Cloud():
    def __init__(self):
        self.x = my_G_img.SCREEN_WIDTH + my_G_img.random.randint(800 ,1000)
        self.y = my_G_img.random.randint(50, 100)
        self.image = my_G_img.CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= my_G_img.game_speed
        if self.x < -self.width:
            self.x = my_G_img.SCREEN_WIDTH + my_G_img.random.randint(2600, 3000)
            self.y = my_G_img.random.randint(50 ,100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
