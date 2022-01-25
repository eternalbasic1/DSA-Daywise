a = "AGGTAB"
b = "GXTXAYB"
len_a = len(a)
len_b = len(b)
t = [[-1 for i in range(len_b+1)]for j in range(len_a+1)]
# for i in range(len_a +1):
#     for j in range(len_b+1):
#         print(t[i][j])
#     print()

def LCS(a,b,len_a,len_b):
    if len_a == 0 or len_b == 0:
        return 0
    if t[len_a][len_b] !=-1:
        return t[len_a][len_b]
    if a[len_a-1] == b[len_b-1]:
        t[len_a][len_b] =  1+LCS(a,b,len_a-1,len_b-1)
        return t[len_a][len_b]
    else:
        t[len_a][len_b] = max(LCS(a,b,len_a,len_b-1),LCS(a,b,len_a-1,len_b))
        return t[len_a][len_b]

maximum = LCS(a,b,len_a,len_b)
print(maximum)

# print(t[len_a][len_b])
#
# print()
for i in range(len_a +1):
    for j in range(len_b+1):
        print(t[i][j],end=' ')
    print()