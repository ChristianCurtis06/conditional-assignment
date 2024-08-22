# Task 1: Leap Year Checker
year_input = int(input("Enter a year (ex. 2024): "))
leap_year = year_input % 4 == 0
cent_year = year_input % 100 == 0
four_year = year_input % 400 == 0

if leap_year and not cent_year:
    print(year_input, "is a leap year!")
elif four_year:
    print(year_input, "is a leap year")
else:
    print(year_input, "is not a leap year!")