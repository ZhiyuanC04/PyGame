# Basketball Frogger beginning code

import uvage
import random

screen_width = 800
screen_height = 600
camera = uvage.Camera(screen_width, screen_height)
score = 0
##############################  SCENERY  ##############################
# create boxes for background objects
#

court = uvage.from_image(screen_width // 2, screen_height // 2, 'uva_court.jpg')
court.scale_by(3)
court.rotate(90)


# create a function for drawing the scenery
#
def draw_scenery():
    # draw each scenery box
    camera.draw(court)


######################## INTERACTIVE COMPONENTS ########################
# create boxes that will be active
#
interactives = []

fan_sprite = uvage.load_sprite_sheet('person5.png', 1, 6)
# https://www.codeandweb.com/o/blog/2016/05/10/how-to-create-a-sprite-sheet/spritestrip-1536.png
fan = uvage.from_image(100, 300, fan_sprite[0])
fan.scale_by(0.35)
interactives.append(fan)

num_b_balls = 15
b_balls = []
sideline_width = 200
b_ball_sprite = uvage.load_sprite_sheet('b_ball4.png', 1, 1)
# b_ball_sprite_sheet from: https://www.clipartmax.com/max/m2H7Z5G6K9H7H7H7/
b_ball_image = 0
for i in range(num_b_balls):
    x = random.randrange(sideline_width, screen_width - sideline_width)
    y = random.randrange(100, screen_height)
    b_balls.append(uvage.from_image(x, y, b_ball_sprite[b_ball_image]))
# b_balls.append(gamebox.from_circle(x, y, 'OrangeRed1', b_ball_radius))

# color names at https://www.tcl.tk/man/tcl/TkCmd/colors.html
interactives += b_balls

for each in b_balls:
    speed = random.choice([-10, -8, -6, -4, 4, 6, 8, 10])
    each.speedy = speed


# create a function for drawing the interactives
#
def draw_interactives():
    global b_ball_image
    # respond to keys
    handle_keys()

    # move an interactive according to its speed
    for each in b_balls:
        if each.y < -20:
            speed = random.choice(range(4, 11))
            each.speedy = speed
            each.x = random.randrange(sideline_width, screen_width - sideline_width)
        elif each.y > screen_height + 20:
            speed = random.choice(range(-10, -3))
            each.speedy = speed
            each.x = random.randrange(sideline_width, screen_width - sideline_width)
        each.move_speed()
        fan.move_to_stop_overlapping(each)

    # draw each interactive box
    for each in interactives:
        camera.draw(each)


# handle keys used
def handle_keys():
    speed = 5
    if uvage.is_pressing("right arrow"):
        fan.x += speed
    if uvage.is_pressing("left arrow"):
        fan.x -= speed
    if uvage.is_pressing("up arrow"):
        fan.y -= speed
    if uvage.is_pressing("down arrow"):
        fan.y += speed


################################ STATS ################################

# update the stat boxes each loop - call from tick function
def draw_stats():
    global score
    score += 0.1
    camera.draw("Score:" + str(int(score)), 36, "blue", 65, 30)


############################### PHYSICS ###############################

# initialize physics variables
#
# update physics each loop

############################## MAIN LOOP ##############################

def tick():
    # clear camera
    camera.clear('black')

    # update the physics

    # draw the scenery
    draw_scenery()

    # draw the interactive components
    draw_interactives()

    # update the stats
    draw_stats()

    # show the updated scene
    camera.display()


# Start the main game loop
# redraw the scene 30 times per second, call the tick function
uvage.timer_loop(30, tick)
