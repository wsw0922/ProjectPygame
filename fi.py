import sys
from cmath import rect
import os, random, math
from re import T
from re import X
from tkinter.messagebox import NO
from tkinter.tix import CELL
from turtle import position
import pygame
import time

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# python game with pygame : Jumping dino
# by. BlockDMask
# step1 : set screen, fps
# step2 : show dino, jump dino
# step3 : show tree, move treev

# <<<< 시작 화면 >>>>
# <<<< 시작 화면 >>>>
# <<<< 시작 화면 >>>>

pygame.init()
MAX_WIDTH = 800
MAX_HEIGHT = 600
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

in_sound = pygame.mixer.Sound(resource_path("sound/ogg/Tiny-Button-Push-Sound.ogg"))
login_sound = pygame.mixer.Sound(resource_path("sound/ogg/Coin-1.ogg"))
jump_sound = pygame.mixer.Sound(resource_path("sound/ogg/Jump-Low_1.ogg"))
ingame_sound = pygame.mixer.Sound(resource_path("sound/ogg/SellBuyMusic-뒤뚱뒤뚱.ogg"))
shoot_sound = pygame.mixer.Sound(resource_path("sound/ogg/Blop-Sound.ogg"))

current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, resource_path("backgroundstart.png")))

def main():

    fps = pygame.time.Clock()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                    time.sleep(0.3)
                    in_sound.play()
                    in_sound.set_volume(0.3)


        screen.blit(background, (0, 0))

        pygame.display.update()
        fps.tick(30)

if __name__ == '__main__':
    main()

pygame.time.delay(1000)
pygame.quit()

# <<<< 중간 화면 1 >>>>
# <<<< 중간 화면 1 >>>>
# <<<< 중간 화면 1 >>>>

pygame.init()

MAX_WIDTH = 800
MAX_HEIGHT = 500
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

current_path = os.path.dirname(__file__)
story01 = pygame.image.load(os.path.join(current_path, resource_path("news.png")))

start_ticks = pygame.time.get_ticks()

def main():

    fps = pygame.time.Clock()

    running = True
    while running:

        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
     
        screen.blit(story01, (0, 0))

        if elapsed_time > 3:
            running = False
        
    
        pygame.display.update()
        fps.tick(30)

if __name__ == '__main__':
    main()

pygame.time.delay(2000)
pygame.quit()

# 스크린 전체 크기 지정

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 672

# pygame 초기화

pygame.init()

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환

# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame Sprite")


# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

FPS = 60


background = pygame.image.load(resource_path('back1.png'))
cloud1 = pygame.image.load(resource_path("Cloud1.png"))
cloud2 = pygame.image.load(resource_path("Cloud2.png"))

class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, position):

        super(AnimatedSprite, self).__init__()

        # 이미지를 Rect안에 넣기 위해 Rect의 크기 지정
        # 이미지의 크기와 같게 하거나, 크기를 다르게 한다면 pygame.transform.scale을 사용하여 rect 안에
        # 이미지를 맞추도록 한다.
        size = (1440, 672)

        # 여러장의 이미지를 리스트로 저장한다. 이미지 경로는 자신들의 경로를 사용한다.
        images = []

        # 서있는 상태 1~10
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))

        # 걷기 11~20
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W2.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W2.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W2.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1.png"))))


        # 여러장의 이미지를 리스트로 저장한다. 이미지 경로는 자신들의 경로를 사용한다.
        images_2 = []

        # 서있는 상태 1~10
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))

        # 걷기 11~20
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W2.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W2.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W2.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))


        # rect 만들기
        self.rect = pygame.Rect(position, size)
        
        # Rect 크기와 Image 크기 맞추기. pygame.transform.scale
        self.images = [pygame.transform.scale(image, size) for image in images]

        # 원본 캐릭터 이미지들
        self.images_right = images
        self.images_left = images_2

        # 캐릭터의 현재 상태
        # 0 - idle 상태, 1 - 걷고 있는 상태
        self.state = 0
        # 방향
        self.direction = 'left'
        # 속도
        self.velocity_x = 0

        # 캐릭터의 첫번째 이미지
        self.index = 0
        self.image = images[self.index]

        # 1초에 보여줄 1장의 이미지 시간을 계산, 소수점 3자리까지 반올림
        self.animation_time = round(50 / len(self.images * 100), 2)

        # mt와 결합하여 animation_time을 계산할 시간 초기화
        self.current_time = 0

    def update(self, mt):
        # update를 통해 캐릭터의 이미지가 계속 반복해서 나타나도록 한다.

        # 현재 상태에 따라 반복해줄 이미지의 index 설정과 속도
        if self.state == 0:
            count = 10
            start_Index = 0
            self.velocity_x = 0
        elif self.state == 1:
            count = 10
            start_Index = 10
            self.velocity_x = 9

        # 방향이 오른쪽이면, 오른쪽 이미지 선택
        if self.direction == 'right':
            self.images = self.images_left
        # 방향이 왼쪽이면 왼쪽 이미지 선택, 진행방향 x축으로 -
        elif self.direction == 'left':
            self.images = self.images_right
            self.velocity_x = abs(self.velocity_x) * -1

        # loop 시간 더하기
        self.current_time += mt

        # loop time 경과가 animation_time을 넘어서면 새로운 이미지 출력 
        if self.current_time >= self.animation_time:
            self.current_time = 0

            # 상태에 따라 이미지 index 범위를 다르게 설정한다.

            # idle 상태는 1 ~ 2, 걷기 상태는 3 ~ 6
            self.index = (self.index % count) + start_Index

            self.image = self.images[self.index]
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0

        # 좌우 위치값 변경, 이동
        self.rect.x += self.velocity_x
        if self.rect.x < 90:
            self.rect.x = 90

        elif self.rect.x > 370:
            self.rect.x = 370
        global x 
        x = self.rect.x 
 
def main():

    # player 생성
    player = AnimatedSprite(position=(90, 300))
    # 생성된 player를 그룹에 넣기
    all_sprites = pygame.sprite.Group(player)  

    running = True
    while running:
            
        # 각 loop를 도는 시간. clock.tick()은 밀리초를 반환하므로
        # 1000을 나누어줘서 초단위로 변경한다.

        mt = clock.tick(60) / 3000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: 
                    player.direction = "right"
                    player.state = 1
                elif event.key == pygame.K_LEFT:
                    player.direction = "left"
                    player.state = 1
                elif event.key == pygame.K_SPACE:
                    if x > 135 and x < 165:
                        running = False
                        player.image = pygame.image.load(os.path.join(resource_path("solball3.png")))
                        login_sound.play()
                        login_sound.set_volume(0.3)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.velocity_x = 0
                    player.state = 0
    
        
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(cloud1, (0, 0))
        SCREEN.blit(cloud2, (0, 0))

        # all_sprites 그룹안에 든 모든 Sprite update
        all_sprites.update(mt)
        # 배경색
        
        # 모든 sprite 화면에 그려주기
        all_sprites.draw(SCREEN)

        
        pygame.display.update()
 

