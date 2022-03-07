student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     student_grades = [key]
#     print(key)
#     print(student_scores[key])

#for i in range(len(student_scores)):
#    print(i)

for key in student_scores:
    #print(f"hello {key}")
    #student_grades[key] = i
    print(key)
    print(student_scores[key])
    number = student_scores[key]
    if number > 91 and number < 100:
        print("Outstanding")
    elif number > 81 and number < 90:
        print("Exceeds Exp")
    elif number > 71 and number < 80:
        print("Acceptable")
    else :
        print("Fail")

#add teh stuff in the new dict


# 🚨 Don't change the code below 👇
print(student_grades)