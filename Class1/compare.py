# years=int(input("Enter number of years: "))
# choice=input("""
# 1 - Days
# 2 - Weeks
# 3 - Hours
# """)
# if choice == "1":
#     print(f"In {years} there are {365*years} days")
# elif choice == "2":
#     print(f"In {years} there are {52*years} weeks")
# elif choice == "3":
#     print(f"In {years} there are {365*24*years} hours")
# else:
#     print("Select a right choice")

# print("Enter your age: ")
# age=int(input())
# if age < 13 :
#     print("Ur a child")
# elif age >= 13 and age < 18:
#     print("Ur a teenager")
# elif age >= 18 and age < 65 or age >= 65:
#     print("Ur an adult")
# else:
#     print("Select a right choice")

print(""""
Enter your percentage: 
15% = Standard
18% = Good
20% = Great
ABOVE 20% = My hero

Enter: 
""")
percentage=int(input())
if percentage == 15 :
    print("Standard")
elif percentage == 18:
    print("Good")
elif percentage == 20:
    print("Great")
elif percentage > 20:
    print("My hero")
else:
    print("Not valid tip. Can't tip? Eat at home XD")
