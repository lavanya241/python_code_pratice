"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one."""
input_string = input("enter the numbers
nums = list(map(input_string.spilt()))
def Single_num(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print("The single number is:", find_single_number(nums))
