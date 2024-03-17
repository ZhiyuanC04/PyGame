import uvage

camera = uvage.Camera(800,600)

p1 = uvage.from_color(100, 400, "red", 100, 100)

def tick():
    camera.clear("black")

    # #xspeed vs. x
    if uvage.is_pressing("right arrow"):
        p1.x += 5
        # p1.xspeed = 5
    # p1.move_speed()

    # # #yspeed vs. y
    if uvage.is_pressing("down arrow"):
        p1.y += 5
        # p1.yspeed = 5
    # print(p1.yspeed) #used to print out yspeed to show that you have to use move_speed with any xspeed or yspeed
    # p1.move_speed()

    camera.draw(p1)
    camera.display()


ticks_per_second = 30

# keep this line the last one in your program
uvage.timer_loop(ticks_per_second, tick)
