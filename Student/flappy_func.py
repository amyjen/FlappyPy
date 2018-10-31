import os
import pgzero
from pgzero import actor
from random import randint

os.environ['SDL_VIDEO_WINDOW_POS']='%d,%d'%(30,30)
WIDTH = 0
HEIGHT = 0
pipe_gap=180

def animate(bird):
    if bird.image == 'birddead':
        bird.image = 'bird0'
    else:
        image_num = int(bird.image[-1])
        image_num = (image_num + 1) % 4
        bird.image="bird"+str(image_num)

def move_ground(grounds):
    WIDTH = 400
    HEIGHT = 708
    grounds_width = 0
    if len(grounds) == 0:
        grounds.append(actor.Actor('ground',bottomleft = (0,HEIGHT)))
    for ground in grounds:
        ground.x-=3
        if ground.right < -10:
            grounds.remove(ground)
    for ground in grounds:
        grounds_width += ground.right - ground.left
    while grounds_width < WIDTH * 2:
        new_ground = actor.Actor('ground',bottomleft = grounds[-1].bottomright)
        grounds.append(new_ground)
        grounds_width+=grounds[0].right - grounds[0].left
def pass_pipe(pipes):
    in_pipe = False
    for pipe_pair in pipes:
        for pipe in pipe_pair:
            if pipe.right < 0:
                pipes.remove(pipe_pair)
                break
            if pipe.x == 80:
                return True
    return False

def spawn_pipes(pipes):
    WIDTH = 400
    HEIGHT = 708
    top = actor.Actor('top')
    bottom = actor.Actor('bottom')
    gap = 180
    top.bottom = randint(75,HEIGHT-200-gap)
    top.x = 800
    bottom.top = gap + top.bottom
    bottom.x = 800
    pipes.append((top,bottom))
    return pipes

def get_record():
    filename = os.getcwd() + r'\FlappyPy\Instructor\highscore.txt'
    with open(filename, 'r') as file:
        return int(file.readline())
def set_record(score):
    filename = os.getcwd() + r'\FlappyPy\Instructor\highscore.txt'
    with open(filename, 'w') as file:
        file.write(str(score))

def draw_score(screen, score):
    screen.draw.text(str(score), (WIDTH/2, 25), color = (255,255,255))
def draw_highscore(screen, highscore):
    screen.draw.text("highscore: "+str(highscore), (WIDTH/2, 5), color = (255,255,255))
