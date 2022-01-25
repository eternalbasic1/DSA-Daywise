a = 'AABEBCDD'
b = 'AABEBCDD'

t = [[0 for i in range(len(b)+1)]for j in range(len(a)+1)]

for i in range(len(a)+1):
    for j in range(len(b)+1):
        if i == 0 or j == 0:
            t[i][j] = 0
            continue
        if a[i-1] == b[j-1] and i!=j:
            t[i][j] = 1+t[i-1][j-1]
        else:
            t[i][j] = max(t[i-1][j],t[i][j-1])

print(t[len(a)][len(b)])