test = {"A" : 1, "B" : 2}
print(test["B"])

##Change a value
test["A"] = 2
print(test)

## Add a new key / value pair
test["C"] = 3
print(test)

#print(test["D"])

if "D" in test:
    print(test["D"])
else:
    print("Not found")

print(test["B"] + test["C"])

del test["B"]

print(test)

for key in test:
     print(key)

for key, value in test.items():
      print(key, "->", value)

total = 0
for value in test.values():
	total += value

print(total)





