arr = [1,1,2,3]
diff = 1
sum_value = (diff + sum(arr))

'''
LOGIC 
S1 - S2 = difference
S1 + S2 = sum(arr)
adding both the eq
we get S1 = (differnce + sum(arr))//2 # if it is even or else no subsets available
'''

if sum_value %2 != 0:
    '''
     if sum(arr)+diff is odd, then the sum of subset s1 will be odd/2. 
     say if sum(arr)+diff is 9 , then sum of s1 should be 4.5.
    You can not get a sum of 4.5 (float) in an array of integers.
    If you pass it to function,
    it will truncate 4.5 to 4 and there may be 
    a subset whose sum might be equal to 4 and hence a wrong answer.
    '''
    print("No subset available")
    exit()
else:
    sum_value = sum_value //2
    n = len(arr)
    t = [[None for i in range(sum_value+1)]for j in range(n+1)]
    for i in range(n+1):
        t[i][0] = 1
    for i in range(1,sum_value+1):
        t[0][i] = 0
    for i in range(1,n+1):
        for j in range(1,sum_value+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    print("The number of subsets are" , t[n][sum_value])
for i in range(n+1):
    for j in range(sum_value+1):
        print(t[i][j] , end = ' ')
    print()
