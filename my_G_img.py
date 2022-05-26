import pygame
import os
import random

SCREEN_HEIGHI = 600
SCREEN_WIDTH = 1100

pygame.display.set_caption("Dinosaur Game")
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHI))

# 이미지 연결 애니메이션 사용
RUNNING = [pygame.image.load(os.path.join("Assets\Dino","DinoRun1.png")), 
pygame.image.load(os.path.join("Assets\Dino","DinoRun2.png"))]

JUMPING = pygame.image.load(os.path.join("Assets\Dino","DinoJump.png"))

DUCKING = [pygame.image.load(os.path.join("Assets\Dino","DinoDuck1.png")), 
pygame.image.load(os.path.join("Assets\Dino","DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets\Cactus","SmallCactus1.png")), 
pygame.image.load(os.path.join("Assets\Cactus","SmallCactus2.png")),
pygame.image.load(os.path.join("Assets\Cactus","SmallCactus3.png"))]

LARGE_CACTUS = [pygame.image.load(os.path.join("Assets\Cactus","LargeCactus1.png")), 
pygame.image.load(os.path.join("Assets\Cactus","LargeCactus2.png")),
pygame.image.load(os.path.join("Assets\Cactus","LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets\Bird", "Bird1.png")),
pygame.image.load(os.path.join("Assets\Bird","Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Assets\Other", "Cloud.png"))

BACKGROUND = pygame.image.load(os.path.join("Assets\Other", "Track.png"))