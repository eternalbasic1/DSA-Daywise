a = "AGGTAB"
b = "GXTXAYB"
len_a = len(a)
len_b = len(b)
t = [[-1 for i in range(len_b+1)]for j in range(len_a+1)]
for i in range(len_a+1):
    for j in range(len_b+1):
        if i == 0 or j == 0:
            t[i][j] = 0
            continue
        if a[i-1] == b[j-1]:
            t[i][j] = 1+t[i-1][j-1]
        else:
            t[i][j] = max(t[i-1][j],t[i][j-1])
for i in range(len_a+1):
    for j in range(len_b+1):
        print(t[i][j],end=' ')
    print()
print(t[i][j])