coin = [1,2,3]
sum = 5
# coin = [25,10,5]
# sum = 30
# coin = [9,6,5,1]
# sum = 11
INT_MAX = 10e9
t = [[0 for j in range(sum+1)]for i in range(len(coin)+1)]
for j in range(1,sum+1):
    t[0][j] = INT_MAX-1
for j in range(1,sum+1):
    if j%coin[0] == 0:
        t[1][j] = j//coin[0]
    else:
        t[1][j] = INT_MAX-1
for i in range(2,len(coin)+1):
    for j in range(1,sum+1):
        if coin[i-1]<=j:
            t[i][j] = min((1+t[i][j-coin[i-1]]),(t[i-1][j]))
        else:
            t[i][j] = t[i-1][j]
for i in range(len(coin)+1):
    for j in range(sum+1):
        print(t[i][j],end=' ')
    print()
print(t[len(coin)][sum])
