#O(n2) time | O(n) space

def ThreeSum(array,targetSum):
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        j = i+1
        k = len(array)-1
        while(j<k):
            check = array[i] + array[j] +array[k]
            if check == targetSum:
                triplets.append([array[i],array[j],array[k]])
                j+=1
                k-=1
            elif check <targetSum:
                j+=1
            else:
                k-=1
    return triplets

if __name__ == "__main__":
    arr = [12,3,1,2,-6,5,-8,6]
    target = 0
    print(ThreeSum(arr,target))