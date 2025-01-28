#The Fibonacci series
n = int(input("enter the number"))
a, b = 0, 1
print(a, b, end=" ")
for _ in range(n - 2):  # (n-2) because the first two terms are already printed
    a, b = b, a + b
    print(b, end=" ")
