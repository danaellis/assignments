#read name.txt into a variable my_name
with open('name.txt') as f:
	my_name = f.read()

#construct greeting

greeting = "Hello my name is " + my_name + "."
print(greeting)

#write greeting to a file
with open('hello.txt', 'w') as f:
    f.write(greeting)
    f.write('\n')

