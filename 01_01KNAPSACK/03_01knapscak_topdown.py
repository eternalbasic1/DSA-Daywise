n = 3
W = 50
wt = [10,20,30]
val = [60,100,120]

'''
don't declare in this way declare it's replacing all similar column & row though we declare a single cell
t = [[0]*(W+1)]*(n+1)
https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly
'''

t = [[0 for i in range(W+1)]for j in range (n + 1)]

for i in range(n+1):
    for j in range(W+1):
        if i == 0 or j==0:
            t[i][j] = 0
            continue

        if wt[i-1] <= j: # here make sure its "j" not W Because j indicates the weight of that particular sub problem
            t[i][j] = max((val[i-1]+(t[i-1][j-wt[i-1]])),(t[i-1][j]))
        else:
            t[i][j] = t[i-1][j]
print(t[n][W])
# print()
# for i in range(n+1):
#     for j in range(W+1):
#         print(t[i][j],end=' ')
#     print()












