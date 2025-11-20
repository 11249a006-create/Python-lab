n = input("Enter a number: ")

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

print("Digit Occurrences:")
for d in set(n):
    print(d, ":", n.count(d))
