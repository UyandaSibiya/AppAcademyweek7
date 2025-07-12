#Strings
message = "Bobs world is a wonderful place"

print(message)
print(message.strip())
print(message.lower())
print(message.split())

#Numeric Data

num = 3

print(type(num))

num2 = 3.14

print(type(num2))

#Variable 
my_variable = 10
total_count = 0
user = "John"

#Invalib
second_variable = 20
user_name = 20

#Operators

#Addition (+)
#Subtraction (-)
#Multiplication (*)
#Division (/)
#Modulus (%)
#Exponentiation (**)

y = 10 
x = 5

print(y + x)  
print(y - x)
print(y * x)
print(y / x)
print(y % x)
print(y ** x)  

#Operators with strings

str1 = "Hello"
str2 = "World"

print(str1 + " " + str2 + " " + str2 )
print(str1 * 3)

#Control Statements

num = -5 
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

#Contro; Staements

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")

#Loops
#Using a while loop to count from 1 to 5
count = 1

while count <= 5:
    print("Count is:", count)
    count += 1
    if count == 3:
        break

#loop control statements

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "banana":
        break  
    print(fruit)

print()

for fruit in fruits:
    if fruit == "date":
        continue  
    print(fruit)

print()

for fruit in fruits:
    if fruit == "cherry":
        pass  
    print(fruit)

