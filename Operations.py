filename = input("Enter filename: ")
word = input("Enter word to count: ")

with open(filename) as f:
    lines = f.readlines()

N = int(input("How many lines to display? "))
print("First", N, "lines:")
print("".join(lines[:N]))

count = sum(line.count(word) for line in lines)
print("Frequency of word =", count)
