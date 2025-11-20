def binary_to_decimal(b):
    return int(b, 2)

def octal_to_hex(o):
    return hex(int(o, 8))[2:].upper()

b = input("Enter binary: ")
o = input("Enter octal: ")

print("Decimal:", binary_to_decimal(b))
print("Hexadecimal:", octal_to_hex(o))
