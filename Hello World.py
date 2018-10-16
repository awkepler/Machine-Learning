print("Hello World")


def add_numbers(a, b):
    print(a+b)


add_numbers(2, 3)


name = "Sheetal!"
machine = "Amit"
print("Nice to meet you {0}. I am {1}".format(name, machine))

print(str(name))


number = 5
if number == 5:
    print("number is 5")
else:
    print("number is not 5")


student_name = ["Amit", "Sheetal", "Prasha", "Saiyansh"]
print(student_name[0])

print(student_name)

print(student_name[1:])

print(student_name[1:-1])


for name in student_name:
    print("student name is {0}".format(name));


for index in range(2, 12, 2):
    print(index)


for index in range(2, 12, 2):
    if index == 10:
        print("found {0}".format(index))
        break
    else:
        print("number is {0}".format(index))


for index in range(2, 12, 2):
        if index == 10:
            continue
            print("found {0}".format(index))
        else:
            print("number is {0}".format(index))


student = {
    "name": "Amit",
    "student id": 15163,
    "feedback": None
}

students = [{
    "name": "Amit",
    "student id": 15163,
    "feedback": None
},
    {
    "name": "Sheetal",
    "student id": 15164,
    "feedback": None
},
    {
    "name": "Prasha",
    "student id": 15165,
    "feedback": None
}]

try:
    last_name = student["last_name"]
except KeyError as error:
    print("Error finding last name")
    print(error)








