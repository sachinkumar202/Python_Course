# What is Python?
# Python is a popular programming language. Its was created by Guido van Rossum, and released in 1991.
# It is used for
# Web Developement(Server-Side)
# Software Development
# Mathematics
# System Scripting, etc.


# Q1. Print! Hello World.
print("Hello! Python")

# Q2. Print \n
print("\\n")

# Q3. Print Your Name
print('Sachin Kumar')

# Q4. Write a Python Program which accepts the radius of a circle from the user and compute the area?
import math

# Get the radius of the circle from the user.
radius = float(input("Enter the radius of the circle: "))

# Compute the area of the circle.
area = math.pi * radius ** 2

# Print the area of the circle.
print("The area of the circle is", area, "square units.")

# Q4. Write a Program to get the volume of a sphere with radius 6?
import math

radius = 6
volume = (4 / 3) * math.pi * radius ** 3

print("The volume of the sphere is", volume)

# Q5. Write a Program to calculate the sum of three equal numbers, and the result is the three times of their sum?
# This Python program calculates the sum of three equal numbers and returns the result as three times their sum.

# Get the three numbers from the user.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Check if the numbers are equal.
if num1 == num2 and num2 == num3:
    # Calculate the sum of the three numbers.
    sum = num1 + num2 + num3

    # Calculate the result as three times their sum.
    result = 3 * sum

    # Print the result.
    print("The sum of the three numbers is", sum)
    print("The result is", result)
else:
    # Print an error message.
    print("The numbers are not equal. Please enter three equal numbers.")



# Q6. Write a program that will accept the base and height of a triangle and compute the area?
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area of the triangle
area = 0.5 * base * height

# Print the area of the triangle
print("The area of the triangle is", area, "square units.")


# Q7. Write a program to solve (x+y)*(x+y)?
x = int(input('Enter x value :'))
y = int(input('Enter y valur : '))

# write the formula
a = (x+y)*(x+y)

# print a
print('Answer is :',a)



