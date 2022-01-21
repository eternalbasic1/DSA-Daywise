length = [1, 2, 3, 4, 5, 6, 7, 8]
price = [1, 5, 8, 9, 10, 17, 17, 20]
# length = [1,2,3,4]
# price = [1,5,8,9]
N = 8
max_len = 8
t = [[None for i in range(max_len+1)]for j in range(N+1)]
for i in range(N+1):
    t[i][0] = 0
for j in range(1,max_len+1):
    t[0][j] = 0
for i in range(1,N+1):
    for j in range(1,max_len+1):
        if length[i-1] <= j:
            #In 0/1 knapsack we will be calling "t[i-1][j-length[i-1]]" but here we wiill be calling "t[i][j-length[i-1]]"
            t[i][j] = max((price[i-1]+t[i][j-length[i-1]]), (t[i-1][j]))
        else:
            t[i][j] = t[i-1][j]
print(t[N][max_len])
print()
for i in range(N+1):
    for j in range(max_len +1):
        print(t[i][j] , end= ' ')
    print()