if __name__ == '__main__':
    main()

pygame.time.delay(1000) 

# <<<< 스토리 1 >>>>
# <<<< 스토리 1 >>>>
# <<<< 스토리 1 >>>>

pygame.init()

MAX_WIDTH = 800
MAX_HEIGHT = 500
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

current_path = os.path.dirname(__file__)
story01 = pygame.image.load(os.path.join(current_path, resource_path("s01.png")))
story02 = pygame.image.load(os.path.join(current_path, resource_path("s02.png")))
story03 = pygame.image.load(os.path.join(current_path, resource_path("s03.png")))
story04 = pygame.image.load(os.path.join(current_path, resource_path("s04.png")))
story05 = pygame.image.load(os.path.join(current_path, resource_path("s05.png")))
story06 = pygame.image.load(os.path.join(current_path, resource_path("s06.png")))
story07 = pygame.image.load(os.path.join(current_path, resource_path("s07.png")))
story08 = pygame.image.load(os.path.join(current_path, resource_path("s08.png")))

start_ticks = pygame.time.get_ticks()

def main():

    fps = pygame.time.Clock()

    running = True
    while running:

        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
     
        screen.blit(story01, (0, 0))

        if elapsed_time > 1.5:
            screen.blit(story02, (0, 0))
        if elapsed_time > 3:
            screen.blit(story03, (0, 0))
        if elapsed_time > 4.5:
            screen.blit(story04, (0, 0))
        if elapsed_time > 6:
            screen.blit(story05, (0, 0))
        if elapsed_time > 7.5:
            screen.blit(story06, (0, 0))
        if elapsed_time > 9:
            screen.blit(story07, (0, 0))
        if elapsed_time > 10.5:
            screen.blit(story08, (0, 0))
        if elapsed_time > 12:
            running = False
        
    
        pygame.display.update()
        fps.tick(30)

if __name__ == '__main__':
    main()

pygame.time.delay(2000)
pygame.quit()


# <<<< 공룡게임 >>>>
# <<<< 공룡게임 >>>>
# <<<< 공룡게임 >>>>


Success_Dino = True

while Success_Dino:

    pygame.init()
    MAX_WIDTH = 800
    MAX_HEIGHT = 400
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

    # 시간 설정
    total_time = 10
    start_ticks = pygame.time.get_ticks()

    
    # 배경 불러오기
    current_path = os.path.dirname(__file__)
    background = pygame.image.load(os.path.join(current_path, resource_path("b1.png")))

    def main():
        # set screen, fps
        fps = pygame.time.Clock()

        # dino
        imgDino1 = pygame.image.load(resource_path('sdino1_1.png')).convert_alpha()
        imgDino2 = pygame.image.load(resource_path('sdino2_2.png')).convert_alpha()
        dino_height = imgDino1.get_size()[1]
        dino_bottom = MAX_HEIGHT - dino_height
        dino_x = 50
        dino_y = dino_bottom
        jump_top = 200
        leg_swap = True
        is_bottom = True
        is_go_up = False

        # tree
        imgTree = pygame.image.load(resource_path('tree.png'))
        tree_height = imgTree.get_size()[1]
        tree_x = MAX_WIDTH
        tree_y = MAX_HEIGHT - tree_height

        running = True
        ingame_sound.play()
        ingame_sound.set_volume(0.3)
        while running:

            # event check
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    global Success_Dino # dino 루프 전역변수
                    Success_Dino = False 
                    pygame.quit()
                    sys.exit()
                    
                elif event.type == pygame.KEYDOWN:
                    jump_sound.play()
                    jump_sound.set_volume(0.3)
                    if is_bottom:
                        is_go_up = True
                        is_bottom = False

            # dino move
            if is_go_up:
                dino_y -= 11.0
            elif not is_go_up and not is_bottom:
                dino_y += 11.0

            # dino top and bottom check
            if is_go_up and dino_y <= jump_top:
                is_go_up = False

            if not is_bottom and dino_y >= dino_bottom:
                is_bottom = True
                dino_y = dino_bottom

            # tree move
            tree_x -= 14.0
            if tree_x <= 0:
                tree_x = MAX_WIDTH

            screen.blit(background, (0, 0))

            # draw tree
            screen.blit(imgTree, (tree_x, tree_y))

            # draw dino
            if leg_swap:
                screen.blit(imgDino1, (dino_x, dino_y))
                leg_swap = False
            else:
                screen.blit(imgDino2, (dino_x, dino_y))
                leg_swap = True

            # 충돌처리
            rect_dino = imgDino1.get_rect()
            rect_dino.left = dino_x
            rect_dino.top = dino_y

            rect_tree = imgTree.get_rect()
            rect_tree.left = tree_x
            rect_tree.top = tree_y

            if rect_dino.colliderect(rect_tree): 
                Success_Dino = True
                global Success_Bubble # bubble 루프
                Success_Bubble = False
                running = False
                    
            # 시간 초과        
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

            if total_time - elapsed_time <= 0:
                Success_Dino = False
                Success_Bubble = True
                running = False


            # update
            pygame.display.update()
            fps.tick(30)

    if __name__ == '__main__':
        main()

    pygame.time.delay(2000)
    pygame.quit()


# 스크린 전체 크기 지정

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 672


# pygame 초기화

pygame.init()

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환

# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame Sprite")

 

# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

FPS = 60


# <<<< 중간 화면 2 >>>>
# <<<< 중간 화면 2 >>>>
# <<<< 중간 화면 2 >>>>


# 스크린 전체 크기 지정

i = 255
m = 0


SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 672

# pygame 초기화

pygame.init()

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환

# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame Sprite")

# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

FPS = 60

# 이미지 불러오기
background = pygame.image.load(resource_path('back1.png'))
cloud1 = pygame.image.load(resource_path("Cloud1.png"))
cloud2 = pygame.image.load(resource_path("Cloud2.png"))

# 구름 이미지 rect
cloud2_Rect = cloud2.get_rect()

