arr = [1,1,1,1,1] #leetcode example  & Output was 5 working perfectly
Target_sum = 3
'''
This problem is same as count of subset sum with Given differnce 
So in this problem arr = [1,1,2,3] 
we have to keep '+' or '-' sign before every number of this arr to acheive that sum
for example: +1+1+2-3 == 1 (ie., S1 = (1,1,2) S2 = (3) & S1-S2 == 1 same as 08 problem
 '''

'''
Use the same logic as in 08
S1 = diff + sum(arr) //2
'''
sum_arr = sum(arr)
sum_value = (sum_arr + Target_sum)
if sum_value %2!= 0 :
    print("Not possible")
    exit()
else:
    n = len(arr)
    sum_value = sum_value // 2
    t = [[None for i in range(sum_value+1)]for j in range(n+1)]
    for i in range(n+1):
        t[i][0] = 1
    for j in range(1,sum_value+1):
        t[0][j] = 0
    for i in range(1,n+1):
        for j in range(1,sum_value+1):
            if arr[i-1]<=j:
                t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    print(t[n][sum_value])
    for i in range(n+1):
        for j in range(sum_value+1):
            print(t[i][j],end= " ")
        print()