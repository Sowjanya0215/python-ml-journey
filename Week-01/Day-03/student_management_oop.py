
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name :", self.name)
        print("Marks:", self.marks)
        print("-----------------")


students = []   

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = input("Enter marks: ")

        s = Student(name, marks)   
        students.append(s)         

        print("Student added successfully\n")

    elif choice == "2":
        if len(students) == 0:
            print("No students found\n")
        else:
            for s in students:
                s.display()

    elif choice == "3":s
        print("Program ended")
        break

    else:
        print("Invalid choice\n")
 
