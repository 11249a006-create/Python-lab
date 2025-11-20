s = input("Enter a sentence: ")

words = len(s.split())
digits = sum(c.isdigit() for c in s)
upper = sum(c.isupper() for c in s)
lower = sum(c.islower() for c in s)

print("Words:", words)
print("Digits:", digits)
print("Uppercase:", upper)
print("Lowercase:", lower)
