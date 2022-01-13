# User function Template for python3

class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W, Items, n):
        main_list = []
        for i in range(n):
            main_list.append([Items[i].value,Items[i].weight,(Items[i].value/Items[i].weight)])
        main_list.sort(key = lambda x:x[2],reverse=True)
        #print(main_list)
        count = 0
        checking_weight = W
        for i in range(n):
            if checking_weight-main_list[i][1] >0:
                count = count+main_list[i][0]
                checking_weight = checking_weight- main_list[i][1]
            else:
                count = count+ (checking_weight/main_list[i][1])*main_list[i][0]
                break
        return count

# code here

# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys


# Contributed by : Nagendra Jha

class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, W = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        Items = [Item(0, 0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2 * i]
            Items[i].weight = info[2 * i + 1]

        ob = Solution()
        print("%.2f" % ob.fractionalknapsack(W, Items, n))

# } Driver Code Ends

# 1
# 3 50
# 60 10 100 20 120 30