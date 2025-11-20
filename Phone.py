import re

pattern = r"\d{3}-\d{3}-\d{4}"
phone = input("Enter phone number: ")

if re.fullmatch(pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Format")
