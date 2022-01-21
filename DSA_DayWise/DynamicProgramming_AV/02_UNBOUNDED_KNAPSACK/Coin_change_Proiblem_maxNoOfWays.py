coin = [1,2,3]
#coin = [2,5,3,6]
N= len(coin)
sum = 5
#sum = 10
t = [[0 for i in range(sum+1)]for j in range(N+1)]
print(t)
for i in range(N+1):
    t[i][0] = 1
'''
for j in range(1,sum+1):
    t[0][j] = 0
Actually this partiular statement is not needed because it is already declared 
at the time of initializaing the array line no:6
'''

print()
for i in range(1,N+1):
    for j in range(1,sum+1):
        if coin[i-1]<=sum:
            t[i][j] = t[i][j - coin[i - 1]] + t[i - 1][j]
        else:
            t[i][j] = t[i - 1][j]

for i in range(N+1):
    for j in range(sum+1):
        print(t[i][j] ,end=' ')
    print()
print(t[N][sum])