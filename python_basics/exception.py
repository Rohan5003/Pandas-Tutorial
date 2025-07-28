# try:
#     num = int(input("Enter a number: "))
#     print("100 /", num, "=", 100 / num)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Please enter a valid number.")

class TooYoungError(Exception):
    pass

age = int(input("Enter your age: "))
try:
    if age < 18:
        raise TooYoungError("You must be 18 or older.")
    else:
        print("Access granted.")
except TooYoungError as e:
    print("Custom Error:", e)

