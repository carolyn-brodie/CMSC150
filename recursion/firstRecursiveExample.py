## First Recursion Example


def mystery(firstNumber, secondNumber):
    if firstNumber <= secondNumber:
        print(firstNumber, end = " ")
        mystery(firstNumber + 1, secondNumber)

##def mystery(firstNumber, secondNumber):
##    if firstNumber <= secondNumber:
##        print(firstNumber, end = " ")
##        mystery(firstNumber, secondNumber)
     


mystery(3, 6)
