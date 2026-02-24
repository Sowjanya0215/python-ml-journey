# Simple File-Based Student Report System

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = input("Enter marks: ")

        file = open("students.txt", "a")
        file.write(name + "," + marks + "\n")
        file.close()

        print("Student saved\n")

    elif choice == "2":
        try:
            file = open("students.txt", "r")
            data = file.readlines()
            file.close()

            for line in data:
                name, marks = line.strip().split(",")
                print("Name:", name)
                print("Marks:", marks)
                print("------")

        except FileNotFoundError:
            print("No records found\n")

    elif choice == "3":
        print("Program ended")
        break

    else:
        print("Invalid choice\n")
