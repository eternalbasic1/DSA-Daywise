a = "OldSite:GeeksforGeeks.org"
b = "NewSite:GeeksQuiz.com"
len_a = len(a)
len_b = len(b)
result = 0
t = [[-1 for i in range(len_b+1)]for j in range(len_a+1)]
for i in range(len_a+1):
    for j in range(len_b+1):
        if i == 0 or j == 0:
            t[i][j] = 0
        elif a[i-1] == b[j-1]:
            t[i][j] = 1+t[i-1][j-1]
            result = max(result,t[i][j])
            continue
        else:
            t[i][j] = 0
# print(t[len_a][len_b])
# print()

# for i in range(len_a+1):
#     for j in range(len_b+1):
#         print(t[i][j],end= ' ')
#     print()
#
# print()
print(result)
