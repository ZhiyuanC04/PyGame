# Name: Zhiyuan Chang, Yuhao Niu
# Computing ID: vgs3qt, bhb9ba

# Description of the game: You're the player and you need to jump up and try to stay alive. Use "A" "D" and "Space"
# to control, going out of screen and the player will reappear from the other side. There's stars for player to
# collect.

# Changes from CP2: actually no changes, we finish this project directly without doing the CP2 since it's cancelled.

# 3 Basic features:
# User input: ADR and Space, keyboard inputs to control the player.
# Game over: When the player fall out of the screen from the bottom. The screen turns black and Game Over.
# Graphics/Images: Image of Player and Stars.

# 4 Additional features:
# Restart from Game Over: Press R to restart (R also to start the game).
# Sprite Animation: The player is a sprite animation, and he is running when player press A D or space.
# Collectibles: Stars are collectibles and when player touches the star collection will + 1.
# Timer: There is a timer to count how long the player survived.

import uvage
import random

camera = uvage.Camera(800, 600)
game_on = False
game_over = False
touching = True
need = True
facing_right = True
is_moving = False
n_floor = []
memory = []
player_score = 0
count = 0
ti = 0
frame = 0
number = 0
star_collected = 0

marker = uvage.from_color(400, 620, "green", 20, 20)
play1 = uvage.load_sprite_sheet("sprite sheet player.png", rows = 1, columns = 8)
player = uvage.from_image(400, 580, play1[0])
player.size = [50,50]
star1 = uvage.load_sprite_sheet("stars.png", rows = 1, columns = 1)
star = uvage.from_image(200, 560, star1[0])
star.size = [40, 40]
ground = uvage.from_color(400, 600, "orange", 1000, 20)

def floors_stars_creation():
    """
    To create random floors.
    :return:
    """
    global star1, memory
    global star, n_floor
    check = 0
    num_n_floors = 800
    y_value = 550
    for n in range(num_n_floors):
        y_value -= 75
        length = random.randrange(1, 3)
        for i in range(length):
            x = random.randrange(80, 720)
            n_floor.append(uvage.from_color(x, y_value, "black", 120, 20))
            check = random.randrange(1,10)
            if check == 5:
                memory.append([x, y_value - 30])

def starting_instruction():
    """
    Print the instructions before game starts. Press R to start.
    :return:
    """
    global game_on
    yes = True
    while yes:
        camera.clear("white")
        if not game_on:
            camera.clear("white")
            camera.draw(uvage.from_text(400, 200, "Press 'R' to start.", 50, "Blue", bold=True))
            camera.draw(uvage.from_text(400, 300, "Press 'A' 'Space' 'D' to move", 50, "Blue", bold=True))
            camera.draw(uvage.from_text(400, 400, "Jump up and stay ALIVE!", 50, "Blue", bold=True))
        yes = False

def player_related():
    """
    All player related code like movement and touch to stop.
    :return:
    """
    global game_on, touching, frame, is_moving, facing_right
    global player, ground, n_floor
    is_moving = False
    if game_on:
        player.move_speed()
        if player.x > 800:
            player.x = 0
        if player.x < 0:
            player.x = 800
        if player.bottom_touches(ground):
            player.move_to_stop_overlapping(ground)
            touching = True
        player.move_to_stop_overlapping(ground)
        for all in n_floor:
            if player.left_touches(all) or player.right_touches(all):
                player.move_to_stop_overlapping(all)
            if player.top_touches(all):
                player.move_to_stop_overlapping(all)
            if player.bottom_touches(all):
                player.move_to_stop_overlapping(all)
                touching = True
        player.yspeed += 0.7
        if not uvage.is_pressing("a") or not uvage.is_pressing("d") or not uvage.is_pressing("space"):
            is_moving = False
        if uvage.is_pressing("a"):
            if facing_right:
                facing_right = False
                player.flip()
            player.x -= 7
            is_moving = True
        if uvage.is_pressing("d"):
            if not facing_right:
                facing_right = True
                player.flip()
            player.x += 7
            is_moving = True
        if touching:
            if uvage.is_pressing("space"):
                is_moving = True
                player.speedy -= 16
                touching = False
        if is_moving:
            frame += .3
            if frame >= 8:
                frame = 0
            player.image = play1[int(frame)]
        if not is_moving:
            player.image = play1[0]

def camera_move():
    """
    Movement of floors and stars.
    :return:
    """
    global game_on, ti, need
    global marker
    if game_on:
        if need:
            ti += 1
        if ti >= 120:
            for floor in n_floor:
                floor.move(0, 1)
                if floor.y > 1000:
                    floor.move(0, -60550)
            ground.move(0, 1)
            star.move(0, 1)
            need = False

def timer_related():
    """
    The timer and count-up
    :return:
    """
    global game_on, count
    global player_score
    if game_on:
        count += 1
        if count >= 30:
            player_score += 1
            count = 0

def collectibles():
    """
    Stars as collectibles.
    :return:
    """
    global game_on, memory, number, star_collected
    global marker, star
    if game_on:
        if player.touches(star) or marker.y < star.y:
            star_collected += 1
            number += 1
            star.x = memory[number][0]
            star.y = memory[number][1]

def game_end():
    """
    Reset all values to original if game end.
    :return:
    """
    global game_on, game_over, need, ti, memory, star, star_collected
    global player_score, n_floor, marker, player
    if player.y > marker.y:
        game_on = False
        game_over = True
        camera.clear("black")
        camera.draw("Game Over", 50, "white", 400, 300)
        camera.draw("Press 'R' to restart", 50, "white", 400, 400)
        if uvage.is_pressing("r"):
            need = True
            game_on = True
            game_over = False
            ti = 0
            star_collected = 0
            player_score = 0
            star.x = 200
            star.y = 560
            ground.x = 400
            ground.y = 600
            player.x = 400
            player.y = 580
            player.speedy = 0
            memory.clear()
            n_floor.clear()
            floors_stars_creation()

def tick():
    """
    The function that will run. All other functions above is included inside. (except floor creation.)
    :return:
    """
    global game_on, game_over
    global n_floor, player, marker, star, ground, player_score, star_collected
    camera.clear("white")
    starting_instruction()
    if uvage.is_pressing("r"):
        game_on = True
        game_over = False
    player_related()
    camera_move()
    timer_related()
    collectibles()
    game_end()
    if game_on:
        camera.draw(player)
        camera.draw(marker)
        camera.draw(star)
        camera.draw(ground)
        for item in n_floor:
            camera.draw(item)
        camera.draw("Time Survived: " + str(player_score), 50, "black", [300, 30])
        camera.draw("Star Collected: " + str(star_collected), 30, "black", [600, 30])
    camera.display()

floors_stars_creation()

ticks_per_second = 30
uvage.timer_loop(ticks_per_second, tick)