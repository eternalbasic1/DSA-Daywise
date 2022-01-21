arr = [2,3,5,6,8,10]
sum_value = 10
n = len(arr)
t = [[0 for i in range(sum_value+1)]for j in range(n+1)]
for i in range(n+1):
    t[i][0] = 1
for j in range(1,sum_value+1):
    t[0][j] = 0
'''
from the next for loop JUST REMEMBER that,
we have to traverse from range(1,n+1) & range(1,sum_value+1)
BUT NOT directly range(n+1) & range(sum_value+1)
'''
for i in range(1,n+1):
    for j in range(1,sum_value+1):
        if arr[i-1]<= j:
            t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
        else:
            t[i][j] = t[i-1][j]
print(t[n][sum_value])
for i in range(n+1):
    for j in range(sum_value+1):
        print(t[i][j] , end = ' ')
    print()
