# how to make a list without worrying about functions



def createList(number):
    outList = []
    for element in range(number):
        outList.append(number)
    return outList


print(createList(3))