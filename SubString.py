def substrings(s):
    substrings = []
    for i in range(len(s)):# ending index range 0 to len(s) - 1
        for j in range(i + 1, len(s) + 1): # ending index range i+1 to len(s)+1
            substrings.append(s[i:j])
    return substrings

s1 = "sak"
print(substrings(s1))

        
