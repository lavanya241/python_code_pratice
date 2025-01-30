def is_palindrome(s):
    # Clean the string and remove non-alphanumeric 
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is the same forward and backward
    return cleaned_s == cleaned_s[::-1]

# Example usage
s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

print(is_palindrome(s1))  # Output: True
print(is_palindrome(s2))  # Output: False
print(is_palindrome(s3))  # Output: True
