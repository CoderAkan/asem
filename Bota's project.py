import pygame, sys
from button import Button
from random import randint
pygame.init()

win = pygame.display.set_mode((500, 450))

pygame.display.set_caption("Menu")

BG = pygame.image.load("back.jpeg")
bullets = []

music = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        win.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(30).render("MAIN MENU", True, "#d7fcd4")
        MENU_RECT = MENU_TEXT.get_rect(center=(250, 50))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(250, 150),
                             text_input='PLAY', font=get_font(25), base_color="#d7fcd4", hovering_color="white")
        INSTRUCTION_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(250, 270),
                                    text_input='INSTRUCTIONS', font=get_font(25), base_color="#d7fcd4", hovering_color="white")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(250, 390),
                             text_input='QUIT', font=get_font(25), base_color="#d7fcd4", hovering_color="white")
        win.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, INSTRUCTION_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play1()
                if INSTRUCTION_BUTTON.checkForInput(MENU_MOUSE_POS):
                    instr()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def instr():
    pygame.display.set_caption('Instructions')
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        win.fill("white")
        win.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(20).render("Instructions", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(250, 45))
        win.blit(OPTIONS_TEXT, OPTIONS_RECT)

        GOAL_TEXT1 = get_font(12).render("The main goal is to rescue princess", True, "White")
        GOAL_RECT1 = GOAL_TEXT1.get_rect(topleft=(10, 70))
        win.blit(GOAL_TEXT1, GOAL_RECT1)

        GOAL_TEXT2 = get_font(12).render("from zombies", True, "White")
        GOAL_RECT2 = GOAL_TEXT2.get_rect(topleft=(10, 85))
        win.blit(GOAL_TEXT2, GOAL_RECT2)

        SECOND_TEXT1 = get_font(12).render("A player can simultaneously shoot", True, "White")
        SECOND_RECT1 = SECOND_TEXT1.get_rect(topleft=(10, 115))
        win.blit(SECOND_TEXT1, SECOND_RECT1)

        SECOND_TEXT2 = get_font(12).render("only 5 bullets", True, "White")
        SECOND_RECT2 = SECOND_TEXT2.get_rect(topleft=(10, 130))
        win.blit(SECOND_TEXT2, SECOND_RECT2)

        THIRD_TEXT1 = get_font(12).render("To reach the next level player should", True, "White")
        THIRD_RECT1 = THIRD_TEXT1.get_rect(topleft=(10, 160))
        win.blit(THIRD_TEXT1, THIRD_RECT1)

        THIRD_TEXT2 = get_font(12).render("kill all zombies or reach the end", True, "White")
        THIRD_RECT2 = SECOND_TEXT2.get_rect(topleft=(10, 175))
        win.blit(THIRD_TEXT2, THIRD_RECT2)

        FOURTH_TEXT1 = get_font(12).render("To move forward press right key", True, "White")
        FOURTH_RECT1 = FOURTH_TEXT1.get_rect(topleft=(10, 205))
        win.blit(FOURTH_TEXT1, FOURTH_RECT1)

        FOURTH_TEXT2 = get_font(12).render("to move backward press left key", True, "White")
        FOURTH_RECT2 = FOURTH_TEXT2.get_rect(topleft=(10, 220))
        win.blit(FOURTH_TEXT2, FOURTH_RECT2)

        FIFTH_TEXT1 = get_font(12).render("To shoot press space key, to appear in", True, "White")
        FIFTH_RECT1 = FIFTH_TEXT1.get_rect(topleft=(10, 250))
        win.blit(FIFTH_TEXT1, FIFTH_RECT1)

        FIFTH_TEXT2 = get_font(12).render("specific place click anywhere in the", True, "White")
        FIFTH_RECT2 = FIFTH_TEXT2.get_rect(topleft=(10, 265))
        win.blit(FIFTH_TEXT2, FIFTH_RECT2)

        FIFTH_TEXT3 = get_font(12).render("screen with mouse after 1 seconds", True, "White")
        FIFTH_RECT3 = FIFTH_TEXT3.get_rect(topleft=(10, 280))
        win.blit(FIFTH_TEXT3, FIFTH_RECT3)

        FIFTH_TEXT4 = get_font(12).render("it works only in Level 1", True, "White")
        FIFTH_RECT4 = FIFTH_TEXT4.get_rect(topleft=(10, 295))
        win.blit(FIFTH_TEXT4, FIFTH_RECT4)

        SIXTH_TEXT1 = get_font(12).render("Moving mouse down will make the", True, "White")
        SIXTH_RECT1 = SIXTH_TEXT1.get_rect(topleft=(10, 325))
        win.blit(SIXTH_TEXT1, SIXTH_RECT1)

        SIXTH_TEXT2 = get_font(12).render("number of bullets 0", True, "White")
        SIXTH_RECT2 = SIXTH_TEXT2.get_rect(topleft=(10, 340))
        win.blit(SIXTH_TEXT2, SIXTH_RECT2)

        SIXTH_TEXT3 = get_font(12).render("Moving mouse up will make the", True, "White")
        SIXTH_RECT3 = SIXTH_TEXT3.get_rect(topleft=(10, 355))
        win.blit(SIXTH_TEXT3, SIXTH_RECT3)

        SIXTH_TEXT4 = get_font(12).render("number of bullets 5", True, "White")
        SIXTH_RECT4 = SIXTH_TEXT4.get_rect(topleft=(10, 370))
        win.blit(SIXTH_TEXT4, SIXTH_RECT4)

        OPTIONS_BACK = Button(image=None, pos=(250, 425),
                              text_input="BACK", font=get_font(25), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def play1():
    pygame.display.set_caption("Level 1")
    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load(
        'R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load(
        'R8.png'), pygame.image.load('R9.png')]
    walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load(
        'L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load(
        'L8.png'), pygame.image.load('L9.png')]

    bulletSound = pygame.mixer.Sound("bullet.mp3")
    hitSound = pygame.mixer.Sound("hit.mp3")

    bg = pygame.image.load('bg.jpg')
    char = pygame.image.load('standing.png')

    clock = pygame.time.Clock()

    score = 0

    class Player(object):
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 5
            self.isJump = False
            self.jumpCount = 10
            self.left = False
            self.right = True
            self.walkCount = 0
            self.standing = True
            self.hitBox = (self.x + 17, self.y + 11, 29, 52)

        def draw(self, win):
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if not self.standing:
                if self.left:
                    win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            else:
                if self.right:
                    win.blit(walkRight[0], (self.x, self.y))
                else:
                    win.blit(walkLeft[0], (self.x, self.y))
            self.hitBox = (self.x + 17, self.y + 11, 29, 52)
        def hit(self):
            self.isJump = False
            self.jumpCount = 10
            self.x = 5
            self.y = 350
            self.walkCount = 0
            self.font1 = pygame.font.SysFont("Press Start 2P", 75)
            self.text = self.font1.render('YOU LOST', 1, (255, 0, 0))
            win.blit(self.text, (250 - (self.text.get_width()/2), 200))
            pygame.display.update()
            i = 0
            while i < 100:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 101
                        pygame.quit()
        def cleared(self):
            win.blit(BG, (0, 0))
            self.font2 = pygame.font.SysFont("Press Start 2P", 50)
            self.text2 = self.font2.render("Level 1 is cleared", 1, (255, 0, 0))
            win.blit(self.text2, (250 - (self.text2.get_width() / 2), 200))
            pygame.display.update()
            i = 0
            while i < 100:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 101
                        pygame.quit()


    class Projectile(object):
        def __init__(self, x, y, radius, color, facing):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.facing = facing
            self.vel = 8 * facing

        def draw(self, win):
            pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


    class Enemy(object):
        walkERight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load(
            'R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load(
            'R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
        walkELeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load(
            'L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load(
            'L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

        def __init__(self, x, y, width, height, end):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.end = end
            self.path = [0, self.end]
            self.walkCount = 0
            self.vel = 3
            self.hitBox = (self.x + 17, self.y + 2, 31, 57)
            self.health = 10
            self.visible = True

        def draw(self, win):
            self.move()
            if self.visible:
                if self.walkCount + 1 >= 33:
                    self.walkCount = 0

                if self.vel > 0:
                    win.blit(self.walkERight[self.walkCount//3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.walkELeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                self.hitBox = (self.x + 17, self.y + 2, 31, 57)
                pygame.draw.rect(win, (255, 0, 0), (self.hitBox[0], self.hitBox[1] - 20, 50, 10))
                pygame.draw.rect(win, (0, 255, 0), (self.hitBox[0], self.hitBox[1] - 20, 50 - (5 * (10 - self.health)), 10))

        def move(self):
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
                else:
                    self.vel *= -1
                    self.walkCount = 0
            else:
                if self.x + self.vel > self.path[0]:
                    self.x += self.vel
                else:
                    self.vel *= -1
                    self.walkCount = 0
        def hit(self):
            if self.health > 1:
                self.health -= 1
            else:
                self.visible = False

    def redrawGameWindow():
        global walkCount, x, y, bullets
        win.blit(bg, (0, 0))
        text = font.render("Score: " + str(score), 1, (0, 0, 0))
        win.blit(text, (360, 16))
        man.draw(win)
        goblin.draw(win)
        for bullet in bullets:
            bullet.draw(win)
        pygame.display.update()


    font = pygame.font.SysFont('Press Start 2P', 40, True)
    man = Player(5, 350, 64, 64)
    m = [250, 300, 350]
    goblin = Enemy(m[randint(0, 2)], 350, 64, 64, 400)
    shootLoop = 0
    run = True
    l = 5
    ik = -1
    t = False
    while run:
        clock.tick(27)
        ik += 1
        if ik == 50:
            t = True

        if goblin.visible == True:
            if man.hitBox[1] < goblin.hitBox[1] + goblin.hitBox[3] and man.hitBox[3] + man.hitBox[1] > goblin.hitBox[1]:
                if man.hitBox[0] + man.hitBox[2] > goblin.hitBox[0] and man.hitBox[0] < goblin.hitBox[0] + goblin.hitBox[2]:
                    man.hit()
                    goblin.x = 150
                    score = 0
                    bullets.clear()
                    goblin.health = 10
        else:
            i = 0
            while i < 50:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 101
                        pygame.quit()
            bullets.clear()
            man.cleared()
            play2()

        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                l = 0
                print("Down")
            if event.type == pygame.MOUSEBUTTONUP:
                l = 5
                print('Up')
            if t and event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()
                man.x, man.y = mouse_position[0], 350
                t = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for bullet in bullets:
            if goblin.visible:
                if bullet.y - bullet.radius < goblin.hitBox[1] + goblin.hitBox[3] and bullet.y + bullet.radius > goblin.hitBox[1]:
                    if bullet.x + bullet.radius > goblin.hitBox[0] and bullet.x - bullet.radius < goblin.hitBox[0] + goblin.hitBox[2]:
                        goblin.hit()
                        hitSound.play()
                        score += 1
                        bullets.pop(bullets.index(bullet))
            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))


        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE] and shootLoop == 0:
            if man.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < l:
                bulletSound.play()
                bullets.append(Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))
            shootLoop = 1

        if keys[pygame.K_LEFT] and man.x > 5:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT]:
            if man.x >= 500 - man.width - man.vel - 1:
                i = 0
                while i < 50:
                    pygame.time.delay(10)
                    i += 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            i = 101
                            pygame.quit()
                bullets.clear()
                man.cleared()
                play2()
            elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
                man.x += man.vel
                man.right = True
                man.left = False
                man.standing = False
        else:
            man.standing = True
            man.walkCount = 0
        if not man.isJump:
            if keys[pygame.K_UP]:
                man.isJump = True
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= neg * (man.jumpCount ** 2) * 0.5
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10

        redrawGameWindow()
    pygame.display.update()

