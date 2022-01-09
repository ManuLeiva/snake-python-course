# #1. Create a greeting for your program.
# print("Hello to the people")
# #2. Ask the user for the city that they grew up in.
# city = input("Which is your city? \n")
# #3. Ask the user for the name of a pet.
# name_pet = input("Name of your Pet? \n")
# #4. Combine the name of their city and pet and show them their band name.
# print("Your band name is" + city + " " + name_pet)
# #5. Make sure the input cursor shows on a new line, see the example at:
# #   https://band-name-generator-end.appbrewery.repl.run/

# num_char = len(input("What is your name? "))
# print(type(num_char))
# new_char = str(num_char)
# print("Your name has " + new_char + " characters")


# 🚨 Don't change the code below 👇
#two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# print(type(two_digit_number))
# num_1 = two_digit_number[0]
# num_2 =  two_digit_number[1]
# result = int(num_1) + int(num_2)
# print(result)


# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# height_int = float(height)
# weight_int = int(weight)
#
# bmi = weight_int / (height_int**2)
#
# print(round(bmi,2))



#
# # 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
#
# #There are 365 days in a year, 52 weeks in a year and 12 months in a year
#
# age = int(age)
# days = 90*365 - age*365
# weeks = 90*52 - age*52
# months = 90*12 - age*12
#
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")




# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# result = number%2
#
# if result != 0:
#     print("This is an odd number.")
#
# else:
#     print("This is an even number.")




# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# bill = 0
#
# if size == 'S':
#     bill += 15
#     if add_pepperoni == 'Y':
#         bill += 2
# elif size == 'M':
#     bill += 20
#     if add_pepperoni == 'Y':
#         bill += 3
# else:
#     bill += 25
#     if add_pepperoni == 'Y':
#         bill += 3
# if extra_cheese == 'Y':
#     bill += 1
# print(f"Your final bill is: ${bill}.")

# import random
#
# random_int = random.randint(0,1)
# print(random_int)
# if random_int == 0:
#     print("Heads")
# else:
#     print("Tails")


# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# #Angela, Ben, Jenny, Michael, Chloe
# random_number = random.choice(names)
#
# print(f"{random_number} is going to buy the meal today!")




# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
#
# row = map[int(position[1])]
# row[int(position[0])] = 'x'
#
#
#
# #Write your code above this row 👆
#
# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

# import random
#
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# game = [rock, paper, scissors]
#
# machine_choice = random.randint(0,2)
#
# user_choice = input("What do you want to choose rock = 1 paper = 2 or scissors = 3 ? ")
# user_choice = int(user_choice)
# if user_choice == 1 and machine_choice == 1 or user_choice == 2 and machine_choice == 2 or user_choice == 3 \
#         and machine_choice == 3:
#     print("draw")
# elif user_choice == 1 and machine_choice == 2:
#     print(f"User choice is: {rock}")
#     print(f"Machine choice is: {paper}")
#     print("User wins")
# elif user_choice == 2 and machine_choice == 3:
#     print(f"User choice is: {paper}")
#     print(f"Machine choice is: {scissors}")
#     print("Machine wins")
# elif user_choice == 3 and machine_choice == 1:
#     print(f"User choice is: {scissors}")
#     print(f"Machine choice is: {rock}")
#     print("Machine wins")
# elif user_choice == 3 and machine_choice == 2:
#     print(f"User choice is: {scissors}")
#     print(f"Machine choice is: {paper}")
#     print("User wins")
# elif user_choice == 1 and machine_choice == 3:
#     print(f"User choice is: {scissors}")
#     print(f"Machine choice is: {paper}")
#     print("User wins")



# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
# #156 178 165 171 187
# #Write your code below this row 👇
#
# count = 0
# total_height = 0
# for height in student_heights:
#     count +=1
#     total_height = total_height + height
#
# result = int(total_height/count)
#
# print(result)

#
# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
#
# #78 65 89 86 55 91 64 89
# new_score = 0
# for score in student_scores:
#   if score > new_score:
#     new_score = score
#
# print(new_score)
#


# for i in range (1,101):
#   if i%3 == 0 and i%5 == 0:
#     print("fizzbuzz")
#   elif i%3 == 0:
#     print("fizz")
#   elif i%5 == 0:
#     print("buzz")
#   else:
#     print(i)

# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = []

for i in range(1, nr_letters+1) :
  new_letter = random.choice(letters)
  password.append(new_letter)

for i in range(1, nr_symbols+1) :
  new_letter = random.choice(numbers)
  password.append(new_letter)

for i in range(1, nr_numbers+1) :
  new_letter = random.choice(symbols)
  password.append(new_letter)

random.shuffle(password)
password_f = ''
for char in password:
  password_f += char
print(password_f)











