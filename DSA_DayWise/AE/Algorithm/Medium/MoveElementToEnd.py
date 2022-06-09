'''
#Mycode
# O(n) Time | O(n) Space
def MoveElementToEnd(Array,element):
    dic = {}
    for i in Array:
        if i in dic:
            dic[i] +=1
        else:
            dic[i] = 1
    #dic_keys = list(dic.keys())
    Array.clear()
    for i in dic.keys():
        if i != element:
            for j in range(dic[i]):
                Array.append(i)
    for i in range(dic[element]):
        Array.append(element)
    return Array

    '''


# O(n) Time | O(1) Space
def MoveElementToEnd(Array,element):
    i = 0
    j = len(Array)-1
    while (i<=j):
        if Array[i] == element and Array[j] != element:
            Array[i],Array[j] = Array[j],Array[i]
            i+=1
            j-=1
            continue
        if Array[i] != element:
            i+=1
        if Array[j] == element:
            j-=1
    return Array

if __name__ == "__main__":
    arr = [1,2,3,1,3,4,4,3,2,2,4,2,2,2,2]
    element = 2
    result = MoveElementToEnd(arr,element)
    print(result)
