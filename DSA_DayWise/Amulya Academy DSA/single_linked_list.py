# User function Template for python3

class Solution:
    ##Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, a, size):
        ##Your code here
        output = sum(a)
        print()
        print(output)
        print()
        # print(output)
        output_final = 0
        check = output
        for i in range(size - 1, 0, -1):
            check -= a[i]
            print('check')
            print(check)
            print()
            if check > output and check >output_final:
                output_final = check
                print('output_final')
                print(output_final)
                print()
        if output_final > output:
            # print(output_final)

            return output_final
        else:
            # print(output)
            return output


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends