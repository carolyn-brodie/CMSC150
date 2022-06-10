def swap(a, b):
    a, b = b, a
    print("inside function", a,b)

x = 0
y = 1
swap(x, y)
print("out function", x,y)