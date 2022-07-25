import pickle,math
import pygame, sys, time
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.mixer.init()

pygame.display.set_caption("SOMEONE'S ADVENTURE")
screen = pygame.display.set_mode((800, 600), flags=FULLSCREEN)

font = pygame.font.Font('gameAssets\Monsgor-rgx4L.otf', 28)
fonta = pygame.font.Font('gameAssets\Monsgor-rgx4L.otf', 32)
fontb = pygame.font.SysFont('arial', 20)
fontc = pygame.font.Font('gameAssets\Monsgor-rgx4L.otf', 58)
fontd = pygame.font.Font('gameAssets\Monsgor-rgx4L.otf', 48)

star_img = pygame.image.load("gameAssets\star.png").convert()
portal_img_1 = pygame.image.load("gameAssets\portal1.png").convert()
portal_img_2 = pygame.image.load("gameAssets\portal2.png").convert()
portal_img_1.set_colorkey((255,255,255))
portal_img_2.set_colorkey((255,255,255))
star_count = 0

bg0 = pygame.image.load("gameAssets\BG1.png")
bg1 = pygame.image.load("gameAssets\el1.jpg").convert()
bg2 = pygame.image.load("gameAssets\mbg.png").convert()
ll = pygame.image.load("gameAssets\llerror.jpg").convert()
#uae = pygame.image.load("gameAssets\Ae.jpg").convert()
uae = pygame.image.load("gameAssets\JaayFace.png").convert()
but_img = pygame.image.load("gameAssets\Buttons.png")
clickbut = pygame.image.load("gameAssets\clickbutton.png")
score_img = pygame.image.load("gameAssets\score1.png").convert()
score_img.set_colorkey((255, 255, 255))
r = True
mc = ""
ei = pygame.image.load("gameAssets\eid.jpeg").convert()
ep = pygame.image.load("gameAssets\epw.jpeg").convert()
ins = pygame.image.load("gameAssets\instructions.png").convert()
spike_img_2 = pygame.image.load("gameAssets\spike_l.png").convert()
spike_img_1 = pygame.image.load("gameAssets\spike_r.png").convert()
spike_img_2.set_colorkey((255, 255, 255))
spike_img_1.set_colorkey((255, 255, 255))
ded = pygame.image.load("gameAssets\dead.png").convert()
ss1 = pygame.image.load("gameAssets\ss.png").convert()
sco_disp = pygame.image.load("gameAssets\highscore.png").convert()
sco_disp.set_colorkey((0,0,0))
#pw = pygame.image.load("gameAssets\iderror.jpg").convert()
pw = pygame.image.load("gameAssets\JaayFace.png").convert()
game_comp = pygame.image.load("gameAssets\gamecompleted.png").convert()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def but(x, y, l, b, txt, ic, fc):
    sx,sy = pygame.mouse.get_pos()
    button = pygame.Rect(x,y,l,b)
    z=x+l
    f=y+b
    if z > sx > x  and f > sy > y:
        #pygame.draw.rect(screen, ic, button)
        screen.blit(clickbut,(button.x,button.y))
        textSurf, textRect = text_objects(txt, font)
        textRect.center = (((z+x)//2), ((f+y)//2))
        screen.blit(textSurf, textRect)
    else:
        #pygame.draw.rect(screen, fc, button)
        screen.blit(but_img,(button.x,button.y))
        textSurf, textRect = text_objects(txt, font)
        textRect.center = (((z+x)//2), ((f+y)//2))
        screen.blit(textSurf, textRect)
    return button

white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
orange = (255,100,10)
yellow = (255,255,0)
blue_green = (0,255,170)
marroon = (115,0,0)
lime = (180,255,100)
pink = (255,100,180)
purple = (240,0,255)
gray = (127,127,127)
magenta = (255,0,230)
brown = (100,40,0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

def mp(hay):
    global p
    global g
    while True:
        if p == True:
            if hay == 'g' :
                pygame.mixer.music.load('gameAssets\gamemusic.wav')
                pygame.mixer.music.play(-1)
                g = True
                break
            elif hay == 'm':
                pygame.mixer.music.stop()
                pygame.mixer.music.load('gameAssets\menumusic.wav')
                pygame.mixer.music.play(-1)
                break
        else:
            break
        
def entry():
    global p
    p = True
    while True:
        screen.blit(bg0, (0,0))
        
        nx, ny = pygame.mouse.get_pos()
        x = but(100, 420, 200, 50, "SIGN IN", blue_green, white)
        y = but(100, 500, 200, 50, "SIGN UP", purple, magenta)

        sick = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    sick = True

        if x.collidepoint((nx, ny)):
            if sick:
                sign_in()
        if y.collidepoint((nx, ny)):
            if sick:
                sign_up()

        mp('m')
        pygame.display.update()
        mainClock.tick(60)

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 128, 0))
    return textSurface, textSurface.get_rect()

def sign_up():
    global current_player
    ut = ""
    pt = ""
    s = 0
    ir = pygame.Rect(400, 182, 140, 35)
    color_active = yellow
    color_passive = black
    color = color_passive
    color1 = color_passive
    ace = False
    hi = False
    tr = pygame.Rect(400, 382, 140, 35)
    while True:
        screen.blit(bg2,(0,0))
        draw_text("SIGN UP ", fontd, white, screen, 310, 20)
       
        screen.blit(ei, (200,180))
        screen.blit(ep, (200,380))

        ax, ay = pygame.mouse.get_pos()
        back_but = but(150, 500, 200, 50, "BACK", purple, white)
        sub_but = but(450, 500, 200, 50, "SUBMIT", purple, yellow)

        jeshnu = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    jeshnu = True
            if event.type == MOUSEBUTTONDOWN:
                if ir.collidepoint((ax, ay)):
                    ace = True
                else:
                    ace = False
            if event.type == MOUSEBUTTONDOWN:
                if tr.collidepoint((ax, ay)):
                    hi = True
                else:
                    hi = False
            if event.type == pygame.KEYDOWN:
                if ace == True:
                    if len(ut)<=14:
                        ut += event.unicode
                        if event.key == K_BACKSPACE:
                            if True:
                                ut = ut[0:-2]
                    else:
                        ut += ""
                        if event.key == K_BACKSPACE:
                            if True:
                                ut = ut[0:14]
            if event.type == pygame.KEYDOWN:
                if hi == True:
                    if len(pt)<=10:
                        pt += event.unicode
                        if event.key == K_BACKSPACE:
                            if True:
                                pt = pt[0:-2]
                    else:
                        pt += ""
                        if event.key == K_BACKSPACE:
                            if True:
                                pt = pt[0:10]
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if ace:
            color = color_active
        else:
            color = color_passive

        if hi:
            color1 = color_active
        else:
            color1 = color_passive

        pygame.draw.rect(screen, color, ir, 2)
        text2 = fontb.render(ut, True, (0, 255, 0), None)
        text2Rect = text2.get_rect()
        text2Rect.center = (300, 200)
        screen.blit(text2, (ir.x + 5, ir.y + 5))
        ir.w = 165

        pygame.draw.rect(screen, color1, tr, 2)
        f = len(pt)
        g = '*'*f
        text3 = fontb.render(g, True, (0, 255, 0), None)
        text3Rect = text3.get_rect()
        text3Rect.center = (300, 200)
        screen.blit(text3, (tr.x + 5, tr.y + 5))
        tr.w = 165

        if back_but.collidepoint((ax, ay)):
            if jeshnu:
                entry()
        if sub_but.collidepoint((ax, ay)):
            if jeshnu:
                SEArch(ut,pt)

        pygame.display.update()
        mainClock.tick(60)

def SEArch(m,n):
    uaecheck = False
    f=open("gameAssets\Records.dat", "rb")
    l=[]
    l=pickle.load(f)
    for a in l:
        if a[0] == m:
            uaecheck = True
            break
    f.close()
    if uaecheck :
      u_a_e()
    else :
      APPEND(m,n)

def APPEND(z,y):
    l=[]
    f=open("gameAssets\Records.dat", "rb")
    l=pickle.load(f)
    f.close()
    f=open("gameAssets\Records.dat", "wb")
    x=[z,y,None,0,0,0,0,0]
    l.append(x)
    pickle.dump(l,f)
    f.close()
    ss()

def UPDATE(level_prog,score):
    global current_player
    f=open("gameAssets\Records.dat", "rb")
    l=[]
    l=pickle.load(f)
    for x in l:
      if x == current_player:
          if level_prog == "1":
              x[2] = "1"
          if level_prog == "2":
              x[2] = "2"
          if level_prog == "3":
              x[2] = "3"
          if level_prog == "4":
              x[2] = "4"
          if current_level == 1:
              if x[3] < score:
                  x[3] = score
          if current_level == 2:
              if x[4] < score:
                  x[4] = score
          if current_level == 3:
              if x[5] < score:
                  x[5] = score
          if current_level == 4:
              if x[6] < score:
                  x[6] = score
          if current_level == 5:
              if x[7] < score:
                  x[7] = score
          current_player = x
          break
    f.close()
    f = open("gameAssets\Records.dat", "wb")
    pickle.dump(l,f)
    f.close()

def ss():
    while True:
        screen.blit(ss1,(0,0))

        ax,ay=pygame.mouse.get_pos()
        v = but(300, 500, 200, 50, "SIGN IN", gray, magenta)

        nu = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    nu = True

        if v.collidepoint((ax, ay)):
            if nu:
                sign_in()

        pygame.display.update()
        mainClock.tick(60)

def u_a_e():
    while True:
        screen.blit(bg2,(0,0))
        screen.blit(uae, (0,0))
        draw_text("ERROR", font, (0, 128, 0), screen, 350, 20)

        ax,ay=pygame.mouse.get_pos()
        r=but(300, 500, 200, 50, "BACK", yellow, red)

        ae = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    ae = True

        if r.collidepoint((ax, ay)):
            if ae:
                sign_up()

        pygame.display.update()
        mainClock.tick(60)

def wrong_message():
    while True:
        screen.blit(pw,(0,0))

        ax,ay=pygame.mouse.get_pos()
        button_b=but(300, 500, 200, 50, "BACK", lime, brown)

        jeshnu = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    jeshnu = True

        if button_b.collidepoint((ax, ay)):
            if jeshnu:
                sign_in()

        pygame.display.update()
        mainClock.tick(60)

def sign_in():
    global current_player
    global mc
    ut = ""
    s = 0
    ir = pygame.Rect(400, 182, 140, 35)
    color_active = yellow
    color_passive = black
    color = color_passive
    color1 = color_passive
    ace = False
    pt = ""
    tr = pygame.Rect(400, 382, 140, 35)
    hi = False
    while True:
      f=open("gameAssets\Records.dat", "rb")
      l=pickle.load(f)
      f.close()
      screen.blit(bg2,(0,0))
      draw_text("SIGN IN ", fontd, white, screen, 315, 20)
      ax, ay = pygame.mouse.get_pos()
      button_b = but(150, 500, 200, 50, "BACK", blue, black)
      button_c = but(450, 500, 200, 50, "SUBMIT", marroon, blue_green)
      screen.blit(ei,(200,182))
      screen.blit(ep,(200,382))
      jeshnu = False
      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.KEYDOWN:
              if event.key == K_ESCAPE:
                  pygame.quit()
                  sys.exit()
          if event.type == MOUSEBUTTONDOWN:
              if ir.collidepoint((ax, ay)):
                  ace = True
              else:
                  ace = False
          if event.type == MOUSEBUTTONDOWN:
              if tr.collidepoint((ax, ay)):
                  hi = True
              else:
                  hi = False
          if event.type == MOUSEBUTTONDOWN:
              if event.button == 1:
                  jeshnu = True
          if event.type == pygame.KEYDOWN:
              if ace == True:
                  if len(ut)<=10:
                      ut += event.unicode
                      if event.key == K_BACKSPACE:
                          if True:
                              ut = ut[0:-2]
                  else:
                      ut += ""
                      if event.key == K_BACKSPACE:
                          if True:
                              ut = ut[0:10]
          if event.type == pygame.KEYDOWN:
              if hi == True:
                  if len(pt)<=10:
                      pt += event.unicode
                      if event.key == K_BACKSPACE:
                          if True:
                              pt = pt[0:-2]
                  else:
                      pt += ""
                      if event.key == K_BACKSPACE:
                          if True:
                              pt = pt[0:10]

          
      if ace:
          color = color_active
      else:
          color = color_passive

      if hi:
          color1 = color_active
      else:
          color1 = color_passive

      pygame.draw.rect(screen, color, ir, 2)
      text2 = fontb.render(ut, True, (0, 255, 0), None)
      text2Rect = text2.get_rect()
      text2Rect.center = (300, 200)
      screen.blit(text2, (ir.x + 5, ir.y + 5))
      ir.w = 165

      pygame.draw.rect(screen, color1, tr, 2)
      f = len(pt)
      g = '*'*f
      text3 = fontb.render(g, True, (0, 255, 0), None)
      text3Rect = text3.get_rect()
      text3Rect.center = (300, 200)
      screen.blit(text3, (tr.x + 5, tr.y + 5))
      tr.w = 165

      if button_b.collidepoint((ax, ay)):
          if jeshnu:
              entry()
      if button_c.collidepoint((ax, ay)):
          if jeshnu:
              for a in l:
                if a[0] == ut and a[1] == pt:
                  wrgmesginit=True
                  current_player = a
                  mc = "Hey, " + str(ut)
                  main_menu()
                else:
                  wrngmsginit=False
              if wrngmsginit == False:
                wrong_message()
                
      pygame.display.update()
      mainClock.tick(60)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animating = False
        self.x = x
        self.y = y
        self.sprites = []
        self.sprites.append(pygame.image.load("gameAssets\wp1.png"))
        self.sprites.append(pygame.image.load("gameAssets\wp2.png"))
        self.sprites.append(pygame.image.load("gameAssets\wp3.png"))
        self.sprites.append(pygame.image.load("gameAssets\wp4.png"))
        self.sprites.append(pygame.image.load("gameAssets\wp5.png"))
        self.sprites.append(pygame.image.load("gameAssets\wp6.png"))
        self.sprites.append(pygame.image.load("gameAssets\wp7.png"))
        self.sprites.append(pygame.image.load("gameAssets\wp8.png"))
        self.sprites.append(pygame.image.load("gameAssets\wp9.png"))
        self.sprites.append(pygame.image.load("gameAssets\wp10.png"))
        self.sprites.append(pygame.image.load("gameAssets\wp11.png"))
        self.sprites.append(pygame.image.load("gameAssets\wp12.png"))
        self.sprites.append(pygame.image.load("gameAssets\wp13.png"))
        self.sprites.append(pygame.image.load("gameAssets\wp14.png"))
        self.sprites.append(pygame.image.load("gameAssets\wp15.png"))
        self.sprites.append(pygame.image.load("gameAssets\wp16.png"))
        self.currentSprite = 0
        self.image = self.sprites[self.currentSprite]
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.motion = False

    def animate(self, dir):
        self.animating = dir
        if self.animating == "right":
            self.currentSprite = 1
        if self.animating == "left":
            self.currentSprite = 9

    def update(self, speed):
        if self.animating == "stop":
            self.currentSprite = 0
            self.image = self.sprites[int(self.currentSprite)]
        if self.animating == "right":
            self.currentSprite += speed
            if self.currentSprite > 8:
                self.currentSprite = 1
            self.image = self.sprites[int(self.currentSprite)]
        if self.animating == "left":
            self.currentSprite += speed
            if self.currentSprite > 15:
                self.currentSprite = 9
            self.image = self.sprites[int(self.currentSprite)]
        if self.animating == "pause":
            if moving_right :
                self.currentSprite = 1
            if moving_left :
                self.currentSprite = 9
            self.image = self.sprites[int(self.currentSprite)]

class Objects():
        global vertical_momentum
        global player_rect
        global r
        def __init__(self,x,y,end,choice):
            self.x = x
            self.y = y
            self.end = end
            self.c= 0
            self.path = [self.x,self.y,self.end]
            self.choice = choice
            self.hitbox = pygame.Rect(self.x,self.y,20,20)
            
            if self.choice == 1:
                if self.x > self.end:
                    self.velx = -1.5
                    
                    self.c=1
                else:
                    self.velx = 1.5
            elif self.choice == 2:
                if self.y > self.end:
                    self.vely1 = -1
                    self.c=1
                else:
                    self.vely1 = 1
    
            self.vely2 = 0.1
                       
        def move1(self):       
            if self.velx >= 0:
                if self.c==1:
                    if self.x < self.path[0]:
                        self.x += self.velx
                    else:
                        self.velx = self.velx * -1
                else:
                    if self.x < self.path[2]:
                        self.x += self.velx
                    else:
                        self.velx = self.velx * -1                   
            else:
                if self.c == 1:
                    if self.x > self.path[2]:
                        self.x += self.velx
                    else:
                        self.velx = self.velx * -1               
                else:
                    if self.x > self.path[0]:
                        self.x += self.velx
                    else:
                        self.velx = self.velx * -1
            self.hitbox = pygame.Rect(self.x,self.y,20,20)
            spike_img.set_colorkey((255,255,255))
            display.blit(spike_img,(self.x,self.y))

        def move2(self):
            if self.vely1 >= 0:
                if self.c==1:
                    if self.y < self.path[1]:
                        self.y += self.vely1
                    else:
                        self.vely1 = self.vely1 * -1
                else:
                    if self.y < self.path[2]:
                        self.y += self.vely1
                    else:
                        self.vely1 = self.vely1 * -1
            else:
                if self.c == 1:
                    if self.y > self.path[2]:
                        self.y += self.vely1
                    else:
                        self.vely1 = self.vely1        
                else:
                    if self.y > self.path[1]:
                        self.y += self.vely1
                    else:
                        self.vely1 = self.vely1 * -1
            self.hitbox = pygame.Rect(self.x,self.y,20,20)
            spike_img.set_colorkey((255,255,255))
            display.blit(spike_img,(self.x,self.y))

        def move3(self):
            if self.vely2 >= 0:
                if self.y < self.path[2]:
                    self.y += self.vely2
                
            self.hitbox = pygame.Rect(self.x,self.y,20,20)
            spike_img.set_colorkey((255,255,255))
            display.blit(spike_img,(self.x,self.y))

        def star(self):
            global player
            if player.rect.colliderect(self.hitbox) == True:
                if r == True:
                    if self.c == 0:
                        x = pygame.mixer.Sound("gameAssets\star.ogg")
                        pygame.mixer.Sound.play(x)
                    else:
                        pass
                self.c = 1
                self.end += 1
            if self.c != 1:
                star_img.set_colorkey((255,255,255))
                display.blit(star_img,(self.x,self.y))

        def portal(self):
            if self.choice == 1:
                self.hitbox = pygame.Rect(self.x + 4,self.y,12,20)
                display.blit(portal_img_1,(self.x,self.y))
            elif self.choice == 2:
                self.hitbox = pygame.Rect(self.x,self.y + 4,20,12)
                display.blit(portal_img_2,(self.x,self.y))

def dead():
    global r
    if r==True:
        x = pygame.mixer.Sound("gameAssets\gameover.wav")
        pygame.mixer.Sound.play(x)
    else:
        pass
    while True:
        mp('m')
        ded.set_colorkey(white)
        screen.blit(ded, (200, 150))

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        vx,vy = pygame.mouse.get_pos()
        button_2 = but(300,300,200,50,"RETRY",pink,lime)
        button_3 = but(300,375,200,50,"BACK",gray,orange)

        if button_2.collidepoint((vx,vy)):
            if click:
                game()
        if button_3.collidepoint((vx,vy)):
            if click:
                LEVELS()

        pygame.display.update()
        clock.tick(60)

def main_menu():
    global mc
    while True:
        screen.blit(bg2,(0,0))
        draw_text(mc, fontd, (255, 255, 255), screen, 100, 20)

        mx, my = pygame.mouse.get_pos()
        button_1 = but(300, 100, 200, 50, "START GAME", orange, black)
        button_2 = but(300, 200, 200, 50, "SETTINGS", gray, lime)
        button_3 = but(300, 300, 200, 50, "HIGH SCORE", green, yellow)
        button_4 = but(300, 400, 200, 50, "INSTRUCTIONS", magenta, purple)
        button_5 = but(300, 500, 200, 50, "LOGOUT", red, orange)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mx, my)):
            if click:
                LEVELS()
        if button_2.collidepoint((mx, my)):
            if click:
                settings()
        if button_3.collidepoint((mx, my)):
            if click:
                highscore()
        if button_4.collidepoint((mx, my)):
            if click:
                instructions()
        if button_5.collidepoint((mx, my)):
            if click:
                entry()

        pygame.display.update()
        mainClock.tick(60)

def settings():
    global p
    global r
    running = True
    text4 = font.render("ON", True, yellow, None)
    text4Rect = text4.get_rect()
    text4Rect.center = (550, 175)

    text5 = font.render("OFF", True, yellow, None)
    text5Rect = text5.get_rect()
    text5Rect.center = (550, 175)

    text6 = font.render("ON", True, yellow, None)
    text6Rect = text6.get_rect()
    text6Rect.center = (550, 325)

    text7 = font.render("OFF", True, yellow, None)
    text7Rect = text7.get_rect()
    text7Rect.center = (550, 325)
    while running:
        screen.blit(bg2,(0,0))
        draw_text('SETTINGS', fontd, (255, 255, 255), screen, 320, 20)
        
        if p == True:
            screen.blit(text4, text4Rect)
        else:
            screen.blit(text5, text5Rect)

        if r == True:
            screen.blit(text6, text6Rect)
        else:
            screen.blit(text7, text7Rect)
            
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()
        button_1 = but(300, 150, 200, 50, "MUSIC", orange, blue_green)
        button_2 = but(300, 300, 200, 50, "SFX", gray, lime)
        button_3 = but(300, 450, 200, 50, "BACK", blue, red)

        if button_1.collidepoint((mx, my)):
            if click:
                pass
                if p == True:
                    pygame.mixer.music.pause()
                    screen.blit(text5, text5Rect)
                    p = False
                else:
                    pygame.mixer.music.unpause()
                    screen.blit(text4, text4Rect)
                    p = True
        if button_2.collidepoint((mx, my)):
            if click:
                if r == True:
                    screen.blit(text7, text7Rect)
                    r = False
                else:
                    screen.blit(text6, text6Rect)
                    r = True                  
        if button_3.collidepoint((mx,my)):
            if click:
                main_menu()

        pygame.display.update()
        mainClock.tick(60)

def scoredisplay(le):
    l = sc = []
    lensc = 5
    f= open("gameAssets\Records.dat",'rb')
    l = pickle.load(f)
    f.close()
    n=len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j+1][2+le]>l[j][2+le]:
                l[j],l[j+1] = l[j+1],l[j]
    if len(l) < 5:
        lensc = len(l)
    while True:
        y=0
        screen.blit(bg2,(0,0))
        screen.blit(sco_disp,(200,150))
        ax,ay = pygame.mouse.get_pos()
        button_73 = but(600, 540, 200, 50, "BACK", yellow, black)    
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()            
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        if button_73.collidepoint((ax, ay)):
            if click:
                highscore()

        for i in range(lensc):
            draw_text(str(l[i][0]),font,white,screen,230,220+y)
            draw_text(str(l[i][2+le]),font,white,screen,430,220+y)
            y+=45
        pygame.display.update()
        mainClock.tick(60)

