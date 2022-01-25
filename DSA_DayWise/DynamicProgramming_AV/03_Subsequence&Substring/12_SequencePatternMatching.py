'''
Actually for this problem there is no need of DP we can actually solve using linear search
but knowing in multiple ways helps
'''

#1st Way LINEAR APPOARCH:
a = 'AXY'
b = 'ADXCPY'

len_a = len(a)
len_b = len(b)
i = 0
j = 0

while(True):
    if (i == len_a-1) or (j == len_b-1):
        break
    if a[i] == b[j]:
        i+=1
        j+=1
    else:
        j+=1
if i == len_a-1:
    print("Yes Pattern Matching")
else:
    print('No Pattern Not Matching')

#2nd Way DP METHOD

a = 'AXY'
b = 'ADXCPY'

t = [[0 for i in range(len(b)+1)]for j in range(len(a)+1)]
for i in range(len(a)+1):
    for j in range(len(b)+1):
        if i==0 or j==0:
            t[i][j] =0
            continue
        if a[i-1] == b[j-1]:
            t[i][j] = 1+t[i-1][j-1]
        else:
            t[i][j] = max(t[i-1][j],t[i][j-1])
if len(a) == t[len(a)][len(b)]:
    print("Yes Pattern Matching")
else:
    print("PAttern Not Matching")
'''
basically when pattern match then it should be size of checking string ie., string a
a = 'AXY'
b = 'ADXCPY'
so OUTPUT gonna be 'AXY' length = 3 

'''
