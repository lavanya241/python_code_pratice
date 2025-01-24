def gcd(a, b):
    while b: # replaces b with the remainder and the loop continues till b becomes 0
        a, b = b, a % b 
    return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")
