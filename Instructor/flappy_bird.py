import pgzrun #do not remove and leave as first line of code
from flappy_func import *

WIDTH = 400
HEIGHT = 708
start_position=(WIDTH/5, HEIGHT/3)

frame=0
speed=0
is_down=False
started_game=False
ground=[]
pipes=[]
score=0
highscore=get_record()
game_over=False

bird = Actor('bird0')
bird.pos=start_position

def fall():
    global speed
    bird.y+= speed
    speed+=.5
    bird.angle = 3*(3-speed)#looks better

def move_pipes(pipes):
    for pipe_pair in pipes:
        for pipe in pipe_pair:
            pipe.x-=3

def hit_ground():
    for tile in ground:
        if tile.colliderect(bird):
            return True
    return False

def hit_pipe():
    for pipe_pair in pipes:
        for pipe in pipe_pair:
            if pipe.colliderect(bird):
                return True
    return False

def die():
    global frame,speed,is_down,started_game,ground,pipes,score,highscore,game_over
    frame=-60
    speed=-5
    is_down=False
    started_game=False
    #ground=[]
    #pipes=[]
    #score=0
    set_record(highscore)
    game_over=True

    sounds.die.play()
    bird.image = 'birddead'

def reset_game():
    global frame,speed,is_down,started_game,ground,pipes,score,highscore,game_over
    pipes=[]
    speed=0
    score=0
    game_over=False
    bird.image='bird0'
    bird.pos=start_position

def draw():
    screen.blit('background', (0,0))
    for pipe_pair in pipes:
        for pipe in pipe_pair:
            pipe.draw()
    for tile in ground:
        tile.draw()
    bird.draw()
    draw_score(screen,score)
    draw_highscore(screen,highscore)

def update():
    global frame,speed,is_down,started_game,ground,pipes,score,highscore,game_over
    frame+=1
    if not game_over:
        if keyboard.space:
            started_game = True
            if not is_down:
                speed = -10
                sounds.wing.play()
            is_down=True
        else:
            is_down=False
        if frame % 4 == 0:
            animate(bird)
        move_ground(ground)
    else:
        fall()
    if started_game:
        fall()
        move_pipes(pipes)
        if frame % 100 == 0:
            spawn_pipes(pipes)
        if pass_pipe(pipes):
            score+=1
            sounds.point.play()
        if (bird.top < 0 or hit_pipe() or hit_ground()):
            sounds.hit.play()
            die()
        if score > highscore:
            highscore = score
    if frame == 0:
        reset_game()

pgzrun.go() #do not remove and leave as last line of code