def highscore():
    run = True
    while run:
        screen.blit(bg2, (0,0))
        draw_text("HIGHSCORE", fontd, white, screen, 310, 20)
        
        ax,ay = pygame.mouse.get_pos()
        button_1 = but(300, 100, 200, 50, "LEVEL 1", orange, black)
        button_2 = but(300, 200, 200, 50, "LEVEL 2", gray, lime)
        button_3 = but(300, 300, 200, 50, "LEVEL 3", green, yellow)
        button_4 = but(300, 400, 200, 50, "LEVEL 4", magenta, purple)
        button_5 = but(300, 500, 200, 50, "LEVEL 5", red, orange)
        button_73 = but(600, 540, 200, 50, "BACK", yellow, black)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if button_1.collidepoint((ax, ay)):
            if click:
                scoredisplay(1)
        if button_2.collidepoint((ax, ay)):
            if click:
                scoredisplay(2)
        if button_3.collidepoint((ax, ay)):
            if click:
                scoredisplay(3)
        if button_4.collidepoint((ax, ay)):
            if click:
                scoredisplay(4)
        if button_5.collidepoint((ax, ay)):
            if click:
                scoredisplay(5)
        if button_73.collidepoint((ax, ay)):
            if click:
                main_menu()

        pygame.display.update()
        mainClock.tick(60)
    
