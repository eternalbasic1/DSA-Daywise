a = 'agbcba'
b = a[::-1]
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
print('Longest Palindromic Subsequence', t[len(a)][len(b)])

'''
OUTPUT:
 a = 'agbcba'
 b = 'abcbga' 
 palindromic_subsequence = 'abcba'
 
'''
for i in range(len(a)+1):
    for j in range(len(b)+1):
        print(t[i][j],end=' ')
    print()
print()

final_string = ' '
i = len(a)
j = len(b)

while(i!=0 and j!=0):
    if a[i-1] == b[j-1]:
        final_string = final_string+a[i-1]
        i = i-1
        j = j-1
    else:
        if t[i-1][j] >t[i][j-1]:
            i= i-1
            j = j
        else:
            i = i
            j = j-1
final_string = final_string[::-1]
print(final_string)