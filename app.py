from math import * # importing more math methods


# drawing a shape
print("   /|\\")
print("  / | \\")
print(" /  |  \\")
print("/___|___\\")

# general introduction
character_name = "Tom"
character_age = "50"
is_male = True
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old. ")
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

# String Practice
phrase = "Python\n\"Practice\""
print(phrase + " is cool")
print(phrase.lower())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("Practice"))
print(phrase.replace("Python", "some other snake"))

# Number Practice
print(3 * 4.5)
print(3 * (4 + 5))
print(10 % 3) # finding the remainder
my_num = 5
print(str(my_num) + " my favorite number") # str method to change a number to a string
neg_num = -9
print(abs(neg_num)) # absolute value
print(pow(my_num, 6)) # power
print(min(4, 6)) # gets the minimum number
print(sqrt(36)) # can be used with the math import
