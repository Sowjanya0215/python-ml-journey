try:
    num = int(input("Enter number: "))
    print(10 / num)
except:
    print("Something went wrong")

try:
    n=int(input('Enter number:'))
    print(10/n)
except ZeroDivisionError as e:
    print("Something went wrong.....Cannot divide by zero")
except ValueError as e:
    print("value error.....")    
finally:
    print("succesfullly executed")    

#Raising Your Own Exception-----

age = int(input("Enter age: "))

if age < 18:
    raise ValueError("Age must be 18 or above")

print("Eligible")
