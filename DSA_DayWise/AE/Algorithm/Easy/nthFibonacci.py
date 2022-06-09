'''
# O(2^n) time | o(n) space
def getfibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getfibonacci(n-1)+getfibonacci(n-2)
'''


'''
# O(n) time | o(n) space
def getfibonacci(n , memoize = {1:0,2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getfibonacci(n-1,memoize) + getfibonacci(n-2,memoize)
        return memoize[n]
'''

#O(n) time | O(1) space
#fineeestt method
def getfibonacci(n):
    lastTwo = [0,1]
    counter = 3
    while counter <=n:
        nextFib = lastTwo[0] +lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter+=1
    return lastTwo[1] if n>1 else lastTwo[0]


'''
#my method
def getfibonacci(n,first,second):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(n-2):
            sum = first + second
            first = second
            second = sum
        return sum
'''


if __name__ == "__main__":
    n = 25
    result = getfibonacci(n)
    print(result)