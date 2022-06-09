
'''
# Please Don't FOllow These Kind of Approach because in this approach Same reference is happening
# which makes a chios NEVER TRY TO APPEND IF YOU TOOK ANY REFERENCE FROM MAIN ARRAY
#BECAUSE IT IS TRYING TO CHANGE THE MAIN VARIABLE ALSO SO DO SOME KIND OF '+' OPERATION AS GIVEN BELOW.
def PowerSet(Array,AllPowerSet):
    for i in Array:
        IntermediateArray = []
        for j in range(len(AllPowerSet)):
            pointer = AllPowerSet[j]
            pointer.append(i)
            IntermediateArray.append(pointer)
        AllPowerSet.extend(IntermediateArray)
        IntermediateArray = []
    return AllPowerSet

'''



#Iterative Approach
# Time O(n*2^n) |Space O(n*2^n)
def PowerSet(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset+[ele])
    return subsets

'''
#Recursive Approach
# Time O(n*2^n) |Space O(n*2^n)
def PowerSet(array,idx=None):
    if idx == None:
        idx = len(array)-1
    elif idx <0 :
        return [[]]
    ele = array[idx]
    subsets = PowerSet(array,idx-1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset+[ele])
    return subsets
'''

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    AllPowerSet = PowerSet(arr)
    for i in AllPowerSet:
        print(i)