def play2():
    pygame.display.set_caption("Level 2")
    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load(
        'R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load(
        'R8.png'), pygame.image.load('R9.png')]
    walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load(
        'L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load(
        'L8.png'), pygame.image.load('L9.png')]

    bulletSound = pygame.mixer.Sound("bullet.mp3")
    hitSound = pygame.mixer.Sound("hit.mp3")

    bg = pygame.image.load('bg.jpg')
    char = pygame.image.load('standing.png')

    clock = pygame.time.Clock()

    score = 0

    class Player(object):
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 5
            self.isJump = False
            self.jumpCount = 10
            self.left = False
            self.right = True
            self.walkCount = 0
            self.standing = True
            self.hitBox = (self.x + 17, self.y + 11, 29, 52)

        def draw(self, win):
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            self.hitbox = (self.x + 17, self.y + 11, 29, 52)
            if not self.standing:
                if self.left:
                    win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            else:
                if self.right:
                    win.blit(walkRight[0], (self.x, self.y))
                else:
                    win.blit(walkLeft[0], (self.x, self.y))
            self.hitBox = (self.x + 17, self.y + 11, 29, 52)
        def hit(self):
            self.isJump = False
            self.jumpCount = 10
            self.x = 5
            self.y = 350
            self.walkCount = 0
            self.font1 = pygame.font.SysFont("Press Start 2P", 75)
            self.text = self.font1.render('YOU LOST', 1, (255, 0, 0))
            win.blit(self.text, (250 - (self.text.get_width()/2), 200))
            pygame.display.update()
            i = 0
            while i < 100:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 101
                        pygame.quit()
            play1()
        def cleared(self):
            win.blit(BG, (0, 0))
            self.font2 = pygame.font.SysFont("Press Start 2P", 50)
            self.text2 = self.font2.render("Level 2 is cleared", 1, (255, 0, 0))
            win.blit(self.text2, (250 - (self.text2.get_width() / 2), 200))
            pygame.display.update()
            i = 0
            while i < 100:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 101
                        pygame.quit()


    class Projectile(object):
        def __init__(self, x, y, radius, color, facing):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.facing = facing
            self.vel = 8 * facing

        def draw(self, win):
            pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


    class Enemy(object):
        walkERight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load(
            'R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load(
            'R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
        walkELeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load(
            'L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load(
            'L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

        def __init__(self, x, y, width, height, end, vel=3):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.end = end
            self.walkCount = 0
            self.vel = vel
            if self.vel > 0:
                self.path = [self.x, self.end]
                self.path[0] = 0
            else:
                self.path = [self.end, self.x]
                self.path[0] = 0
            self.hitBox = (self.x + 17, self.y + 2, 31, 57)
            self.health = 10
            self.visible = True

        def draw(self, win):
            self.move()
            self.hitBox = (self.x + 17, self.y + 2, 31, 57)
            if self.visible:
                if self.walkCount + 1 >= 33:
                    self.walkCount = 0

                if self.vel > 0:
                    win.blit(self.walkERight[self.walkCount//3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.walkELeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                pygame.draw.rect(win, (255, 0, 0), (self.hitBox[0], self.hitBox[1] - 20, 50, 10))
                pygame.draw.rect(win, (0, 255, 0), (self.hitBox[0], self.hitBox[1] - 20, 50 - (5 * (10 - self.health)), 10))

        def move(self):
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
                else:
                    self.vel *= -1
                    self.walkCount = 0
            else:
                if self.x + self.vel > self.path[0]:
                    self.x += self.vel
                else:
                    self.vel *= -1
                    self.walkCount = 0
        def hit(self):
            if self.health > 1:
                self.health -= 1
            else:
                self.visible = False

    def redrawGameWindow():
        global walkCount, x, y, bullets
        win.blit(bg, (0, 0))
        text = font.render("Score: " + str(score), 1, (0, 0, 0))
        win.blit(text, (360, 16))
        man.draw(win)
        goblin1.draw(win)
        goblin2.draw(win)
        for bullet in bullets:
            bullet.draw(win)
        pygame.display.update()


    font = pygame.font.SysFont('Press Start 2P', 40, True)
    man = Player(5, 350, 64, 64)
    m = [250, 300, 350]
    goblin1 = Enemy(m.pop(), 350, 64, 64, 400)
    goblin2 = Enemy(m.pop(), 350, 64, 64, 50, -3)
    shootLoop = 0
    run = True
    while run:
        clock.tick(27)

        if goblin1.visible:
            if man.hitBox[1] < goblin1.hitBox[1] + goblin1.hitBox[3] and man.hitBox[3] + man.hitBox[1] > goblin1.hitBox[1]:
                if man.hitBox[0] + man.hitBox[2] > goblin1.hitBox[0] and man.hitBox[0] < goblin1.hitBox[0] + goblin1.hitBox[2]:
                    man.hit()
                    goblin1.x, goblin1.y = 50, 350
                    score = 0
                    bullets.clear()
                    goblin1.health = 10
        if goblin2.visible:
            if man.hitBox[1] < goblin2.hitBox[1] + goblin2.hitBox[3] and man.hitBox[3] + man.hitBox[1] > goblin2.hitBox[1]:
                if man.hitBox[0] + man.hitBox[2] > goblin2.hitBox[0] and man.hitBox[0] < goblin1.hitBox[0] + goblin2.hitBox[2]:
                    man.hit()
                    goblin2.x, goblin2.y = 50, 350
                    score = 0
                    bullets.clear()
                    goblin2.health = 10
        if not goblin1.visible and not goblin2.visible:
            i = 0
            while i < 50:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 101
                        pygame.quit()
            bullets.clear()
            man.cleared()
            play3()

        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for bullet in bullets:
            try:
                if goblin1.visible:
                    if bullet.y - bullet.radius < goblin1.hitBox[1] + goblin1.hitBox[3] and bullet.y + bullet.radius > goblin1.hitBox[1]:
                        if bullet.x + bullet.radius > goblin1.hitBox[0] and bullet.x - bullet.radius < goblin1.hitBox[0] + goblin1.hitBox[2]:
                            goblin1.hit()
                            hitSound.play()
                            score += 1
                            bullets.pop(bullets.index(bullet))
                if goblin2.visible:
                    if bullet.y - bullet.radius < goblin2.hitBox[1] + goblin2.hitBox[3] and bullet.y + bullet.radius > goblin2.hitBox[1]:
                        if bullet.x + bullet.radius > goblin2.hitBox[0] and bullet.x - bullet.radius < goblin2.hitBox[0] + goblin2.hitBox[2]:
                            goblin2.hit()
                            hitSound.play()
                            score += 1
                            bullets.pop(bullets.index(bullet))
            except:
                i = 0
                while i < 10:
                    pygame.time.delay(10)
                    i += 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            i = 101
                            pygame.quit()
                if goblin2.visible:
                    if bullet.y - bullet.radius < goblin2.hitBox[1] + goblin2.hitBox[3] and bullet.y + bullet.radius > goblin2.hitBox[1]:
                        if bullet.x + bullet.radius > goblin2.hitBox[0] and bullet.x - bullet.radius < goblin2.hitBox[0] + goblin2.hitBox[2]:
                            goblin2.hit()
                            hitSound.play()
                            score += 1
                            bullets.pop(bullets.index(bullet))
                else:
                    if bullet.y - bullet.radius < goblin1.hitBox[1] + goblin1.hitBox[3] and bullet.y + bullet.radius > goblin1.hitBox[1]:
                        if bullet.x + bullet.radius > goblin1.hitBox[0] and bullet.x - bullet.radius < goblin1.hitBox[0] + goblin1.hitBox[2]:
                            goblin1.hit()
                            hitSound.play()
                            score += 1
                            bullets.pop(bullets.index(bullet))
            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))


        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootLoop == 0:
            if man.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 5:
                bulletSound.play()
                bullets.append(Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))
            shootLoop = 1

        if keys[pygame.K_LEFT] and man.x > 5:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT]:
            if man.x >= 500 - man.width - man.vel - 1:
                i = 0
                while i < 50:
                    pygame.time.delay(10)
                    i += 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            i = 101
                            pygame.quit()
                bullets.clear()
                man.cleared()
                play3()
            elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
                man.x += man.vel
                man.right = True
                man.left = False
                man.standing = False
        elif keys[pygame.K_RIGHT] and man.x == 500 - man.width - man.vel:
            print("Second level is finished")
            main_menu()
        else:
            man.standing = True
            man.walkCount = 0
        if not man.isJump:
            if keys[pygame.K_UP]:
                man.isJump = True
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= neg * (man.jumpCount ** 2) * 0.5
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10

        redrawGameWindow()
    pygame.display.update()

