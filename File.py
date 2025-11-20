import re

filename = input("Enter filename: ")
text = open(filename).read()

phones = re.findall(r"\+?\d{10,13}", text)
emails = re.findall(r"[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]+", text)

print("Phone Numbers Found:", phones)
print("Emails Found:", emails)
