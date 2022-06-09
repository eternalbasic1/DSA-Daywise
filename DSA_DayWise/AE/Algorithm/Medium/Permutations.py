#MyCode
#O(n^2) time| O(n) Space

'''
def Permutations(Array):
    Length = len(Array)
    check = []
    for i in range(Length):
        Arr = []
        for z in Array:
            Arr.append(z)
        print(Arr)
        Firstvalue = Arr.pop(i)
        for j in range(len(Arr)):
            if j == 0:
                continue
            check.append(Firstvalue)
            check = check+ Arr[j:len(Arr)+1] + Arr[0:j]
            #check.insert(0,Firstvalue)
            print(check)
            check = []
    return
if __name__ == "__main__":
    arr = [1,2,3]
    Permutations(arr)
'''



# Upper Bound: O(n^2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
# def getPermutations(array):
#     permutations = []
#     permutationsHelper(array, [], permutations)
#     return permutations
#
#
# def permutationsHelper(array, currentPermutation, permutations):
#     if not len(array) and len(currentPermutation):
#         permutations.append(currentPermutation)
#     else:
#         for i in range(len(array)):
#             newArray = array[:i] + array[i + 1:]
#             newPermutation = currentPermutation + [array[i]]
#             permutationsHelper(newArray, newPermutation, permutations)



# O(n*n!) time | O(n*n!) space
def getPermutations(array):
    permutations = []
    permutationsHelper(0, array, permutations)
    return permutations


def permutationsHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationsHelper(i + 1, array, permutations)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

if __name__ == "__main__":
    Permutations = getPermutations([1,2,3,4])
    print(Permutations)
