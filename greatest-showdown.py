# Task 1: Identify the Greatest
first_number = float(input("Enter a number: "))
second_number = float(input("Enter another number: "))
third_number = float(input("Enter a third number: "))

if second_number <= first_number >= third_number:
    largest_number = first_number
elif first_number <= second_number >= third_number:
    largest_number = second_number
elif first_number < third_number > second_number:
    largest_number = third_number

# Task 2: Identify the Smallest
if second_number >= first_number <= third_number:
    smallest_number = first_number
elif first_number >= second_number <= third_number:
    smallest_number = second_number
elif first_number > third_number < second_number:
    smallest_number = third_number

print("The smallest number is " + str(smallest_number) + ". The largest number is " + str(largest_number) + ".")