class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, position):

        super(AnimatedSprite, self).__init__()

        # 이미지를 Rect안에 넣기 위해 Rect의 크기 지정
        # 이미지의 크기와 같게 하거나, 크기를 다르게 한다면 pygame.transform.scale을 사용하여 rect 안에
        # 이미지를 맞추도록 한다.
        size = (1440, 672)

        # 여러장의 이미지를 리스트로 저장한다. 이미지 경로는 자신들의 경로를 사용한다.
        images = []

        # 서있는 상태 1~10
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))

        # 걷기 11~20
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W2.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W2.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W2.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1.png"))))


        # 여러장의 이미지를 리스트로 저장한다. 이미지 경로는 자신들의 경로를 사용한다.
        images_2 = []

        # 서있는 상태 1~10
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))

        # 걷기 11~20
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W2.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W2.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W2.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))


        # rect 만들기
        self.rect = pygame.Rect(position, size)

        # Rect 크기와 Image 크기 맞추기. pygame.transform.scale
        self.images = [pygame.transform.scale(image, size) for image in images]

        # 원본 캐릭터 이미지들
        self.images_right = images
        self.images_left = images_2

        # 캐릭터의 현재 상태
        # 0 - idle 상태, 1 - 걷고 있는 상태
        self.state = 0
        # 방향
        self.direction = 'left'
        # 속도
        self.velocity_x = 0

        # 캐릭터의 첫번째 이미지
        self.index = 0
        self.image = images[self.index]

        # 1초에 보여줄 1장의 이미지 시간을 계산, 소수점 3자리까지 반올림
        self.animation_time = round(50 / len(self.images * 100), 2)

        # mt와 결합하여 animation_time을 계산할 시간 초기화
        self.current_time = 0

    def update(self, mt):
        # update를 통해 캐릭터의 이미지가 계속 반복해서 나타나도록 한다.

        # 현재 상태에 따라 반복해줄 이미지의 index 설정과 속도
        if self.state == 0:
            count = 10
            start_Index = 0
            self.velocity_x = 0
        elif self.state == 1:
            count = 10
            start_Index = 10
            self.velocity_x = 9

        # 방향이 오른쪽이면, 오른쪽 이미지 선택
        if self.direction == 'right':
            self.images = self.images_left
        # 방향이 왼쪽이면 왼쪽 이미지 선택, 진행방향 x축으로 -
        elif self.direction == 'left':
            self.images = self.images_right
            self.velocity_x = abs(self.velocity_x) * -1
 
        # loop 시간 더하기
        self.current_time += mt

        # loop time 경과가 animation_time을 넘어서면 새로운 이미지 출력 
        if self.current_time >= self.animation_time:
            self.current_time = 0

            # 상태에 따라 이미지 index 범위를 다르게 설정한다.

            # idle 상태는 1 ~ 2, 걷기 상태는 3 ~ 6
            self.index = (self.index % count) + start_Index

            self.image = self.images[self.index]
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0

        # 좌우 위치값 변경, 이동
        self.rect.x += self.velocity_x
        if self.rect.x < 150:
            self.rect.x = 150

        elif self.rect.x > 790:
            self.rect.x = 790
        global x 
        x = self.rect.x

def main():

    # player 생성
    player = AnimatedSprite(position=(150, 300))
    # 생성된 player를 그룹에 넣기
    all_sprites = pygame.sprite.Group(player)  

    running = True
    while running:
            
        # 각 loop를 도는 시간. clock.tick()은 밀리초를 반환하므로
        # 1000을 나누어줘서 초단위로 변경한다.

        mt = clock.tick(60) / 5000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: 
                    player.direction = "right"
                    player.state = 1
                elif event.key == pygame.K_LEFT:
                    player.direction = "left"
                    player.state = 1
                elif event.key == pygame.K_SPACE:
                    if x > 668 and x < 697:
                        player.image = pygame.image.load(os.path.join(resource_path("solball3.png")))
                        running = False
                        login_sound.play()
                        login_sound.set_volume(0.3)


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.velocity_x = 0
                    player.state = 0
                    

        global m
        m += 1

        if m > 20:
            cloud2_Rect.x += 4

            if cloud2_Rect.x > SCREEN_WIDTH:
                cloud2_Rect.x = SCREEN_WIDTH

            global i
            i -= 6
            cloud2.set_alpha(i)

            if i < 0:
                i = 0


        if cloud2_Rect.x > SCREEN_WIDTH:
            cloud2_Rect.x = SCREEN_WIDTH
        
        SCREEN.blit(background, (0, 0)) 
        SCREEN.blit(cloud1, (0, 0))
        SCREEN.blit(cloud2, cloud2_Rect)

        # all_sprites 그룹안에 든 모든 Sprite update
        all_sprites.update(mt)
        # 배경색
        
        # 모든 sprite 화면에 그려주기
        all_sprites.draw(SCREEN)

        pygame.display.update()
 
if __name__ == '__main__':
    main()

pygame.time.delay(1000) 

# <<<< 스토리 1 >>>>
# <<<< 스토리 1 >>>>
# <<<< 스토리 1 >>>>

pygame.init()

MAX_WIDTH = 800
MAX_HEIGHT = 500
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

current_path = os.path.dirname(__file__)
story01 = pygame.image.load(os.path.join(current_path, resource_path("s10.png")))
story02 = pygame.image.load(os.path.join(current_path, resource_path("s11.png")))
story03 = pygame.image.load(os.path.join(current_path, resource_path("s12.png")))
story04 = pygame.image.load(os.path.join(current_path, resource_path("s13.png")))
story05 = pygame.image.load(os.path.join(current_path, resource_path("s14.png")))
story06 = pygame.image.load(os.path.join(current_path, resource_path("s15.png")))
story07 = pygame.image.load(os.path.join(current_path, resource_path("s16.png")))


start_ticks = pygame.time.get_ticks()

def main():

    fps = pygame.time.Clock()

    running = True
    while running:

        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
     
        screen.blit(story01, (0, 0))

        if elapsed_time > 1.5:
            screen.blit(story02, (0, 0))
        if elapsed_time > 3:
            screen.blit(story03, (0, 0))
        if elapsed_time > 4.5:
            screen.blit(story04, (0, 0))
        if elapsed_time > 6:
            screen.blit(story05, (0, 0))
        if elapsed_time > 7.5:
            screen.blit(story06, (0, 0))
        if elapsed_time > 9:
            screen.blit(story07, (0, 0))
        if elapsed_time > 10.5:
            running = False
        
    
        pygame.display.update()
        fps.tick(30)

if __name__ == '__main__':
    main()

pygame.time.delay(2000)
pygame.quit()

# <<<< 버블슈터 >>>>
# <<<< 버블슈터 >>>>
# <<<< 버블슈터 >>>>


