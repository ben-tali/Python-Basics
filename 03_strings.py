# declare a string
course_name = "Pythons's Basics"

# multilime strings
message = ''' 
I wanted to say,
We have goals we are trying to acheive.
But the person we are right now,
is not the person we need to be,
when we reach the finish line to our goals.
'''
print(message)


# get a character in a string by index
p = course_name[0]
print(p)

# get a character from the end
print(course_name[-1])

# extract some characters from a string
print(course_name[2:5])

# formatted strings --dynamically generate text

first_name = "Jack"
last_name = "Sparrow"

# way 1
message = first_name + " [" + last_name + " ] is a Software Developer"

print(message)

message = f"{first_name} [{last_name}] is a Software developer "
print(message)


# string functions
# len
# upper
# lower
# in
