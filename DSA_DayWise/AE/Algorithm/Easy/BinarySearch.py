# Recursive way
# time:O(log n ) and Space O(log n)
# def BinarySearch(array,target):
#     return BinarySearchHelper(array,target,0,len(array)-1)
#
# def BinarySearchHelper(array,target,left,right):
#     if left>right:
#         return "Target is not available in the array"
#     middle = (left+right) // 2
#     if array[middle] == target:
#         return f"We found the target {target} at position {middle}"
#     if array[middle]<target:
#         return BinarySearchHelper(array,target,middle+1,right)
#     else:
#         return BinarySearchHelper(array,target,left,middle-1)



# Iterative Way
# time:O(log n ) and Space O(1)
def BinarySearch(array,target):
    return BinarySearchHelper(array,target,0,len(array)-1)

def BinarySearchHelper(array,target,left,right):
    while left<=right:
        middle = (left+right) // 2
        if array[middle] == target:
            return f"We found the target {target} at position {middle}"
        if array[middle]<target:
            left = middle+1
        else:
            right = middle-1
    return -1


if __name__ == '__main__':
    array = [1,3,4,34,43,54,65,76,87,99]
    target = 43
    output = BinarySearch(array,target)
    print(output)

