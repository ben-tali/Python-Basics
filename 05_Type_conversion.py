# write a program to get the year you were born in
#yob = input("Tell me your year of birth")


# calculate the age
#age = 2021 - yob
#print(f"You are {age} old")
#print(type(yob))
#age = 2021 - int(input("Tell me your year of birth"))


# write a program to ask  a user to enter their weight in pounds and convert it into a kg
# 1lb = 0.45kg
change_to_kilograms = True
change_to_pounds = True

pounds = float(input('Enter weight in Pounds(Lbs) to Convert into Kilograms:'))
kilo_grams = pounds * 0.453592


kilograms = float(input("Enter weight in kilograms(Kgs) to convert into Pounds:"))
pounds = kilograms / 0.453592

if change_to_kilograms and change_to_pounds:
    print(pounds," you (Lbs) are", kilo_grams, "Kilograms (Kgs)")
else: 
     print(kilograms,"you (Kgs) are", pounds, "Pounds (Lbs)") 







