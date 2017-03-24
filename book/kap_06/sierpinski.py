def sierpinski(x):
    if x < 5: return
    fd(x)
    right(120)
    fd(x)
    right(120)
    fd(x)
    right(120)
    sierpinski(x / 2)
    fd(x / 2)
    sierpinski(x / 2)
    back(x / 2)
    right(60)
    fd(x / 2)
    left(60)
    sierpinski(x / 2)
    right(60)
    back(x / 2)
    left(60)
    return


speed(0)
hideturtle()
left(60)
sierpinski(200)
