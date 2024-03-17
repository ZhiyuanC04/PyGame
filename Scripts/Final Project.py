

import uvage
import random

camera = uvage.Camera(800, 600)
num_n_floors = 500
n_floor = []
y_value = 0
for n in range(num_n_floors):
    y_value += 150
    x = random.randrange(60, 740)
    n_floor.append(uvage.from_color(x, y_value, "black", 1500, 20))
    n_floor.append(uvage.from_color(x, y_value, "black", 1500, 20))
wall1 = uvage.from_color(-10, 300, "black", 20, 600)
wall2 = uvage.from_color(810, 300, "black", 20, 600)
wall3 = uvage.from_color(400, 610, "orange", 1000, 20)
player = uvage.from_color(400, 380, "green", 20, 20)
player_score = 0
marker = uvage.from_color(400, -20, "black", 20, 20)
game_on = False
game_over = False
count = 0


def tick():
    global game_on, game_over, player_score, n_floor, count
    camera.clear("white")
    # The if function to open the game:
    if uvage.is_pressing("space"):
        game_on = True
    # Functions running after game on:
    if game_on:
        # Start moving the player.
        player.move_speed()
        # Making the "gravity" effect.
        player.yspeed += 0.3
        # Stop the ball when it touches the end of the screen.
        player.move_to_stop_overlapping(wall1)
        player.move_to_stop_overlapping(wall2)
        player.move_to_stop_overlapping(wall3)
        # Move walls upward, and make the wall down again when it reaches some x value to make the game endless.
        for i in n_floor:
            i.move(0,-3)
            if i.y < -100:
                i.move(0, 20000)
            if player.bottom_touches(i) or player.left_touches(i) or player.right_touches(i) or player.top_touches(i):
                player.move_to_stop_overlapping(i)
        # Stop the player if it touches the end of the screen.
        if not (player.left_touches(wall1)) or not (player.right_touches(wall2)):
            if uvage.is_pressing("a"):
                player.x -= 7
            if uvage.is_pressing("d"):
                player.x += 7
        # Couting the number at the left-bottom.
        count += .05
        if count >= 3:
            player_score += 1
            count = 0
        # A comparision to the mark to end the game.
        if player.y < marker.y:
            game_on = False
            game_over = True
    # The gameover and print the "Game Over" line.
    if game_over:
        camera.draw(uvage.from_text(400, 300, "Game Over", 50, "Blue", bold = True))
        if uvage.is_pressing("r"):
            player_score = 0
            game_over = False
            game_on = False
    # Camera to draw all things on the screen.
    for n in n_floor:
        camera.draw(n)
    camera.draw(uvage.from_text(30, 570, str(player_score), 50, "Red", bold = True))
    camera.draw(player)
    camera.draw(marker)
    camera.draw(wall1)
    camera.draw(wall2)
    camera.draw(wall3)
    camera.display()

ticks_per_second = 30
uvage.timer_loop(ticks_per_second, tick)























