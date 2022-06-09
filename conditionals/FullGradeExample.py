
## Assign grade based on the score

## Ask user to enter a score
score = int(input("Enter the score: "))

if score > 90:
    print("Your grade is an A.")
    print("Congratulations")
elif score > 80:
    print("Your grade is a B.")
    print("You missed an A by", 91 - score)
elif score > 70:
    print("Your grade is a C.")
    print("You missed a B by", 81 - score)
elif score > 60:
    print("Your grade is a D.")
    print("You missed a C by", 71 - score)
else:
    print("Your grade is an E.")





# ## Alternative spacing
# if grade > 90: print("Your grade is an A.")


print("Thank you for entering your grade")