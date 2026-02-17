student={}
n=int(input("enter the number of students:"))
for i in range(n):
  name=input("enter name:")
  marks=int(input("enter the marks:"))
  student[name]=marks
total=sum(student.values())
avg=total/len(student)
print("the total marks:",total)
print("the average is:",avg)
top=max(student,key=student.get)
print("the top is:",top,"-", student[top])
