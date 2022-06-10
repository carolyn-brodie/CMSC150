
def mystery1(x, y):
    if (y == 0):
        return 1;
    elif (y < 0):
        return 1 / mystery1(x,-y)
    else:
        return x * mystery1(x, y-1)


print(mystery1(2,3))

