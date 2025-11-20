t1 = float(input("Enter Test 1 marks: "))
t2 = float(input("Enter Test 2 marks: "))
t3 = float(input("Enter Test 3 marks: "))

best_two = sorted([t1, t2, t3], reverse=True)[:2]
avg = sum(best_two) / 2

print("Best two average =", avg)
