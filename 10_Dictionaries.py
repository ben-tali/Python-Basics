# key value pairs
# define dicitionaries

student = {
    "name": "Jack Sparrow",
    "id": 1324,
    "age": 30,
    "is_cleared": True
}

# get a value by key
print(student.get("name"))

# supply a default
print(student.get("birthdate", "Jan 1 2008"))

# write a program that converts numerical digits to words

number = input("Phone:  ")

digit_word = {
    "1": "one",
    "2": "two",
    "3": "Three",
    "4": "Four"
}

output = ""
for num in number:
    output += digit_word.get(num, "!!") + "  "

print(output)