def instructions():
    run = True
    while run:
        screen.blit(ins, (0,0))

        mx,my = pygame.mouse.get_pos()
        bac = but(600, 540, 200, 50, "BACK", yellow, pink)
        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        if bac.collidepoint((mx, my)):
            if click:
                main_menu()

        pygame.display.update()
        mainClock.tick(60)
      
def LEVELS():
    global current_level
    global current_player
    while True:
        f=open("gameAssets\Records.dat", "rb")
        l=pickle.load(f)
    
        screen.blit(bg2,(0,0))
        draw_text('LEVELS', fontd, (255, 255, 255), screen, 341, 20)

        vx, vy = pygame.mouse.get_pos()
        button_68 = but(300, 100, 200, 50, "LEVEL 1", magenta, gray)
        button_69 = but(300, 200, 200, 50, "LEVEL 2", green, black)
        button_70 = but(300, 300, 200, 50, "LEVEL 3", blue, brown)
        button_71 = but(300, 400, 200, 50, "LEVEL 4", yellow, blue_green)
        button_72 = but(300, 500, 200, 50, "LEVEL 5", orange, yellow)
        button_73 = but(600, 540, 200, 50, "BACK", yellow, black)

        lick = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    lick = True

        if button_68.collidepoint((vx, vy)):
            if lick:
                current_level = 1
                game()
        if button_69.collidepoint((vx, vy)):
            if lick:
                if current_player[2] == "1" or current_player[2] =="2" or current_player[2] =='3' or current_player[2] =='4' or current_player[2] =='5':
                    current_level=2
                    game()
                else:
                    level_error()
                
        if button_70.collidepoint((vx, vy)):
            if lick:
                if current_player[2] == "2" or current_player[2] =='3' or current_player[2] =='4' or current_player[2] =='5' :
                    current_level= 3
                    game()
                else:
                    level_error()
                        
        if button_71.collidepoint((vx, vy)):
            if lick:
                if current_player[2] == "3" or current_player[2] =='4' or current_player[2] =='5':
                    current_level= 4
                    game()
                else:
                    level_error()

        if button_72.collidepoint((vx, vy)):
            if lick:
                if current_player[2] == "4" or current_player[2] =='5':
                    current_level= 5
                    game()
                else:
                    level_error()

        if button_73.collidepoint((vx, vy)):
            if lick:
                main_menu()
            
        f.close()
        pygame.display.update()
        mainClock.tick(60)

