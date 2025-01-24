def sum_of_factors(n):
    total = 0
    for i in range(1, n + 1): 
        if n % i == 0: # checks if the numbers are divisible if so then it is added to the total 
            total += i
    return total

num = int(input("Enter a number: "))
print(f"The sum of the factors of {num} is: {sum_of_factors(num)}")