if Success_Bubble:

    while Success_Bubble:

        class Bubble(pygame.sprite.Sprite):
            def __init__(self, image, color, position=(0,0), row_idx=-1, col_idx=-1):
                super().__init__()
                self.image = image
                self.color = color
                self.rect = image.get_rect(center=position)
                self.radius = 18
                self.row_idx = row_idx
                self.col_idx = col_idx

            def set_rect(self, position):
                self.rect = self.image.get_rect(center=position)

            def draw(self, screen, to_x=None):
                if to_x:
                    screen.blit(self.image, (self.rect.x + to_x, self.rect.y))
                else: screen.blit(self.image, self.rect)

            def set_angle(self, angle):
                self.angle = angle
                self.rad_angle = math.radians(self.angle)

            def move(self):
                to_x = self.radius * math.cos(self.rad_angle)
                to_y = self.radius * math.sin(self.rad_angle) * -1

                self.rect.x += to_x
                self.rect.y += to_y
        
                if self.rect.left < 0 or self.rect.right > screen_width:
                    self.set_angle(180 - self.angle)

            def set_map_index(self, row_idx, col_idx):
                self.row_idx = row_idx
                self.col_idx = col_idx

            def drop_downward(self, height):
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery + height))

        # 발사대 클래스 생성
        class Pointer(pygame.sprite.Sprite):
            def __init__(self, image, position, angle):
                super().__init__()
                self.image = image
                self.rect = image.get_rect(center=position)
                self.angle = angle
                self.original_image = image
                self.position = position

            def draw(self, screen):
                screen.blit(self.image, self.rect)

            # 회전
            def rotate(self, angle):
                self.angle += angle

                if self.angle > 170:
                    self.angle = 170
                elif self.angle < 10:
                    self.angle = 10

                self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
                self.rect = self.image.get_rect(center=self.position)

        # 맵 만들기
        def setup():
            global map
            map = [
                # ["R", "R", "Y", "Y", "B", "B", "G", "G"],
                list("RRYYBBGG"),
                list("RRYYBBG/"), # / : 버블이 위치할 수 없는 곳
                list("BBGGRRYY"),
                list("BGGRRYY/"),
                list("........"), # . : 비어 있는 곳
                list("......./"),
                list("........"),
                list("......./"),
                list("........"),
                list("......./"),
                list("........")        
            ]

            for row_idx, row in enumerate(map):
                for col_idx, col in enumerate(row):
                    if col in [".", "/"]:
                        continue
                    position = get_bubble_position(row_idx, col_idx)
                    image = get_bubble_image(col)
                    bubble_group.add(Bubble(image, col, position, row_idx, col_idx))
            
        def get_bubble_position(row_idx, col_idx):
            pos_x = col_idx * CELL_SIZE + (BUBBLE_WIDTH // 2)
            pos_y = row_idx * CELL_SIZE + (BUBBLE_HEIGHT // 2) + wall_height
            if row_idx % 2 == 1:
                pos_x += CELL_SIZE // 2
            return pos_x, pos_y

        def get_bubble_image(color):
            if color == "R":
                return bubble_images[0]
            elif color == "Y":
                return bubble_images[1]
            elif color == "B":
                return bubble_images[2]
            elif color == "G":
                return bubble_images[3]
            elif color == "P":
                return bubble_images[4]
            else: # BLACK
                return bubble_images[-1]

        def prepare_bubbles():
            global curr_bubble, next_bubble
            if next_bubble:
                curr_bubble = next_bubble
            else:
                curr_bubble = create_bubble() # 새 버블 만들기

            curr_bubble.set_rect((screen_width // 2, 624))
            next_bubble = create_bubble()
            next_bubble.set_rect((screen_width // 4, 688))

        def create_bubble():
            color = get_random_bubble_color()
            image = get_bubble_image(color)
            return Bubble(image, color)

        def get_random_bubble_color():
            colors = []
            for row in map:
                for col in row:
                    if col not in colors and col not in [".", "/"]:
                        colors.append(col)
            return random.choice(colors)

        def process_collision():
            global curr_bubble, fire, curr_fire_count
            hit_bubble = pygame.sprite.spritecollideany(curr_bubble, bubble_group, pygame.sprite.collide_mask)
            if hit_bubble or curr_bubble.rect.top <= wall_height:
                row_idx, col_idx = get_map_index(*curr_bubble.rect.center) # (x, y)
                place_bubble(curr_bubble, row_idx, col_idx)
                remove_adjacent_bubbles(row_idx, col_idx, curr_bubble.color)
                curr_bubble = None
                fire = False
                curr_fire_count -= 1

        def get_map_index(x, y):
            row_idx = (y - wall_height) // CELL_SIZE
            col_idx = x // CELL_SIZE
            if row_idx % 2 == 1:
                col_idx = (x - (CELL_SIZE // 2)) // CELL_SIZE
                if col_idx < 0:
                    col_idx = 0
                elif col_idx > MAP_COLUMN_COUNT - 2:
                    col_idx = MAP_COLUMN_COUNT - 2 

            return row_idx, col_idx

        def place_bubble(bubble, row_idx, col_idx):
            map[row_idx][col_idx] = bubble.color
            position = get_bubble_position(row_idx, col_idx)
            bubble.set_rect(position)
            bubble.set_map_index(row_idx, col_idx)
            bubble_group.add(bubble)

        def remove_adjacent_bubbles(row_idx, col_idx, color):
            visited.clear()
            visit(row_idx, col_idx, color)
            if len(visited) >= 3:
                remove_visited_bubbles()
                remove_hanging_bubbles()

        def visit(row_idx, col_idx, color=None):
            # 맵의 범위를 벗어나는지 확인
            if row_idx < 0 or row_idx >= MAP_ROW_COUNT or col_idx < 0 or col_idx >= MAP_COLUMN_COUNT:
                return 
            # 현재 셀의 색상이 컬러와 같은지 확인
            if color and map[row_idx][col_idx] != color:
                return
            # 빈 공간이거나 버블이 존재할 수 없는 위치인지 확인
            if map[row_idx][col_idx] in [".", "/"]:
                return
            # 이미 방문했는지 여부 확인
            if (row_idx, col_idx) in visited:
                return
            # 방문 처리
            visited.append((row_idx, col_idx))

            rows = [0, -1, -1, 0, 1, 1]
            cols = [-1, -1, 0 ,1, 0, -1]
            if row_idx % 2 == 1:
                rows = [0, -1, -1, 0, 1, 1]
                cols = [-1, 0, 1, 1, 1, 0]

            for i in range(len(rows)):
                visit(row_idx + rows[i], col_idx + cols[i], color)

        def remove_visited_bubbles():
            bubbles_to_remove = [b for b in bubble_group if (b.row_idx, b.col_idx) in visited]
            for bubble in bubbles_to_remove:
                map[bubble.row_idx][bubble.col_idx] = "."
                bubble_group.remove(bubble)

        def remove_not_visited_bubbles():
            bubbles_to_remove = [b for b in bubble_group if (b.row_idx, b.col_idx) not in visited]
            for bubble in bubbles_to_remove:
                map[bubble.row_idx][bubble.col_idx] = "."
                bubble_group.remove(bubble)

        def remove_hanging_bubbles():
            visited.clear()
            for col_idx in range(MAP_COLUMN_COUNT):
                if map[0][col_idx] != ".":
                    visit(0, col_idx)

            remove_not_visited_bubbles()

        def draw_bubbles():
            to_x = None
            if curr_fire_count == 2:
                to_x = random.randint(0, 2) - 1 # -1 ~ 1
            elif curr_fire_count == 1:
                to_x = random.randint(0, 8) - 4 # -4 ~ 4

            for bubble in bubble_group:
                bubble.draw(screen, to_x)

        def drop_wall():
            global wall_height, curr_fire_count
            wall_height += CELL_SIZE
            for bubble in bubble_group:
                bubble.drop_downward(CELL_SIZE)
            curr_fire_count = FIRE_COUNT

        def get_lowest_bubble_bottom():
            bubble_bottoms = [bubble.rect.bottom for bubble in bubble_group]
            return max(bubble_bottoms)

        def change_bubble_image(image):
            for bubble in bubble_group:
                bubble.image = image

        def display_game_over():
            txt_game_over = game_font.render(game_result, True, WHITE)
            rect_game_over = txt_game_over.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(txt_game_over, rect_game_over)

        pygame.init()
        screen_width = 448
        screen_height = 720
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Puzzle Bobble")
        clock = pygame.time.Clock()
        ingame_sound.play()

        # 배경 이미지 불러오기
        current_path = os.path.dirname(__file__)
        background = pygame.image.load(os.path.join(current_path, resource_path("background1.png")))
        # 벽 이미지 불러오기
        wall = pygame.image.load(os.path.join(current_path, resource_path("wall.png")))

        # 버블 이미지 불러오기
        bubble_images = [
            pygame.image.load(os.path.join(current_path, resource_path("red.png"))).convert_alpha(),
            pygame.image.load(os.path.join(current_path, resource_path("yellow.png"))).convert_alpha(),
            pygame.image.load(os.path.join(current_path, resource_path("blue.png"))).convert_alpha(),
            pygame.image.load(os.path.join(current_path, resource_path("green.png"))).convert_alpha(),
            pygame.image.load(os.path.join(current_path, resource_path("purple.png"))).convert_alpha(),
            pygame.image.load(os.path.join(current_path, resource_path("black.png"))).convert_alpha()
        ]

        # 발사대 이미지 불러오기
        pointer_image = pygame.image.load(os.path.join(current_path, resource_path("pointer.png")))
        pointer = Pointer(pointer_image, (screen_width // 2, 624), 90)

        # 게임 관련 변수
        CELL_SIZE = 56
        BUBBLE_WIDTH = 56
        BUBBLE_HEIGHT = 62
        RED = (255,0,0)
        WHITE = (255, 255, 255)
        MAP_ROW_COUNT = 11
        MAP_COLUMN_COUNT = 8
        FIRE_COUNT = 7

        # 화살표 관련 변수
        # to_angle = 0 # 좌우로 움직일 각도 정보
        to_angle_left = 0 # 왼쪽으로 움직일 각도 정보
        to_angle_right = 0 # 오른쪽으로 움직일 각도 정보
        angle_speed = 1.5 # 1.5 도씩 움직이게 됨

        curr_bubble = None # 이번에 쏠 버블
        next_bubble = None # 다음에 쏠 버블
        fire = False # 발사 여부
        curr_fire_count = FIRE_COUNT
        wall_height = 0 # 화면에 보여지는 벽의 높이

        is_game_over = False
        game_font = pygame.font.SysFont("arialrounded", 48)
        game_result = None

        map = [] # 맵
        visited = [] # 방문 위치 기록
        bubble_group = pygame.sprite.Group()
        setup()

        running = True
        while running:
            clock.tick(60) # FPS 60 으로 설정

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        to_angle_left += angle_speed
                    elif event.key == pygame.K_RIGHT:
                        to_angle_right -= angle_speed
                    elif event.key == pygame.K_SPACE:
                        shoot_sound.play()
                        shoot_sound.set_volume(0.3)
                        if curr_bubble and not fire:
                            fire = True
                            curr_bubble.set_angle(pointer.angle)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        to_angle_left = 0
                    elif event.key == pygame.K_RIGHT:
                        to_angle_right = 0

            if not curr_bubble:
                prepare_bubbles()

            if fire:
                process_collision() # 충돌 처리

            if curr_fire_count == 0:
                drop_wall()

            if not bubble_group:
                game_result = "Mission Complete"
                Success_Bubble = False
                global Success_Monster # 공뽀개기 루프
                Success_Monster = True
                is_game_over = True
            elif get_lowest_bubble_bottom() > len(map) * CELL_SIZE:
                game_result = "Game Over"
                Success_Bubble = True
                Success_Monster = False
                is_game_over = True
                change_bubble_image(bubble_images[-1])

            screen.blit(background, (0, 0))
            screen.blit(wall, (0, wall_height - screen_height))

            draw_bubbles()
            pointer.rotate(to_angle_left + to_angle_right)
            pointer.draw(screen)    
            if curr_bubble:
                if fire:
                    curr_bubble.move()
                curr_bubble.draw(screen) 


            if next_bubble:
                next_bubble.draw(screen)

            if is_game_over:
                display_game_over()
                running =  False
                    
            pygame.display.update()

        pygame.time.delay(2000)
        pygame.quit()


# <<<< 중간 화면 3 >>>>
# <<<< 중간 화면 3 >>>>
# <<<< 중간 화면 3 >>>>

# 스크린 전체 크기 지정

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 672

 

# pygame 초기화

pygame.init()

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환

# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame Sprite")

 

# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

FPS = 60

 
i = 255
m = 0

# 이미지 불러오기
background = pygame.image.load(resource_path('back1.png'))
cloud1 = pygame.image.load(resource_path("Cloud1.png"))


# 구름 이미지 rect
cloud1_Rect = cloud1.get_rect()



class AnimatedSprite(pygame.sprite.Sprite):

 

    def __init__(self, position):

        super(AnimatedSprite, self).__init__()

 

        # 이미지를 Rect안에 넣기 위해 Rect의 크기 지정
        # 이미지의 크기와 같게 하거나, 크기를 다르게 한다면 pygame.transform.scale을 사용하여 rect 안에
        # 이미지를 맞추도록 한다.
        size = (1440, 672)

 

        # 여러장의 이미지를 리스트로 저장한다. 이미지 경로는 자신들의 경로를 사용한다.
        images = []

        # 서있는 상태 1~10
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))

        # 걷기 11~20
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W2.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W2.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1_W2.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1.png"))))
        images.append(pygame.image.load(os.path.join(resource_path("solball1.png"))))


        # 여러장의 이미지를 리스트로 저장한다. 이미지 경로는 자신들의 경로를 사용한다.
        images_2 = []

        # 서있는 상태 1~10
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard_1.png"))))

        # 걷기 11~20
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W1.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W2.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W2.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_W2.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))
        images_2.append(pygame.image.load(os.path.join(resource_path("solball2_standard.png"))))


        # rect 만들기
        self.rect = pygame.Rect(position, size)
        


        # Rect 크기와 Image 크기 맞추기. pygame.transform.scale
        self.images = [pygame.transform.scale(image, size) for image in images]

 

        # 원본 캐릭터 이미지들
        self.images_right = images
        self.images_left = images_2


        # 캐릭터의 현재 상태
        # 0 - idle 상태, 1 - 걷고 있는 상태
        self.state = 0
        # 방향
        self.direction = 'left'
        # 속도
        self.velocity_x = 0

 

        # 캐릭터의 첫번째 이미지
        self.index = 0
        self.image = images[self.index]

 

        # 1초에 보여줄 1장의 이미지 시간을 계산, 소수점 3자리까지 반올림
        self.animation_time = round(50 / len(self.images * 100), 2)

        # mt와 결합하여 animation_time을 계산할 시간 초기화
        self.current_time = 0


    def update(self, mt):
        # update를 통해 캐릭터의 이미지가 계속 반복해서 나타나도록 한다.

       

        # 현재 상태에 따라 반복해줄 이미지의 index 설정과 속도
        if self.state == 0:
            count = 10
            start_Index = 0
            self.velocity_x = 0
        elif self.state == 1:
            count = 10
            start_Index = 10
            self.velocity_x = 6

 

        # 방향이 오른쪽이면, 오른쪽 이미지 선택
        if self.direction == 'right':
            self.images = self.images_left
        # 방향이 왼쪽이면 왼쪽 이미지 선택, 진행방향 x축으로 -
        elif self.direction == 'left':
            self.images = self.images_right
            self.velocity_x = abs(self.velocity_x) * -1
 

        # loop 시간 더하기
        self.current_time += mt


        # loop time 경과가 animation_time을 넘어서면 새로운 이미지 출력 
        if self.current_time >= self.animation_time:
            self.current_time = 0


            # 상태에 따라 이미지 index 범위를 다르게 설정한다.

            # idle 상태는 1 ~ 2, 걷기 상태는 3 ~ 6
            self.index = (self.index % count) + start_Index

           

            self.image = self.images[self.index]
            self.index += 1


            if self.index >= len(self.images):
                self.index = 0

           

        # 좌우 위치값 변경, 이동
        self.rect.x += self.velocity_x
        
        if self.rect.x < 682:
            self.rect.x = 682

        elif self.rect.x > 1320:
            self.rect.x = 1320
        global x 
        x = self.rect.x
 

def main():

    # player 생성
    player = AnimatedSprite(position=(682, 300))
    # 생성된 player를 그룹에 넣기
    all_sprites = pygame.sprite.Group(player)  

    
    
    running = True
    while running:
            
 

        # 각 loop를 도는 시간. clock.tick()은 밀리초를 반환하므로
        # 1000을 나누어줘서 초단위로 변경한다.

        mt = clock.tick(60) / 5000
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: 
                    player.direction = "right"
                    player.state = 1
                elif event.key == pygame.K_LEFT:
                    player.direction = "left"
                    player.state = 1
                elif event.key == pygame.K_SPACE:
                    if x > 1230 and  x < 1260:
                        player.image = pygame.image.load(os.path.join(resource_path("solball3.png")))
                        running = False
                        login_sound.play()
                        login_sound.set_volume(0.3)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.velocity_x = 0
                    player.state = 0
                    
        global m
        m += 1
    
        if m > 20:
            cloud1_Rect.x += 4

            if cloud1_Rect.x > SCREEN_WIDTH:
                cloud1_Rect.x = SCREEN_WIDTH
            

            global i
            i -= 6
            cloud1.set_alpha(i)
            if i < 0:
                i = 0


        SCREEN.blit(background, (0, 0)) 
        SCREEN.blit(cloud1, cloud1_Rect)



        # all_sprites 그룹안에 든 모든 Sprite update
        all_sprites.update(mt)
        # 배경색
        
        # 모든 sprite 화면에 그려주기
        all_sprites.draw(SCREEN)

        
        pygame.display.update()

if __name__ == '__main__':
    main()

pygame.time.delay(1000) 


# <<<< Moster Shooting >>>>
# <<<< Moster Shooting >>>>
# <<<< Moster Shooting >>>>

if Success_Monster:
    
    while Success_Monster:
 
        # 기본 초기화 (반드시 해야 하는 것들)
        pygame.init()

        # 화면 크기 설정
        screen_width = 800 # 가로 크기
        screen_height = 500 # 세로 크기
        screen = pygame.display.set_mode((screen_width, screen_height))

        # 화면 타이틀 설정
        pygame.display.set_caption("Monster Shooting")

        # FPS
        clock = pygame.time.Clock()
        ##############################################################

        # 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
        current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
    
        # 배경 만들기
        background = pygame.image.load(os.path.join(resource_path("m.background_2.png")))

        # 스테이지 만들기
        stage = pygame.image.load(os.path.join(resource_path("m.stage_2.png")))
        stage_size = stage.get_rect().size
        stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

        # 캐릭터 만들기
        character = pygame.image.load(os.path.join(resource_path("solball1_78.png")))
        character_size = character.get_rect().size
        character_width = character_size[0]
        character_height = character_size[1]
        character_x_pos = (screen_width / 2) - (character_width / 2)
        character_y_pos = screen_height - character_height - stage_height

        # 캐릭터 이동 방향
        character_to_x = 0

        # 캐릭터 이동 속도
        character_speed = 3.5

        # 무기 만들기
        weapon = pygame.image.load(os.path.join(resource_path("arrow_2_70.png")))
        weapon_size = weapon.get_rect().size
        weapon_width = weapon_size[0]

        # 무기는 한 번에 여러 발 발사 가능, 그러나 딜레이 추가
        weapons = []

        # 무기 이동 속도
        weapon_speed = 10

        # 공 만들기 (4개 크기에 대해 따로 처리)
        ball_images = [
            pygame.image.load(os.path.join(resource_path("spider1_2.png"))),
            pygame.image.load(os.path.join(resource_path("spider2.png"))),
            pygame.image.load(os.path.join(resource_path("spider3.png"))),
            pygame.image.load(os.path.join(resource_path("spider4.png")))]

        # 공 크기에 따른 최초 스피드
        ball_speed_y = [-14, -12.5, -11, -9] # index 0, 1, 2, 3 에 해당하는 값

        # 공들
        balls = []

        # 최초 발생하는 큰 공 추가
        balls.append({
            "pos_x" : random.randrange(0, 700), # 공의 랜덤 x 좌표
            "pos_y" : random.randrange(0, 150), # 공의 랜덤 y 좌표
            "img_idx" : 0, # 공의 이미지 인덱스
            "to_x": 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
            "to_y": -6, # y축 이동방향,
            "init_spd_y": ball_speed_y[0]})# y 최초 속도

        # 사라질 무기, 공 정보 저장 변수
        weapon_to_remove = -1
        ball_to_remove = -1

        # Font 정의
        game_font = pygame.font.SysFont("arial", 40)
        total_time = 80
        start_ticks = pygame.time.get_ticks() # 시작 시간 정의

        # 게임 종료 메시지 
        # Time Over(시간 초과 실패)
        # Mission Complete(성공)
        # Game Over (캐릭터 공에 맞음, 실패)
        game_result = "Game Over"

        leg_swap = True
        i = 0
        running = True
        ingame_sound.play()
        while running:
            dt = clock.tick(60)
            
            # 경과 시간 계산
            global elapsed_time
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s
            timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255, 255, 255))
            

            # 시간 초과했다면
            if total_time - elapsed_time <= 0:
                game_result = "Time Over"
                running = False


            # 2. 이벤트 처리 (키보드, 마우스 등)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                        i = 1
                        character_to_x -= character_speed
                    elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                        i = 2
                        character_to_x += character_speed
                    elif event.key == pygame.K_SPACE: # 무기 발사
                        shoot_sound.play()
                        shoot_sound.set_volume(0.3)
                        i = 3
                        character = pygame.image.load(os.path.join(resource_path("solball3_78.png")))
                        weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                        weapon_y_pos = character_y_pos
                        weapons.append([weapon_x_pos, weapon_y_pos])

                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        character_to_x = 0
                    i = 0
                    
            t = elapsed_time % 2
            if i == 1:
                if t < 0.25 or t >= 0.5 and t < 0.75 or t >= 1.0 and t < 1.25 or t >= 1.5 and t < 1.75:
                    character = pygame.image.load(os.path.join(resource_path("solball1_W1_78.png")))
                else:
                    character = pygame.image.load(os.path.join(resource_path("solball1_W2_78.png")))
            if i == 2:
                if t < 0.25 or t >= 0.5 and t < 0.75 or t >= 1.0 and t < 1.25 or t >= 1.5 and t < 1.75:
                    character = pygame.image.load(os.path.join(resource_path("solball2_W1_78.png")))
                else:
                    character = pygame.image.load(os.path.join(resource_path("solball2_W2_78.png")))
            
            # 3. 게임 캐릭터 위치 정의
            character_x_pos += character_to_x

            if character_x_pos < 0:
                character_x_pos = 0
            elif character_x_pos > screen_width - character_width:
                character_x_pos = screen_width - character_width

            # 무기 위치 조정
            # 100, 200 -> 180, 160, 140, ...
            # 500, 200 -> 180, 160, 140, ...
            weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로

            # 천장에 닿은 무기 없애기
            weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]
            
            # 공 위치 정의
            for ball_idx, ball_val in enumerate(balls):
                ball_pos_x = ball_val["pos_x"]
                ball_pos_y = ball_val["pos_y"]
                ball_img_idx = ball_val["img_idx"]

                ball_size = ball_images[ball_img_idx].get_rect().size
                ball_width = ball_size[0]
                ball_height = ball_size[1]

                # 가로벽에 닿았을 때 공 이동 위치 변경 (튕겨 나오는 효과)
                if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
                    ball_val["to_x"] = ball_val["to_x"] * -1

                # 세로 위치
                # 스테이지에 튕겨서 올라가는 처리
                if ball_pos_y >= screen_height - stage_height - ball_height:
                    ball_val["to_y"] = ball_val["init_spd_y"]
                else: # 그 외의 모든 경우에는 속도를 증가
                    ball_val["to_y"] += 0.35

                ball_val["pos_x"] += ball_val["to_x"]
                ball_val["pos_y"] += ball_val["to_y"]

            # 4. 충돌 처리

            # 캐릭터 rect 정보 업데이트
            character_rect = character.get_rect()
            character_rect.left = character_x_pos
            character_rect.top = character_y_pos

            for ball_idx, ball_val in enumerate(balls):
                ball_pos_x = ball_val["pos_x"]
                ball_pos_y = ball_val["pos_y"]
                ball_img_idx = ball_val["img_idx"]

                # 공 rect 정보 업데이트
                ball_rect = ball_images[ball_img_idx].get_rect()
                ball_rect.left = ball_pos_x
                ball_rect.top = ball_pos_y

                # 공과 캐릭터 충돌 체크
                if character_rect.colliderect(ball_rect):
                    running = False
                    break

                # 공과 무기들 충돌 처리
                for weapon_idx, weapon_val in enumerate(weapons):
                    weapon_pos_x = weapon_val[0]
                    weapon_pos_y = weapon_val[1]

                    # 무기 rect 정보 업데이트
                    weapon_rect = weapon.get_rect()
                    weapon_rect.left = weapon_pos_x
                    weapon_rect.top = weapon_pos_y

                    # 충돌 체크
                    if weapon_rect.colliderect(ball_rect):
                        weapon_to_remove = weapon_idx # 해당 무기 없애기 위한 값 설정
                        ball_to_remove = ball_idx # 해당 공 없애기 위한 값 설정

                        # 가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
                        if ball_img_idx < 3:
                            # 현재 공 크기 정보를 가지고 옴
                            ball_width = ball_rect.size[0]
                            ball_height = ball_rect.size[1]

                            # 나눠진 공 정보
                            small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                            small_ball_width = small_ball_rect.size[0]
                            small_ball_height = small_ball_rect.size[1]

                            # 왼쪽으로 튕겨나가는 작은 공
                            balls.append({
                                "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
                                "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y 좌표
                                "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스
                                "to_x": -3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
                                "to_y": -6, # y축 이동방향,
                                "init_spd_y": ball_speed_y[ball_img_idx + 1]})# y 최초 속도

                            # 오른쪽으로 튕겨나가는 작은 공
                            balls.append({
                                "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
                                "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2), # 공의 y 좌표
                                "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스
                                "to_x": 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
                                "to_y": -6, # y축 이동방향,
                                "init_spd_y": ball_speed_y[ball_img_idx + 1]})# y 최초 속도

                        break
                else: # 계속 게임을 진행
                    continue # 안쪽 for 문 조건이 맞지 않으면 continue. 바깥 for 문 계속 수행
                break # 안쪽 for 문에서 break 를 만나면 여기로 진입 가능. 2중 for 문을 한번에 탈출

            # for 바깥조건:
            #     바깥동작
            #     for 안쪽조건:
            #         안쪽동작
            #         if 충돌하면:
            #             break
            #     else:
            #         continue
            #     break

            # 충돌된 공 or 무기 없애기
            if ball_to_remove > -1:
                del balls[ball_to_remove]
                ball_to_remove = -1

            if weapon_to_remove > -1:
                del weapons[weapon_to_remove]
                weapon_to_remove = -1

            # 모든 공을 없앤 경우 게임 종료 (성공)
            if len(balls) == 0:
                game_result = "Mission Complete"
                running = False
                Success_Monster = False
                Success_end = True

            # 5. 화면에 그리기
            screen.blit(background, (0, 0))
            
            for weapon_x_pos, weapon_y_pos in weapons:
                screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

            for idx, val in enumerate(balls):
                ball_pos_x = val["pos_x"]
                ball_pos_y = val["pos_y"]
                ball_img_idx = val["img_idx"]
                screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

            screen.blit(stage, (0, screen_height - stage_height))
            screen.blit(character, (character_x_pos, character_y_pos))
            screen.blit(timer, (10, 10))
        
            pygame.display.update()

        # 게임 오버 메시지
        msg = game_font.render(game_result, True, (255, 255, 0)) # 노란색
        msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
        screen.blit(msg, msg_rect)
        pygame.display.update()

        # 2초 대기
        pygame.time.delay(4000)

        pygame.quit()

        pygame.init()


MAX_WIDTH = 800
MAX_HEIGHT = 500
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

current_path = os.path.dirname(__file__)
story01 = pygame.image.load(os.path.join(current_path, resource_path("news2.png")))

start_ticks = pygame.time.get_ticks()

def main():

    fps = pygame.time.Clock()

    running = True
    while running:

        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
     
        screen.blit(story01, (0, 0))

        if elapsed_time > 3:
            running = False
        
    
        pygame.display.update()
        fps.tick(30)

if __name__ == '__main__':
    main()

pygame.time.delay(2000)
pygame.quit()



# <<<< 엔딩 >>>> 

if Success_end:

    pygame.init()

    MAX_WIDTH = 1000
    MAX_HEIGHT = 500
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

    current_path = os.path.dirname(__file__)
    ending = pygame.image.load(os.path.join(current_path, resource_path("end.png")))
    story01 = pygame.image.load(os.path.join(current_path, resource_path("tree1.png")))
    story02 = pygame.image.load(os.path.join(current_path, resource_path("tree.png")))
    story03 = pygame.image.load(os.path.join(current_path, resource_path("test4.png")))
    story04 = pygame.image.load(os.path.join(current_path, resource_path("test6.png")))
    story05 = pygame.image.load(os.path.join(current_path, resource_path("test3.png")))
    story06 = pygame.image.load(os.path.join(current_path, resource_path("test5.png")))
    story08 = pygame.image.load(os.path.join(current_path, resource_path("tree2.png")))
    end1 = pygame.image.load(os.path.join(current_path, resource_path("sb1.png")))
    end2 = pygame.image.load(os.path.join(current_path, resource_path("sb2.png")))
    end3 = pygame.image.load(os.path.join(current_path, resource_path("sb3.png")))
    end4 = pygame.image.load(os.path.join(current_path, resource_path("sb4.png")))
    end5 = pygame.image.load(os.path.join(current_path, resource_path("sb5.png")))
    end6 = pygame.image.load(os.path.join(current_path, resource_path("sb6.png")))
    end7 = pygame.image.load(os.path.join(current_path, resource_path("sb7.png")))
    end8 = pygame.image.load(os.path.join(current_path, resource_path("sb8.png")))

    imgDino1 = pygame.image.load(resource_path('sdino1.png')).convert_alpha()
    imgDino2 = pygame.image.load(resource_path('sdino2.png')).convert_alpha()


    start_ticks = pygame.time.get_ticks()

    color = (46, 46, 46)


    def main():

        fps = pygame.time.Clock()

        dino_height = story05.get_size()[1]
        leg_swap = False
        is_bottom = True
        is_go_up = False
        end_y = 0
        dino_y = 300
        jump_top = 200
        dino_bottom = MAX_HEIGHT - dino_height
        dino_x = 10
        tree_x = 0
        tree1_x = 0
        tree2_x = 0
        tree3_x = 0

        running = True

        while running:

            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            end_y -= 2.5

            screen.fill(color)
            screen.blit(ending, (580, end_y))
            
            if elapsed_time > 0:
                screen.blit(end8, (30, 30))
            if elapsed_time > 3:
                screen.blit(end1, (30, 30))
            if elapsed_time > 6:
                screen.blit(end2, (30, 30))
            if elapsed_time > 9:
                screen.blit(end3, (30, 30))
            if elapsed_time > 12:
                screen.blit(end4, (30, 30))
            if elapsed_time > 15:
                screen.blit(end5, (30, 30))
            if elapsed_time > 18:
                screen.blit(end6, (30, 30))
            if elapsed_time > 21:
                screen.blit(end7, (30, 30))
            if elapsed_time > 24:
                screen.blit(story04, (30, 30))

            if elapsed_time > 0 and elapsed_time < 26:
                screen.blit(story06, (10, 375))

            elif elapsed_time >= 26 and elapsed_time < 27:
                screen.blit(story03, (10, 375))

            elif elapsed_time >= 27 and elapsed_time < 28:
                screen.blit(story05, (10, 315))

            elif elapsed_time >= 28  and elapsed_time < 28.8:
                if is_bottom:
                    is_go_up = True
                    is_bottom = False
                if leg_swap:
                    screen.blit(story05, (10, dino_y))
                    leg_swap = False
                else:
                    screen.blit(story05, (10, dino_y))
                    leg_swap = True

            elif elapsed_time >= 28.8:
                if leg_swap:
                    screen.blit(imgDino1, (dino_x, 375))
                    leg_swap = False
                else:
                    screen.blit(imgDino2, (dino_x, 375))
                    leg_swap = True
                dino_x += 7
        
            if elapsed_time >= 30.4:
                screen.blit(story08, (tree2_x, 380))
                tree2_x += 8

            if elapsed_time >= 29.4:
                screen.blit(story01, (tree1_x, 437))
                tree1_x += 7

            if elapsed_time >= 29.2:
                screen.blit(story02, (tree_x, 437))
                tree_x += 6

            if elapsed_time >= 30.7:
                screen.blit(story01, (tree3_x, 437))
                tree3_x += 6

                if tree3_x > 1100:
                    running = False

            if is_go_up:
                dino_y -= 22.0
            elif not is_go_up and not is_bottom:
                dino_y += 22.0

            # dino top and bottom check
            if is_go_up and dino_y <= jump_top:
                is_go_up = False

            if not is_bottom and dino_y >= dino_bottom:
                is_bottom = True
                dino_y = dino_bottom

            # draw dino
            
            

            pygame.display.update()
            fps.tick(30)

    if __name__ == '__main__':
        main()

    pygame.time.delay(3000)
    pygame.quit()

