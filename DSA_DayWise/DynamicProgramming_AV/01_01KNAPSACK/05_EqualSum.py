arr = [1,5,5,11]
#arr = [1,1,1,1,2,1,1]
#sum_value = 4
check = sum(arr)
if (check % 2 != 0): # I'm not sure why i get this equation here "if (check%2 != 0) or (check //2 != sum_value):" its actually working good without this equation
    print(False,"We can divide them into two parts")
else:
    n = len(arr)
    value = check // 2
    t = [[None for i in range(value+1)] for j in range(n+1)]
    for i in range(n+1):
        t[i][0] = True
    for j in range(1,value+1):
        t[0][j] = False

    '''
    from the next for loop JUST REMEMBER that,
    we have to traverse from range(1,n+1) & range(1,value+1)
    BUT NOT directly range(n+1) & range(value+1)
    '''

    for i in range(1,n+1):
        for j in range(1,value+1):
            if arr[i-1]<= j:
                t[i][j] = (t[i-1][j-arr[i-1]]) or (t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    print(t[n][value])
    for i in range(n+1):
        for j in range(value+1):
            print(t[i][j],end = ' ')
        print()





