arr = [1, 6, 11, 5]
n =  len(arr)
max_value = sum(arr)
t = [[None for i in range(max_value+1)]for j in range(n+1)]
for i in range(n+1):
    t[i][0] = True
for j in range(1,max_value+1):
    t[0][j] = False
for i in range(1,n+1):
    for j in range(1,max_value+1):
        if arr[i-1]<= j:
            t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
        else:
            t[i][j] = t[i-1][j]
arr_final = []
'''
Travewersing the last row and 
fetching all the "TRUE" values into  arr_final 
'''
for i in range(0,max_value+1):
    a = t[n][i]
    #print(a)
    #print()
    if a == True:
        #print("YES")
        arr_final.append(i)
    else:
        continue

'''
mini = range - 2(S1) {here range is nothing but the maximum sum}
and depending upon the number of values we take even loop or the odd loop
'''
mini = 10e7
length = len(arr_final)
if length%2 == 0:
    length = length //2
else:
    length = (length//2)+1

'''
We were actually traversing only upto 
the half part of the array because we only need 
s1 to check the condition {range - 2*S1}
and if we finding the minimum value 
we'll be replacing them into the mini
'''
for i in range(length):
    a = max_value - 2*(arr_final[i])
    if a<mini:
        mini = a
    else:
        continue
# for i in range(n+1):
#     for j in range(max_value+1):
#         print(t[i][j],end=' ')
#     print()
#print(arr_final)
#print(len(arr_final))
print(mini)