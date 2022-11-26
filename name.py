
# name = input("What's your name? ")

# file = open("names.txt", "a")
# file.write(name + "\n")
# file.close()

students = []

with open("names.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)


def get_name(student):
    return student["name"]

for student in sorted(students, key=sutdent["house"]):
    print(f"{student['name']} is in {student['house']}")