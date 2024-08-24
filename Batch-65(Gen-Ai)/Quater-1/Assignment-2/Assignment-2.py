# Qno.1---Calculate your age based on the current year and your birth year.

birthYear =int(input("Enter Your Birth Year: "))
currentYear = int(input("Enter Current Year : "))
result = "Your Age is: "+ str(currentYear-birthYear)
print(result)  

# Qno.2---Write a program that calculates the area of a rectangle using length and width variables.

lenght = int(input("Enter Lenght of rectangle: "))
width = int(input("Enter the width of rectangle: "))
Ans = "The Area of rectangle is: "+str(lenght*width) 
print(Ans)

# Qno.3---Write a program that calculates the area of a circle.

radius = int(input("Enter the radius of circle: "))
Answer = "The area of circle is: "+str(3.141592*radius)
print(Answer)

#  Qno.4---Create a program that converts a temperature from Fahrenheit to Celsius 
#          and vice versa using a variable.

print("Temperature converter Celsius to Fahrenheit")
celsius = int(input("Enter the temperature in 'Celsius': "))
Ans1 = "The temperature in 'Fahrenheit': "+str((celsius*9/5)+32)
print(Ans1)
print("Temperature converter Fahrenheit to Celsius")
fahrenheit = int(input("Enter the temperature in 'Fahrenheit': "))
Ans2 = "The temperature in Celsius is: "+str((fahrenheit-32)*5/9)
print(Ans2)


# Qno.5---Convert a given number of seconds into minutes and seconds using variables

print("Second to Minute Converter")
time = int(input("Enter your time in minutes: "))
print("Your time in seconds is: ",(time*60))

# Qno.6---Write a program that calculates the percentage.

print("Percentage Calculator")
number1=int(input("Enter number of which you find percentage: "))
number2 = int(input("Enter total amount: "))


# Qno.7---Write a program that calculates the BMI using height (in meters) 
#         and weight (in kilograms) variables.

height = float(input("Enter your height in metres: "))
weight = int(input("Enter your weight in kilograms: "))
print("Your BMI is: ",weight/height**2,"kg/m2")

# Qno.8---Write a program that calculates the volume of a cylinder using the formula .

height = int(input("Enter the height of cylinder: "))
radius = int(input("Enter the radius of cylinder: "))
pi = 3.14
print("The volume of cylinder is: ",pi*radius**2*height)



