

theList = [1, 5, 2, 9]
totalsList = []
total = theList[0]
for index in range(1,len(theList)):
    total += theList[index]
    totalsList.append(total)

print(totalsList)