s1 = "hello"
s2 = -1
strrev = []
for i in range(len(s1)):# iterates the character one by one
    strrev.append(s1[s2])
    s2 -= 1
    i -= 1
rev = "".join(strrev)# this joins the list into a string
print("the revesed String is:",rev)

#shortest method to find the revesed string is
print("the shortest method is :",s1[::-1])
