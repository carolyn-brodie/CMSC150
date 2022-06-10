
## Method 1
animal = ["mammal", "bird", "reptile", "fish"]
numberOfSpecies =  [428, 784, 311, 1154]

print(numberOfSpecies[animal.index("reptile")] )

## Method 2
numberOfSpecies = [ ["mammal", 428], ["bird", 784], ["reptile", 311], ["fish", 1154]]
for element in numberOfSpecies:
	if element[0] == "reptile":
		print(element[1])

## Use a dictionary
numberOfSpecies = { "mammal" : 428, "bird" : 784, "reptile" : 311, "fish" : 1154 }
print(numberOfSpecies["reptile"])




