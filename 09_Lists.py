
# define a list
modules = ['Java', "Python", "JavaScript", "PHP", "Html", "CSS"]

print(modules)

# access an item using an index
print(modules[0])

# return part of an array --returns a new list

print(modules[1:4])

# write a program to find the largerst number in a list

numbers = [5, 2, 1, 7, 4]

# add items
numbers.append(13)
print(numbers)

# add at the begining or in between
numbers.insert(2, 90)

print(numbers)

# remove an element
numbers.remove(4)
print(numbers)

# remove all items
# numbers.clear()
# print(numbers)

# remove the last item
numbers.pop()

# check for existende
print(40 in numbers)

# length of a list
print(len(numbers))

# occurrence of an item in a list
print(numbers.count(2))

# write a program to remove duplicates in a list
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