def play3():
    pygame.display.set_caption("Level 3")
    walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load(
        'R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load(
        'R8.png'), pygame.image.load('R9.png')]
    walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load(
        'L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load(
        'L8.png'), pygame.image.load('L9.png')]

    bulletSound = pygame.mixer.Sound("bullet.mp3")
    hitSound = pygame.mixer.Sound("hit.mp3")

    bg = pygame.image.load('bg.jpg')
    char = pygame.image.load('standing.png')
    princess = pygame.image.load("pr.png").convert()

    clock = pygame.time.Clock()

    score = 0

    class Player(object):
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 5
            self.isJump = False
            self.jumpCount = 10
            self.left = False
            self.right = True
            self.walkCount = 0
            self.standing = True
            self.hitBox = (self.x + 17, self.y + 11, 29, 52)

        def draw(self, win):
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if not self.standing:
                if self.left:
                    win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            else:
                if self.right:
                    win.blit(walkRight[0], (self.x, self.y))
                else:
                    win.blit(walkLeft[0], (self.x, self.y))
            self.hitBox = (self.x + 17, self.y + 11, 29, 52)
        def hit(self):
            self.isJump = False
            self.jumpCount = 10
            self.x = 5
            self.y = 350
            self.walkCount = 0
            self.font1 = pygame.font.SysFont("Press Start 2P", 75)
            self.text = self.font1.render('YOU LOST', 1, (255, 0, 0))
            win.blit(self.text, (250 - (self.text.get_width()/2), 200))
            pygame.display.update()
            i = 0
            while i < 100:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 101
                        pygame.quit()
            play1()
        def cleared(self):
            win.blit(BG, (0, 0))
            self.font2 = pygame.font.SysFont("Press Start 2P", 50)
            self.font3 = pygame.font.SysFont("Press Start 2P", 25)
            self.text2 = self.font2.render("Level 3 is cleared", 1, (255, 0, 0))
            self.text3 = self.font3 .render("You were able to save the princess", 1, (255, 0, 0))
            win.blit(self.text2, (250 - (self.text2.get_width() / 2), 200))
            win.blit(self.text3, (250 - (self.text3.get_width() / 2), 300))
            pygame.display.update()
            i = 0
            while i < 150:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 101
                        pygame.quit()


    class Projectile(object):
        def __init__(self, x, y, radius, color, facing):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.facing = facing
            self.vel = 8 * facing

        def draw(self, win):
            pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


    class Enemy(object):
        walkERight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load(
            'R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load(
            'R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
        walkELeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load(
            'L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load(
            'L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

        def __init__(self, x, y, width, height, end, vel=3):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.end = end
            self.walkCount = 0
            self.vel = vel
            self.path = [0, end]
            self.hitBox = (self.x + 17, self.y + 2, 31, 57)
            self.health = 10
            self.visible = True

        def draw(self, win):
            self.move()
            if self.visible:
                if self.walkCount + 1 >= 33:
                    self.walkCount = 0

                if self.vel > 0:
                    win.blit(self.walkERight[self.walkCount//3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.walkELeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                self.hitBox = (self.x + 17, self.y + 2, 31, 57)
                pygame.draw.rect(win, (255, 0, 0), (self.hitBox[0], self.hitBox[1] - 20, 50, 10))
                pygame.draw.rect(win, (0, 255, 0), (self.hitBox[0], self.hitBox[1] - 20, 50 - (5 * (10 - self.health)), 10))

        def move(self):
            if self.vel > 0:
                if self.x + self.vel < self.path[1]:
                    self.x += self.vel
                else:
                    self.vel *= -1
                    self.walkCount = 0
            else:
                if self.x + self.vel > self.path[0]:
                    self.x += self.vel
                else:
                    self.vel *= -1
                    self.walkCount = 0
        def hit(self):
            if self.health > 1:
                self.health -= 1
            else:
                self.visible = False

    def redrawGameWindow():
        global walkCount, x, y, bullets
        win.blit(bg, (0, 0))
        text = font.render("Score: " + str(score), 1, (0, 0, 0))
        win.blit(text, (360, 16))
        man.draw(win)
        goblin1.draw(win)
        goblin2.draw(win)
        goblin3.draw(win)
        win.blit(princess,(420, 350))
        win.blit
        for bullet in bullets:
            bullet.draw(win)
        pygame.display.update()


    font = pygame.font.SysFont('Press Start 2P', 40, True)
    man = Player(5, 350, 64, 64)
    m = [250, 300, 350]
    goblin1 = Enemy(m.pop(), 350, 64, 64, 350)
    goblin2 = Enemy(m.pop(), 350, 64, 64, 350, -3)
    goblin3 = Enemy(m.pop(), 350, 64, 64, 350, -3)
    shootLoop = 0
    run = True
    while run:
        clock.tick(27)

        if goblin1.visible:
            if man.hitBox[1] < goblin1.hitBox[1] + goblin1.hitBox[3] and man.hitBox[3] + man.hitBox[1] > goblin1.hitBox[1]:
                if man.hitBox[0] + man.hitBox[2] > goblin1.hitBox[0] and man.hitBox[0] < goblin1.hitBox[0] + goblin1.hitBox[2]:
                    man.hit()
                    goblin1.x, goblin1.y = 50, 350
                    score = 0
                    bullets.clear()
                    goblin1.health = 10
        if goblin2.visible:
            if man.hitBox[1] < goblin2.hitBox[1] + goblin2.hitBox[3] and man.hitBox[3] + man.hitBox[1] > goblin2.hitBox[1]:
                if man.hitBox[0] + man.hitBox[2] > goblin2.hitBox[0] and man.hitBox[0] < goblin1.hitBox[0] + goblin2.hitBox[2]:
                    man.hit()
                    goblin2.x, goblin2.y = 50, 350
                    score = 0
                    bullets.clear()
                    goblin2.health = 10
        if goblin3.visible:
            if man.hitBox[1] < goblin3.hitBox[1] + goblin3.hitBox[3] and man.hitBox[3] + man.hitBox[1] > goblin3.hitBox[1]:
                if man.hitBox[0] + man.hitBox[2] > goblin3.hitBox[0] and man.hitBox[0] < goblin3.hitBox[0] + goblin3.hitBox[2]:
                    man.hit()
                    goblin3.x, goblin3.y = 50, 350
                    score = 0
                    bullets.clear()
                    goblin2.health = 10
        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for bullet in bullets:
            try:
                if goblin1.visible:
                    if bullet.y - bullet.radius < goblin1.hitBox[1] + goblin1.hitBox[3] and bullet.y + bullet.radius > goblin1.hitBox[1]:
                        if bullet.x + bullet.radius > goblin1.hitBox[0] and bullet.x - bullet.radius < goblin1.hitBox[0] + goblin1.hitBox[2]:
                            goblin1.hit()
                            hitSound.play()
                            score += 1
                            bullets.pop(bullets.index(bullet))
                if goblin2.visible:
                    if bullet.y - bullet.radius < goblin2.hitBox[1] + goblin2.hitBox[3] and bullet.y + bullet.radius > goblin2.hitBox[1]:
                        if bullet.x + bullet.radius > goblin2.hitBox[0] and bullet.x - bullet.radius < goblin2.hitBox[0] + goblin2.hitBox[2]:
                            goblin2.hit()
                            hitSound.play()
                            score += 1
                            bullets.pop(bullets.index(bullet))
                if goblin3.visible:
                    if bullet.y - bullet.radius < goblin3.hitBox[1] + goblin3.hitBox[3] and bullet.y + bullet.radius > goblin3.hitBox[1]:
                        if bullet.x + bullet.radius > goblin3.hitBox[0] and bullet.x - bullet.radius < goblin3.hitBox[0] + goblin3.hitBox[2]:
                            goblin3.hit()
                            hitSound.play()
                            score += 1
                            bullets.pop(bullets.index(bullet))
            except:
                i = 0
                while i < 10:
                    pygame.time.delay(10)
                    i += 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            i = 101
                            pygame.quit()
                if goblin2.visible:
                    if bullet.y - bullet.radius < goblin2.hitBox[1] + goblin2.hitBox[3] and bullet.y + bullet.radius > goblin2.hitBox[1]:
                        if bullet.x + bullet.radius > goblin2.hitBox[0] and bullet.x - bullet.radius < goblin2.hitBox[0] + goblin2.hitBox[2]:
                            goblin2.hit()
                            hitSound.play()
                            score += 1
                            if bullet in bullets:
                                bullets.pop(bullets.index(bullet))
                else:
                    if goblin1.visible:
                        if bullet.y - bullet.radius < goblin1.hitBox[1] + goblin1.hitBox[3] and bullet.y + bullet.radius > goblin1.hitBox[1]:
                            if bullet.x + bullet.radius > goblin1.hitBox[0] and bullet.x - bullet.radius < goblin1.hitBox[0] + goblin1.hitBox[2]:
                                goblin1.hit()
                                hitSound.play()
                                score += 1
                                bullets.pop(bullets.index(bullet))
                    else:
                        if bullet.y - bullet.radius < goblin3.hitBox[1] + goblin3.hitBox[3] and bullet.y + bullet.radius > goblin3.hitBox[1]:
                            if bullet.x + bullet.radius > goblin3.hitBox[0] and bullet.x - bullet.radius < goblin3.hitBox[0] + goblin3.hitBox[2]:
                                goblin3.hit()
                                hitSound.play()
                                score += 1
                                bullets.pop(bullets.index(bullet))
            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))


        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shootLoop == 0:
            if man.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 5:
                bulletSound.play()
                bullets.append(Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))
            shootLoop = 1

        if keys[pygame.K_LEFT] and man.x > 5:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT]:
            if man.x == 450 - man.width - man.vel - 1:
                i = 0
                while i < 50:
                    pygame.time.delay(10)
                    i += 1
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            i = 101
                            pygame.quit()
                bullets.clear()
                man.cleared()
                main_menu()
            elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
                man.x += man.vel
                man.right = True
                man.left = False
                man.standing = False
        elif keys[pygame.K_RIGHT] and man.x == 500 - man.width - man.vel:
            print("Third level is finished")
            main_menu()
        else:
            man.standing = True
            man.walkCount = 0
        if not man.isJump:
            if keys[pygame.K_UP]:
                man.isJump = True
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= neg * (man.jumpCount ** 2) * 0.5
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10

        redrawGameWindow()
    pygame.display.update()

main_menu()
