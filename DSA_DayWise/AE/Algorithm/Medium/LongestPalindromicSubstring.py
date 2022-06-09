def LongestPalindromicSubstring(s):
    s_reverse = s[::-1]
    len_s = len(s)
    result = 0
    t = [[-1 for i in range(len_s+1)]for j in range(len_s+1)]
    print(t)
    for i in range(len_s+1):
        for j in range(len_s+1):
            if i == 0 or j == 0:
                t[i][j] = 0
                continue
            elif s[i-1] == s_reverse[j-1]:
                t[i][j] = 1+t[i-1][j-1]
                result = max(result,t[i][j])
            else:
                t[i][j] = 0
    for i in range(len_s+1):
        for j in range(len_s+1):
            print(t[i][j] , end=" ")
        print()
    return result

if __name__ == "__main__":
    s = "abaxyzzyxxf"
    print(s)
    result = LongestPalindromicSubstring(s)
    print(result)