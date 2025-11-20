def fib(n):
    if n <= 0:
        return "Invalid Input"
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a+b
    return a

N = int(input("Enter N: "))
print("Fibonacci Number =", fib(N))
