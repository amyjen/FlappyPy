import pgzrun #do not remove and leave as first line of code
from flappy_func import *

WIDTH = 400
HEIGHT = 708
start_position=(WIDTH/5, HEIGHT/3)
#global frame,speed,score,started_game,game_over,is_down,pipes,ground,highscore
frame = 0
speed = 0
score = 0
started_game = False
game_over = False
is_down = False
pipes = []
ground = []
highscore = get_high_score()

bird = Actor('bird0')
bird.pos=start_position

def fall():
    global speed
    bird.y+= speed
    speed+=.5
    bird.angle = 3*(3-speed)#looks better

def move_pipes():
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

def reset_game():
    global speed,frame,started_game,is_down,score,ground,highscore,game_over,pipes
    frame = -60
    speed = -5
    #score = 0
    started_game = False
    game_over = True
    is_down = False
    #ground removed
    #pipes removed
    set_high_score(highscore)

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
    global frame,speed,score,started_game,game_over,is_down,pipes,ground,highscore
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

        if pass_pipe(pipes):
            score+=1
            sounds.point.play()

        if (bird.top < 0 or hit_pipe() or hit_ground()):
            sounds.hit.play()
            sounds.die.play()
            bird.image = 'birddead'
            reset_game()
    else:
        fall()
    if started_game:
        if frame % 100 == 0:
            spawn_pipes(pipes)
        fall()
        move_pipes()
        if score > highscore:
            highscore = score

    if frame == 0:
        pipes=[]
        speed=0
        score=0
        game_over=False
        bird.image='bird0'
        bird.pos=start_position

pgzrun.go() #do not remove and leave as last line of code
