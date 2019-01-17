# Colin and Dana

from pprint import pprint
import csv
import json

#Read vegtables.csv into a variable called vegtables.

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegtables = [dict(vegtable) for vegtable in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)

#print(vegtables)


#Group vegtables by color as a variable vegtables_by_color.
vegtables_by_color = {}
for vegtable in vegtables:
	color = vegtable['color']
	if color in vegtables_by_color:
		vegtables_by_color[color].append(vegtable)
	else:
		vegtables_by_color[color] = [vegtable]
pprint(vegtables_by_color)

#Output vegtables_by_color into a json called vegtables_by_color.json.
with open('vegtables_by_color.json', 'w') as f:
	json.dump(vegtables_by_color, f, indent=2)