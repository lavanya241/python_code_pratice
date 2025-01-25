def lcm(A, B):
    max_num = max(A, B) #checks for maximum number
    while True: # if max number is divisible by a and b then it is lcm of the num
        if max_num % A == 0 and max_num % B == 0:
            return max_num
        max_num += 1
A = 4
B = 5
print("LCM of", A, "and", B, "is:", lcm(A, B))
