while true:
    age = int(input("Enter your age: "))
    if age < 13:
        print("Call your legal guardian")
    elif age >= 13 and age < 18:
        print("Teenager")
    else:
        print("Adult")