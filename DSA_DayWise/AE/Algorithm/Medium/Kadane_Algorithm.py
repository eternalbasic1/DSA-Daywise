
'''
# time O(n) | Space O(1)
# MY SOLUTION
def Kadanes(arr):
    maxSoFar = -10e9
    maxEndingHere = -10e9
    for i in arr:
        maxEndingHere = max(maxEndingHere+i , i)
        maxSoFar = max(maxSoFar,maxEndingHere)
    return maxSoFar
'''


# time O(n) | Space O(1)
def Kadanes(arr):
    maxSoFar = arr[0]
    maxEndingHere = arr[0]
    for i in arr[1:]:
        maxEndingHere = max(maxEndingHere+i , i)
        maxSoFar = max(maxSoFar,maxEndingHere)
    return maxSoFar


if __name__ == "__main__":
    arr = [3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]
    results = Kadanes(arr)
    print(results)

