# Using conditional statements, check if the number is:
num = int(input("Enter a number: "))

# #  - Even or Odd.
if num % 2 == 0:
    print(num, "is an Even number.")
else:
    print(num, "is an Odd number.")

# #  - Positive, Negative, or Zero.
if num > 0 :
    print(num, "is a positive number.")
elif num < 0 : 
    print(num, "is a negative number.")
else: 
    print(num,"number is zero.")


#  - Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both 
#    check all the cases and print statement for each case.


if num % 2 == 0 and num % 3== 0:
    print(num, "is divisible by '2'and'3'.")
   
elif num % 2 == 0:
    print(num, "is divisible by '2'.")
    print("It's not divisible by '3'.")
elif num%3 == 0:
    print(num, "is divisible by '3'.")
    print("It's not divisible by '2'.")
else:
    print(num, "is not divisible by both '2' and '3'.")


#  - Take the user age.
#   -- If the age is 18 or above:
#   -- Ask if they have a nationality of "Pakistani".
#     ---If yes, print "You are eligible to vote."
#     ---If no, print "Please obtain a valid ID to vote."
user = int(input("Enter your Age: "))
if user >= 18: 
    nation = input("Do you have a valid pakistani nationality? (Yes/No):" )
    if nation.lower() =="yes":
        print("You are eligible to vote.")
    elif nation.lower() == "no":
        print("Please obtain a valid ID to vote.")
else:
    print("You are not eligible to vote.")
    






#  - Write a program that takes the age of a person as input and determines whether they are a child
#    (0-12 years), teenager (13-19 years), adult (20-59 years), or senior citizen (60 years and above)
#  - Enter a month (as a number between 1 and 12). Print the number of days in that month. 
#    Assume a non-leap year.
#  - Check if a year is a leap year or not.
age = int (input("Enter your age:"))
if age == 0 and age <= 12:
    print("You are a child.")
elif age >= 13 and age <=19: 
    print("You are a teenager")
elif age >= 20 and age <=59: 
    print("You are an adult")
elif age >= 60 :
    print("You are a senior citizen")
else:
    print("Invalid age")


