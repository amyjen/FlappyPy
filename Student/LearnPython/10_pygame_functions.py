import pgzrun #must be include in every pygame

def draw(): #called everytime an event occurs (when another pygame method such as update(), on_mouse_up(), etc is used)
    pass
def update(): #runs 60 times per second

def on_mouse_down(pos):
    print("mouse clicked (down)")
def on_mouse_up(pos):
    print("mouse unclicked (up)")

pgzrun.go() #must be include in every pygame
