import turtle as draw

draw.speed(0)
draw.up()
draw.goto(-200, 0)
draw.down()


def xuehua(forward, n):
    if n == 0:
        draw.fd(forward)
    else:
        for i in [0, 60, -120, 60]:
            draw.left(i)
            xuehua(forward / 3, n - 1)


draw.color("red", "pink")
draw.begin_fill()
for i in range(3):
    xuehua(300, 3)
    draw.right(120)

draw.hideturtle()
draw.end_fill()
draw.done()
