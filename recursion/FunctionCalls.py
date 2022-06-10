
def function1(x):
    print("function1",x)
    function2(10)

def function2(x):
    print("function2",x)
    function3(20)

def function3(x):
    print("function3", x)


def main():
    x = 100
    function1(1)
    print("Finished",x)

if __name__ == "__main__":
    main()