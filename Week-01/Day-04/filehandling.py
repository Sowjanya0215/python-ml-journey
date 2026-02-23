#write---------
with open("practice.txt", "w") as f:
    name = input("Enter your name: ")
    f.write(name)

print("Saved successfully")

#Append-----
with open("practice.txt", "a") as f:
    marks = input("Enter your marks: ")
    f.write("\nMarks: " + marks)

print("Data added")

#Read Full File-------
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

#read line
with open("practice.txt", "r") as f:
    for line in f:
        print(line.strip())



