# Third example

def divide_repeatedly(x):
    if x < 2:
        return 0
    else:
        return 1 + divide_repeatedly(x/2)


# Test
print(divide_repeatedly(12))
