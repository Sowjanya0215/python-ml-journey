# Student Record Manager

students = {}

# Add Student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    
    students[roll] = {
        "name": name,
        "marks": marks
    }
    
    print("Student added successfully!\n")


# View All Students
def view_students():
    if not students:
        print("No records found.\n")
        return
    
    for roll, details in students.items():
        print("Roll:", roll)
        print("Name:", details["name"])
        print("Marks:", details["marks"])
        print("-------------------")


# Search Student
def search_student():
    roll = input("Enter Roll Number to search: ")
    
    if roll in students:
        print("Name:", students[roll]["name"])
        print("Marks:", students[roll]["marks"])
    else:
        print("Student not found.\n")


# Update Marks
def update_marks():
    roll = input("Enter Roll Number to update: ")
    
    if roll in students:
        new_marks = int(input("Enter New Marks: "))
        students[roll]["marks"] = new_marks
        print("Marks updated successfully!\n")
    else:
        print("Student not found.\n")


# Main Menu
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice\n")
 
