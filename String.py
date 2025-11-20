s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

similar = sum(c1 == c2 for c1, c2 in zip(s1, s2))
print("String similarity =", similar)
