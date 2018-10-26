import pgzrun #must be include in every pygame

event = "event detected" #create variable called event thats used to show when draw() is called
step = 0 #step is used

def draw(): #called everytime an event occurs (when another pygame method such as update(), on_mouse_up(), etc is called)
    global event #next two lines runas
    print(event)

def update(): #runs 60 times per second, uncomment/comment this to demonstrate draw() method
    global step
    print(step) #prints times its run
    step += 1 #increments step


'''
explain how these two methods work (on mouse up and mouse down)

also explain how the pygame cordinates are set up on screen:
---------------
| (0,0) -> x  |
| |           |
| V           |
| y           |
---------------
zero 0 is in upper left corner

'''

def on_mouse_down(pos):
    print("down at",pos)
def on_mouse_up(pos):
    print("up at",pos)


pgzrun.go() #must be include in every pygame