def unpause():
    global pause
    pause = False
    
def paused():
    global pause
    global moving_right
    global moving_left
    global p
    global g
    text4 = font.render("ON", True, yellow, None)
    text4Rect = text4.get_rect()
    text4Rect.center = (550, 375)

    text5 = font.render("OFF", True, yellow, None)
    text5Rect = text5.get_rect()
    text5Rect.center = (550, 375)
    while pause:
        screen.blit(bg1,(0,0))
        if p == True:
            screen.blit(text4, text4Rect)
        else:
            screen.blit(text5, text5Rect)

        draw_text('PAUSED', fontd, (255, 255, 255), screen, 341, 20)
        moving_left = False
        moving_right = False
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        vx,vy = pygame.mouse.get_pos()
        button_1 = but(300,100,200,50, "RESUME", red, green)
        button_2 = but(300,225,200,50, "RESTART", blue_green, gray)
        button_x = but(300,350,200,50, "MUSIC", marroon, brown)
        button_3 = but(300,475,200,50, "BACK", orange, red)

        if button_1.collidepoint((vx,vy)):
            if click:
                unpause()
        if button_2.collidepoint((vx,vy)):
            if click:
                game()
        if button_3.collidepoint((vx,vy)):
            if click:
                if p == False:
                    p = True
                    mp('m')
                    
                else:
                    mp('m')
                LEVELS()
        if button_x.collidepoint((vx, vy)):
            if click:
                if p == True:
                    pygame.mixer.music.pause()
                    p = False
                    screen.blit(text5, text5Rect)
                else:
                    screen.blit(text4, text4Rect)
                    pygame.mixer.music.unpause()
                    p = True                 
        pygame.display.update()

