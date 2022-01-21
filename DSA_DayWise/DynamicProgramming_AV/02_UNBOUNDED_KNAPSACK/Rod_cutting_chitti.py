t=[]
length=[1,2,3,4,5,6,7,8]
price=[1,5,8,9,10,17,17,20]
arr_size= len(length)  #array length
n=8  #total length of rod
for i in range(arr_size+1):
    c=[]
    for j in range(n+1):
        c.append(0)
    t.append(c)
for i in range(arr_size+1):
    for j in range(n+1):
        if i == 0 or j == 0:
            t[i][j] = 0
        elif(length[i-1]<=j):
            t[i][j]=max(price[i-1]+t[i][j-length[i-1]],t[i-1][j])
        else:
            t[i][j]=t[i-1][j]
print(t[arr_size][n])


for i in range(arr_size+1):
    for j in range(n+1):
        print(t[i][j],end= ' ')
    print()
