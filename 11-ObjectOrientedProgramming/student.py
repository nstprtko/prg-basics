# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.gender = "male"
    student2.name = "Olivia"
    student2.age = 21
    student2.gender = "female"
    student3.name = "Barbara"
    student3.age = 20
    student3.gender = "female"

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old')
    print(f'{student2.name}, {student2.age} years old')
    print(f'{student3.name}, {student3.age} years old')

if __name__ == "__main__":
    main()