#O(n2) time | O(1) space
'''

def TwoSumArray(array, targetSum):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)-1):
            if array[i] + array[j] == targetSum:
                print(array[i] , array[j])
                return True
    return False
'''

#O(n) time | O(n) Space

'''
def TwoSumArray(array, targetSum):
    dic = {}
    for i in array:
        check = targetSum - i
        try:
            if dic[check]:
                return True
        except KeyError:
            dic[i] = True
    return False
'''

# O(nlogn) time | O(1) space
def TwoSumArray(array, targetSum):
    array.sort()
    i = 0
    j = len(array)-1
    while i<j:
        check = array[i] + array[j]
        if check == targetSum:
            print(array[i] , array[j])
            return True
        elif check < targetSum:
            i+=1
        else:
            j-=1
    return False

if __name__ == "__main__":
    arr =  [3,5,-4,8,11,1,-1,6]
    target = 10
    print(TwoSumArray(arr,target))