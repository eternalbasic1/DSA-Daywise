
'''
# O(nm) time | O(nm) space
def Levenshtein_Distance(str1,str2):
    len_a = len(str1)
    len_b = len(str2)
    results = 0
    t = [ [-1 for i in range(len_b+1)]for j in range(len_a+1) ]
    for i in range(len_a + 1):
        for j in range(len_b+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                t[i][j] = 1+ t[i-1][j-1]
                results = max(results,t[i][j])
            else:
                t[i][j] = 0
    return results

'''

if __name__ == "__main__":
    str1 = 'abc'
    str2 = 'yabd'
    commonValue = Levenshtein_Distance(str1,str2)
    if len(str1) == commonValue and commonValue == len(str2):
        print("No Insertions and deletions required")
    elif len(str1) == commonValue:
        print(f"Number of Insertion : {len(str2) - len(str1)}")
    else:
        print(f"Number of Deletions : {len(str1) - commonValue}")
        print(f"Number of Insertions : {len(str2) - commonValue}")
