
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    
def main():
    student = get_student()
    print(f"{student.name} from {student.house}, gender: {student.gender}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    student.gender = "male"
    return student


if __name__ == "__main__":
    main()