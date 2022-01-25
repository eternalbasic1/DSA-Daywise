a = 'acbcf'
b = 'acbcdaf'
# a = 'AGGTAB'
# b = 'GXTXAYB'
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
i = len(a)
j = len(b)
string = ''
while(i != 0 or j != 0):
    if i == 0 or j == 0:
        break
    if a[i-1] == b [j-1]:
        string = string+a[i-1]
        i-=1
        j-=1
    else:
        if t[i-1][j]>t[i][j-1]:
            string = string+a[i-1]
            i -=1
        else:
            string = string + b[j - 1]
            j-=1
while(i!=0):
    string = string+a[i-1]
    i-=1
while(j!=0):
    string = string + b[j-1]
    j-=1

print(string[::-1])