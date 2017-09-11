import pygame as pg
vec = pg.math.Vector2

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DRED = (139,0,0)
YELLOW = (255, 255, 0)
BROWN = (106,55,5)
# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Manor of Terror"
BGCOLOR = DRED
TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'gbrick.jpg'

# Player settings

PLAYER_SPEED = 300.0
PLAYER_ROT_SPEED = 250.0
PLAYER_IMG = 'smgh.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35) #size of rectangle for player
BARREL_OFFSET = vec(30, 10)  #where bullets spawn from
PLAYER_HEALTH = 100
#Gun Settings
BULLET_IMG = 'Bullet2.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 20
GUN_SPREAD = 5
BULLET_DAMAGE = 25
# ZED SETTINGS
ZED_IMG = 'ZED.png'
ZED_SPEEDS = [150,100,75,200,300]                #must add friction             #different speeds can be selected by the computer. randomized
ZED_HIT_RECT = pg.Rect(0,0,30,30)
ZED_HEALTH = 100
ZED_DAMAGE =  10
ZED_KNOCKBACK = 20
AVOID_RADIUS = 50



