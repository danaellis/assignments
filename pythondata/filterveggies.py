#Dana and Colin
import csv
import json

#Read vegetables.csv into a variable called vegetables.

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = [dict(vegetable) for vegetable in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)

#print(vegetables)


#Loop through vegetables and filter down to only green vegtables using a whitelist.

green_vegetables = []
whitelist = ['green']
for vegetable in vegetables:
	if vegetable['color'] in whitelist:
		green_vegetables.append(vegetable)

#Print veggies to the terminal
print(green_vegetables)

#Write the veggies to a json file called greenveggies.json

with open('greenveggies.json', 'w') as f:
	json.dump(green_vegetables, f, indent=2)