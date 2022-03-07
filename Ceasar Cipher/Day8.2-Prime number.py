# Write your code below this line 👇
import math
prime_numb = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def prime_checker(number):
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
        if is_prime:
            print(" prime ")
        else:
            print("not prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)