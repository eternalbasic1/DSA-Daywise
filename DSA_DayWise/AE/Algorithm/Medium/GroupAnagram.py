
'''
# My Code
# Time O(W(nlogn)) | Space O(wn)
arr =  ['yo','act','flop','tac','cat','oy','olfp']
arr_sorted = []
for i in range(len(arr)):
    arr_sorted.append((''.join(sorted(arr[i]))))
#print(arr_sorted)
dic = {}
for i in range(len(arr_sorted)):
    if arr_sorted[i] in dic:
        dic[arr_sorted[i]].append(arr[i])
        arr_sorted[i] = "@"
    else:
        dic[arr_sorted[i]] = [arr[i]]
#print(dic)
#print(arr_sorted)
arr.clear()
for i in arr_sorted:
    if i != '@':
        arr.append(dic[i])
    else:
        continue
print(arr)
'''

#Your code was same as Algoexpert.


# O(w * n * log(n)) time | O(wn) space - where w is the number of words and
# n is the length of the longest word
def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())

'''
# O(w * n * log(n) + n * w * log(w)) time | O(wn) space - where w is the number of words and
# n is the length of the longest word

def groupAnagrams(words):
    if len(words) == 0:
        return []

    sortedWords = ["".join(sorted(w)) for w in words]
    print(sortedWords)
    indices = [i for i in range(len(words))]
    print(indices)
    #HighLight Point sorting indices using lambda function 
    indices.sort(key=lambda x: sortedWords[x])
    print(indices)
    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]
    for index in indices:
        word = words[index]
        sortedWord = sortedWords[index]

        if sortedWord == currentAnagram:
            currentAnagramGroup.append(word)
            continue

        result.append(currentAnagramGroup)
        currentAnagramGroup = [word]
        currentAnagram = sortedWord

    result.append(currentAnagramGroup)

    return result
'''


if __name__ == "__main__":
    arr = ['yo','act','flop','tac','cat','oy','olfp']
    print(groupAnagrams(arr))