def level_error():
    while True:
        screen.blit(ll, (0,0))

        ax,ay=pygame.mouse.get_pos()
        button_c=but(300, 500, 200, 50, "BACK", (238, 55, 255), lime)

        jeshnu = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    jeshnu = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        if button_c.collidepoint((ax, ay)):
            if jeshnu:
                LEVELS()

        pygame.display.update()
        mainClock.tick(60)

WINDOW_SIZE = (800, 600)
clock = pygame.time.Clock()
current_level = 1
display = pygame.Surface((600, 400))
moving_right = False
moving_left = False
current_player=[]
pause = False

def load_map(path):
    path = path + ".txt"
    f = open(path, 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

grass_img = pygame.image.load("gameAssets\gravel.png").convert()
dirt_img = pygame.image.load("gameAssets\gravel.png").convert()
player_image = pygame.image.load("gameAssets\Tile3.png").convert()
door_img = pygame.image.load("gameAssets\door.png").convert()
spike_img = pygame.image.load("gameAssets\spike1.png").convert()
spike_img.set_colorkey((255, 255, 255))
door1 = None
vertical_momentum = 0
air_timer = 0
score = 0
player = Player(50,50)

def scorecalc (time,mint,midt,strcount = 0):
    score = 2999999
    if time > mint and time<= midt :
        score-= time*50000
    elif time > midt and time<= 40 :
        score-=time*10000
        
    score+=strcount*1000
    return score

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {
        'top': False,
        'bottom': False,
        'right': False,
        'left': False
    }
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    float_movm_y = movement[1]
    rect.y += float_movm_y
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

#door_img.set_colorkey(255,255,255)
def level_end(score,star,Time):
    global current_level
    current_level +=1
    screen.blit(score_img,(0,0))
    while True:
        mp('m')        
        draw_text(str(current_level-1), fonta , red, screen, 362, 166)
        draw_text(str(star), fonta, yellow, screen, 362, 244)
        draw_text(str(Time), fonta, yellow, screen, 362, 298)
        draw_text(str(score), fonta, yellow, screen, 362, 351)
        
        click = False
        vx, vy = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        button_c=but(179, 400, 200, 50, "NEXT", red, bright_red)
        button_2 = but(417, 400, 200, 50, "BACK", green, bright_green)
        
        if button_2.collidepoint((vx,vy)):
            if click:
                time.sleep(1)
                LEVELS()

        if button_c.collidepoint((vx,vy)):
            if click:
              if current_level - 1 ==5:

                GAME_COMP()
              else:
                game()

        pygame.display.update()
        clock.tick(60)

def GAME_COMP():
    while True:
        mp("g")
        game_comp.set_colorkey(white)
        screen.blit(game_comp,(0,0))
        draw_text('', font, (255, 255, 255), screen, 300, 20)

        click = False
        vx, vy = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

       
        button_2 = but(300, 400, 200, 50, "BACK", green, bright_green)
        if button_2.collidepoint((vx,vy)):
            if click:
                time.sleep(1)
                main_menu()

        pygame.display.update()
        clock.tick(60)
        
        
def game():
    global current_level
    global moving_right
    global moving_left
    global vertical_momentum
    global air_timer
    global player_rect
    global star_count
    start_timer =None
    timer = star_count = c = 0 
    global pause
    global score
    global p
    global r
    global player
    mp('g')
    if p == False :
        p = True
        mp('g')
        pygame.mixer.music.pause()
        p = False
    check1 = check2 = 0
    seconds = seconds1 = secons2 = 0
    score1 = score2 = score3 = 0
    
    if current_level != 1 :
        vertical_momentum = 0
        moving_right = False
        moving_left = False
        
    if current_level==1:
        player = Player(30, 320)
        playerGroup = pygame.sprite.Group()
        playerGroup.add(player)
        player_rect = pygame.Rect(20,320,20,20)
        star_1 = Objects(340,320,0,4)
        star_2 = Objects(280,200,0,4)
        star_3 = Objects(520,220,0,4)

        game_map = load_map('gameAssets\map1')

    if current_level==2:
        player = Player(30, 320)
        playerGroup = pygame.sprite.Group()
        playerGroup.add(player)
        star_1 = Objects(520,220,0,4)
        star_2 = Objects(300,200,0,4)
        star_3 = Objects(40,160,0,4)
        game_map = load_map('gameAssets\map2')

    if current_level==3:
        player = Player(30, 320)
        playerGroup = pygame.sprite.Group()
        playerGroup.add(player)
        enemy_1 = Objects(380,240,20,1)
        enemy_2 = Objects(140,180,560,1)
        enemy_3 = Objects(500,180,100,2)
        star_1 = Objects(560,260,0,4)
        star_2 = Objects(560,140,0,4)
        star_3 = Objects(500,60,0,4)
        game_map = load_map('gameAssets\map3')

    if current_level==4:
        player = Player(540, 30)
        playerGroup = pygame.sprite.Group()
        playerGroup.add(player)
        enemy_1 = Objects(20,320,160,1)
        enemy_2 = Objects(40,240,360,2)
        enemy_3 = Objects(80,360,240,2)
        enemy_4 = Objects(120,240,360,2)
        enemy_5 = Objects(180,240,280,3)
        enemy_6 = Objects(200,240,360,3)
        enemy_7 = Objects(220,240,360,3)
        enemy_8 = Objects(240,240,360,3)
        enemy_9 = Objects(260,240,300,3)
        enemy_10 = Objects(280,240,420,3)
        enemy_11 = Objects(300,240,420,3)
        enemy_12 = Objects(320,240,340,3)
        enemy_13 = Objects(340,240,420,3)
        enemy_14 = Objects(360,240,420,3)
        enemy_15 = Objects(380,240,420,3)
        star_1 = Objects(20,60,0,4)
        star_2 = Objects(540,200,0,4)
        star_3 = Objects(20,340,0,4)      
        trig_rect = pygame.Rect(20,260,360,400)
        
    if current_level==5:
        player = Player(30, 80)
        playerGroup = pygame.sprite.Group()
        playerGroup.add(player)
        enemy_1 = Objects(60,20,80,2)
        enemy_2 = Objects(200,80,560,1)
        enemy_3 = Objects(560,100,200,1)
        enemy_4 = Objects(200,120,560,1)
        enemy_5 = Objects(340,180,560,1)
        enemy_6 = Objects(560,220,340,1)
        enemy_7 = Objects(340,260,560,1)
        portal_1 = Objects(140,80,0,1)
        portal_2 = Objects(260,40,0,2)
        portal_3 = Objects(560,280,0,1)
        portal_4 = Objects(160,280,0,2)
        star_1 = Objects(300,120,0,4)
        star_2 = Objects(440,300,0,4)
        star_3 = Objects(420,220,0,4)
        game_map = load_map('gameAssets\map5')
    scoreclock = pygame.time.Clock()
    
    while True:
        display.blit(bg1, (0,0))
        player_location = [0, 0]
        spike_list = []
        tile_rects = []
        y = 0
        if current_level == 1:          
          for layer in game_map:
              x = 0
              for tile in layer:
                  if tile == '1':
                      display.blit(dirt_img, (x * 20, y * 20))
                      tile_rects.append(pygame.Rect(x*20,y*20,20,20))
                  if tile == '3':
                      display.blit(door_img, (x * 20, y * 20))
                      door1 = pygame.Rect(x * 20, y * 20, 20, 20)
                  x += 1
              y += 1
            
        if current_level == 2:  
            for layer in game_map:
                x = 0
                for tile in range(len(layer)):           
                    if layer[tile] == '1':
                        display.blit(dirt_img, (x * 20, y * 20))
                        tile_rects.append(pygame.Rect(x*20,y*20,20,20))
                    if layer[tile] == '3':
                        display.blit(door_img, (x * 20, y * 20))
                        door1 = pygame.Rect(x * 20, y * 20, 20, 20)
                    if layer[tile] == '4':
                        if layer[tile + 1] == '1' or layer[tile + 1] == '3':
                            display.blit(spike_img_2, (x * 20, y * 20))
                            spike_list.append(pygame.Rect(x * 20 + 3, y * 20 + 6 , 9, 14))
                        elif layer[tile - 1] == '1' or layer[tile - 1] == '3':
                            display.blit(spike_img_1, (x * 20, y * 20))
                            spike_list.append(pygame.Rect(x * 20 + 3, y * 20 + 3 , 9, 14))
                        else:
                            display.blit(spike_img, (x * 20, y * 20))
                            spike_list.append(pygame.Rect(x * 20 + 3, y * 20 + 11, 14, 9))
                    x += 1
                y += 1

        if current_level == 3:            
            if player.rect.colliderect(enemy_1.hitbox) or player.rect.colliderect(enemy_2.hitbox) or player.rect.colliderect(enemy_3.hitbox):
                dead()
            enemy_1.move1()
            enemy_2.move1()
            enemy_3.move2()
            
            for layer in game_map:
                x = 0
                for tile in range(len(layer)):
                    if layer[tile] == '1':
                        display.blit(dirt_img, (x * 20, y * 20))
                        tile_rects.append(pygame.Rect(x*20,y*20,20,20))
                    if layer[tile] == '3':
                        display.blit(door_img, (x * 20, y * 20))
                        door1 = pygame.Rect(x * 20, y * 20, 20, 20)
                    if layer[tile] == '4':
                        if layer[tile + 1] == '1' or layer[tile + 1] == '3':
                            display.blit(spike_img_2, (x * 20, y * 20))
                            spike_list.append(pygame.Rect(x * 20 + 3, y * 20 + 6 , 9, 14))
                            
                        elif layer[tile - 1] == '1' or layer[tile - 1] == '3':
                            display.blit(spike_img_1, (x * 20, y * 20))
                            spike_list.append(pygame.Rect(x * 20 + 3, y * 20 + 3 , 9, 14))
                        else:
                            display.blit(spike_img, (x * 20, y * 20))
                            spike_list.append(pygame.Rect(x * 20 + 3, y * 20 + 11, 14, 9))                    
                    x += 1
                y += 1

        if current_level == 4:           
            if player.rect.colliderect(trig_rect):
                check1 = True

            if check1 == True:
                game_map = load_map('gameAssets\map4b')
                enemy_1.move1()
                enemy_2.move2()
                enemy_3.move2()
                enemy_4.move2()
                enemy_5.move3()
                enemy_6.move3()
                enemy_7.move3()
                enemy_8.move3()
                enemy_9.move3()
                enemy_10.move3()
                enemy_11.move3()
                enemy_12.move3()
                enemy_13.move3()
                enemy_14.move3()
                enemy_15.move3() 
            else:
                game_map = load_map('gameAssets\map4a')
            
            if player.rect.colliderect(enemy_1.hitbox) or  player.rect.colliderect(enemy_2.hitbox) or  player.rect.colliderect(enemy_3.hitbox) or  player.rect.colliderect(enemy_4.hitbox) or  player.rect.colliderect(enemy_5.hitbox) or  player.rect.colliderect(enemy_6.hitbox) or  player.rect.colliderect(enemy_7.hitbox) or  player.rect.colliderect(enemy_8.hitbox) or  player.rect.colliderect(enemy_9.hitbox) or  player.rect.colliderect(enemy_10.hitbox) or  player.rect.colliderect(enemy_11.hitbox) or  player.rect.colliderect(enemy_12.hitbox) or  player.rect.colliderect(enemy_13.hitbox)or  player.rect.colliderect(enemy_14.hitbox) or  player.rect.colliderect(enemy_15.hitbox):
                dead()                      
            for layer in game_map:
                x=0
                for tile in range(len(layer)):
                    if layer[tile] == '1':
                        display.blit(dirt_img,(x*20,y*20))
                        tile_rects.append(pygame.Rect(x*20,y*20,20,20))
                    if layer[tile] == '3':
                        display.blit(door_img,(x*20,y*20))
                        door1 = pygame.Rect(x*20,y*20,20,20)
                    if layer[tile] == '4':
                        if layer[tile + 1] == '1' or layer[tile + 1] == '3':
                            display.blit(spike_img_2, (x * 20, y * 20))
                            spike_list.append(pygame.Rect(x * 20 + 3, y * 20 + 6 , 9, 14))
                            
                        elif layer[tile - 1] == '1' or layer[tile - 1] == '3':
                            display.blit(spike_img_1, (x * 20, y * 20))
                            spike_list.append(pygame.Rect(x * 20 + 3, y * 20 + 3 , 9, 14))
                        else:
                            display.blit(spike_img, (x * 20, y * 20))
                            spike_list.append(pygame.Rect(x * 20 + 3, y * 20 + 11, 14, 9))                    
                    x += 1
                y += 1

        if current_level == 5:
              if player.rect.colliderect(enemy_1.hitbox) or player.rect.colliderect(enemy_2.hitbox) or player.rect.colliderect(enemy_3.hitbox) or player.rect.colliderect(enemy_4.hitbox)or player.rect.colliderect(enemy_5.hitbox) or player.rect.colliderect(enemy_6.hitbox) or player.rect.colliderect(enemy_7.hitbox):
                    dead()
              enemy_1.move2()
              enemy_2.move1()
              enemy_3.move1()
              enemy_4.move1()
              enemy_5.move1()
              enemy_6.move1()
              enemy_7.move1()
              
              portal_1.portal()
              portal_2.portal()
              portal_3.portal()
              portal_4.portal()

              for layer in game_map:
                  x=0
                  for tile in range(len(layer)):
                      if layer[tile] == '1':
                          display.blit(dirt_img,(x*20,y*20))
                          tile_rects.append(pygame.Rect(x*20,y*20,20,20))
                      if layer[tile] == '3':
                          display.blit(door_img,(x*20,y*20))
                          door1 = pygame.Rect(x*20,y*20,20,20)
                      if layer[tile] == '4':
                        if layer[tile + 1] == '1' or layer[tile + 1] == '3':
                            display.blit(spike_img_2, (x * 20, y * 20))
                            spike_list.append(pygame.Rect(x * 20 + 3, y * 20 + 6 , 9, 14))
                            
                        elif layer[tile - 1] == '1' or layer[tile - 1] == '3':
                            display.blit(spike_img_1, (x * 20, y * 20))
                            spike_list.append(pygame.Rect(x * 20 + 3, y * 20 + 3 , 9, 14))
                        else:
                            display.blit(spike_img, (x * 20, y * 20))
                            spike_list.append(pygame.Rect(x * 20 + 3, y * 20 + 11, 14, 9))
                      if layer[tile] == '5':
                          display.blit(spike_img,(x*20,y*20))
                      x += 1
                  y += 1

        star_1.star()
        if star_1.c == 1 and star_1.end <= 1:
            star_count += 1
        star_2.star()
        if star_2.c == 1 and star_2.end <= 1:
            star_count += 1
        star_3.star()
        if star_3.c == 1 and star_3.end <= 1:
            star_count += 1 

        if moving_right == True:
            player_location[0] += 2
            player.x+=2
        if moving_left == True:
            player_location[0] -= 2
            player.x-=2
        
        vertical_momentum += 0.2
        if vertical_momentum > 3:
            vertical_momentum = 3
        
        player_location[1] += math.floor(vertical_momentum)
        player.rect, collisions = move(player.rect,player_location, tile_rects)
        if collisions['bottom'] == True:
            air_timer = 0
            vertical_momentum = 0
        else:
            air_timer += 1
        spike_coll = collision_test(player.rect, spike_list)
        if len(spike_coll) != 0 :
            dead()
            # game over func

        if player.rect.y > WINDOW_SIZE[1]:
            dead()
            #game over func
        if current_level == 5:
          if player.rect.colliderect(portal_1.hitbox):
              player.rect.x = 260
              player.rect.y = 40+ 18
          if player.rect.colliderect(portal_3.hitbox):
              player.rect.x = 160
              player.rect.y = 280 + 18     
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    moving_right = True
                    player.animate("right")
                if event.key == K_LEFT:
                    moving_left = True
                    player.animate("left")
                if event.key == K_UP:
                    if air_timer < 6:
                        if r == True:
                            y = pygame.mixer.Sound("gameAssets\jump.ogg")
                            pygame.mixer.Sound.play(y)
                        else:
                            pass
                        vertical_momentum = -5
                        player.animate("pause")
                if event.key == K_p:
                    pause = True
                    paused()
                    
            if event.type == KEYUP:
                player.animate("stop")
                if event.key == K_RIGHT:
                    moving_right = False

                if event.key == K_LEFT:
                    moving_left = False

        # Drawing
        playerGroup.draw(display)
        playerGroup.update(0.5)
        pygame.display.flip()

        if player.rect.colliderect(door1):   
            if current_level == 1:           
              seconds = scoreclock.tick()/1000.0
              score1 = scorecalc(seconds,9,14,star_count)
              player_prog = '1'
              UPDATE(player_prog,score1)
              level_end(score1,star_count,seconds)

            if current_level == 2:
                seconds = scoreclock.tick()/1000.0
                score2 = scorecalc(seconds,9,14,star_count)
                player_prog = '2'
                UPDATE(player_prog,score2)
                level_end(score2,star_count,seconds)
        
            if current_level == 3:
                seconds = scoreclock.tick()/1000.0
                score3 = scorecalc(seconds,13,20,star_count)
                player_prog = '3'
                UPDATE(player_prog,score3)
                level_end(score3,star_count,seconds)

            if current_level == 4:
                seconds = scoreclock.tick()/1000.0
                score4 = scorecalc(seconds,13,20,star_count)
                player_prog = '4'
                UPDATE(player_prog,score4)
                level_end(score4,star_count,seconds)

            if current_level == 5:
                seconds = scoreclock.tick()/1000.0
                score5 = scorecalc(timer,13,20,star_count)
                player_prog = '5'
                UPDATE(player_prog,score5)
                level_end(score5,star_count,timer)#game_comp()
        #add door to complete level
        screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0, 0))
        pygame.display.update()
        clock.tick(60)
        
entry()
