def MaxSumNoAdjacent(arr):
    a = arr[0]
    if (arr[0] > arr[1]):
        b = arr[0]
    else:
         b = arr[1]
    dummy = [a,b]
    for i in range(2,len(arr)):
        #print((dummy[i-2]+arr[i]),arr[i])
        check = max((dummy[i-2]+arr[i]),dummy[i-1])
        dummy.append(check)
    print(arr)
    print(dummy)
    return dummy[-1]

if __name__ == "__main__":
    arr = [2,1,4,9]
    result = MaxSumNoAdjacent(arr)
    print(result)