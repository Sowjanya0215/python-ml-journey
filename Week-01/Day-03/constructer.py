class Student(): #class
    name="raj"
s1=Student()     #object
print(s1.name) 

#constructer-------

class Student:    
 def __init__(self,name,marks):
    self.name=name
    self.marks=marks
    print("The Data")
s=Student("Ram",3)
print(s.name,s.marks) 
