arr = [22,44,66]
sum = 132
n = 3
t = [[None for i in range(sum+1)]for j in range(n+1)]

# If sum is 0, then answer is true
for i in range(n + 1):
    t[i][0] = True

# If sum is not 0 and set is empty,
# then answer is false
for i in range(1, sum + 1):
    t[0][i] = False
'''
from the next for loop JUST REMEMBER that,
we have to traverse from range(1,n+1) & range(1,sum+1)
BUT NOT directly range(n+1) & range(sum+1)
'''
for i in range(1,n+1):
    for j in range(1,sum+1):
        if arr[i-1]<=j:
            t[i][j] = (t[i-1][j-arr[i-1]]) or (t[i-1][j])
            '''
            In use t[i-1][j-arr[i-1]] instead of t[i][j-arr[i-1]] in the line t[i][j] = (t[i-1][j-arr[i-1]]) or (t[i-1][j])
            '''
        else:
            t[i][j] = t[i-1][j]
print(t[n][sum])

for i in range(n+1):
    for j in range(sum+1):
        print(t[i][j] ,end = ' ')
    print()
print(t[n][sum])



'''
intial approah but its not working 
we have to declare i == 0 and j == 0 
outside the for loop with a new for loop as above statement
'''

# for i in range(n+1):
#     for j in range(sum+1):
#         # if i == 0 and j == 0:
#         #     t[i][j] = True
#         #     continue
#         if i == 0:
#             t[i][j] = False
#             continue
#         if j == 0:
#             t[i][j] = True
#             continue
#         if arr[i-1]<=j:
#             t[i][j] = t[i][j-arr[i-1]] or t[i-1][j]
#         else:
#             t[i][j] = t[i-1][j]

