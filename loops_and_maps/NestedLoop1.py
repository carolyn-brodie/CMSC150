##How can we display the first m multiples of the numbers 1 through n?
##E.g. if n = 4 and m = 5
##  1 2 3 4 5
##  2 4 6 8 10
##  3 6 9 12 15
##  4 8 12 16 20

##Let's look at the case where n is 3 and m is 5 just to be easier
####First line - First m multiples of 1
for col in range(1,6):
    print(col, end = " ")
print()
##
####Second line - first m multiples of 2
##for col in range(1, 6):
##    print(2*col, end = " ")
##print()
##
####Third Line
##for col in range(1,6):
##    print(3 * col, end = " ")
    

##Generalize
##for row in range(1,3+1):
##    for col in range(1,5+1):
##        print(row * col, end = " ")
##    print()

##Generalize fully
##n = 4
##m = 5
##for row in range(1, n+1):
##    for col in range(1, m+1):
##        print(row * col, end = " ")
##    print()
