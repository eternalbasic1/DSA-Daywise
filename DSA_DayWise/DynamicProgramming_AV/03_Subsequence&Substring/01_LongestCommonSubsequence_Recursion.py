a = "AGGTAB"
b = "GXTXAYB"
len_a = len(a)
len_b = len(b)

def LCS(a,b,len_a,len_b):
    if len_a == 0 or len_b == 0:
        return 0
    if a[len_a-1] == b[len_b-1]:
        return 1+LCS(a,b,len_a-1,len_b-1)
    else:
        return max(LCS(a,b,len_a-1,len_b) , LCS(a,b,len_a,len_b-1))
number = LCS(a,b,len_a,len_b)
print(number)