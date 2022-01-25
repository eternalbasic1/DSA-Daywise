a = 'AGGTAB'
b = 'GXTXAYB'
t = [[0 for i in range(len(b)+1)]for j in range(len(a)+1)]

for i in range(len(a)+1):
    for j in range(len(b)+1):
        if i == 0 or j == 0:
            t[i][j] = 0
            continue
        if a[i-1] == b[j-1]:
            t[i][j] = 1+t[i-1][j-1]
        else:
            t[i][j] = max(t[i-1][j],t[i][j-1])
for i in range(len(a)+1):
    for j in range(len(b)+1):
        print(t[i][j],end=' ')
    print()
print(len(a)+len(b)-t[len(a)][len(b)])

'''
OUTPUT: 
a = 'AGGTAB'
b = 'GXTXAYB'
So, 
Shortest Common SuperSequence = 'AGGXTXAYB'
Indirectly we are finding longest common subsequence and subtracting that length once 
We got longest common subsequence  = 4 
Therefore, Len(a)+ Len(b)-(LongestCommonSubsequence) 
            6+7-4  = 9 => 'AGGXTXAYB' 
'''