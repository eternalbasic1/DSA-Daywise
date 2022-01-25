a = 'heap'
b = 'pea'
# a = 'qwerty'
# b = 'asdfgh'
len_a = len(a)
len_b = len(b)

t = [[0 for j in range(len_b+1)]for i in range(len_a+1)]

for i in range(len_a+1):
    for j in range(len_b+1):
        if i == 0 or j == 0:
            t[i][j] = 0
            continue
        if a[i-1]==b[j-1]:
            t[i][j] = 1+t[i-1][j-1]
        else:
            t[i][j] = max(t[i-1][j],t[i][j-1])

Insertion = 0
Deletion = 0
Insertion = len_b - t[len_a][len_b]
Deletion = len_a - t[len_a][len_b]

print("Insertion: ",Insertion)
print("Deletion: ", Deletion)