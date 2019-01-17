import csv

# define list of vegetables
vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]


# write the vegetable (row) to a csv file
with open('vegetables.csv', 'w') as f:
    writer = csv.writer(f)
    #write header
    writer.writerow(['name', 'color'])
    #write data	
    # loop through each vegetable
    for vegetable in vegetables:
        name = vegetable['name']
        color = vegetable['color']
        length_of_name = len(vegetable['name'])
        writer.writerow([name, color, length_of_name])

