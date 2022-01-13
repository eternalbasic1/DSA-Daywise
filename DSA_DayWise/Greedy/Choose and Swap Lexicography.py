# User function Template for python3


class Solution:
    def chooseandswap(self, A):
        choose = ''
        swap = ''
        list1 = list(A)
        #print(list1)
        mainlist = list(set(list1))
        #print(mainlist)
        mainlist.sort()
        #print(mainlist)
        mainlist.remove(list1[0])
        #print(mainlist)
        if len(mainlist) == 0:
            return A
        for i in range(len(list1)):
            if A[i]>mainlist[0]:
                choose = A[i]
                swap = mainlist[0]
                break
            if A[i] == mainlist[0]:
                mainlist = mainlist[1:]
            if len(mainlist) == 0:
                return A
        for i in range(len(list1)):
            if A[i] == choose:
                list1[i] = swap
            if A[i] == swap:
                list1[i] = choose
        str1 = ''.join(list1)
        return str1



# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        A = input()
        ans = ob.chooseandswap(A)
        print(ans)

# } Driver Code Ends


'''
1st Trail
'''
# # code here
#         print(type(A))
#         count = 1
#         for i in range(len(A) - 1):
#             if A[i] <= A[i + 1]:
#                 count += 1
#         if count == len(A):
#             return A
#         else:
#             mini = 'z'
#             position = 0
#             for i in range(len(A)):
#                 if A[i] < mini:
#                     mini = A[i]
#                     position = i
#             for i in range(len(A)):
#                 if A[i] != mini:
#                     swap = A[i]
#                     A[i] = mini
#                     break
#             for i in range(1, len(A)):
#                 if A[i] == swap:
#                     A[i] = mini
#                 if A[i] == mini:
#                     A[i] = swap
#             return A

'''
2nd Trail
'''

# length = len(A)
#         choose = ''
#         swap = 'z'
#         position = 0
#         count = 1
#         main_list = list(A)
#         choose = 'z'
#         for i in range(length-1):
#             if A[i]<=A[i+1]:
#                 count +=1
#                 continue
#             else:
#                 position = i
#                 break
#         # if (position == length-2 and length%2==0) or (count == length):
#         #     return A
#         for i in range(length):
#             if A[i]<=choose:
#                 choose = A[i]
#                 break
#         for i in range(position,length):
#             if A[i]<swap:
#                 swap = A[i]
#         for i in range(length):
#             if A[i] == swap:
#                 main_list[i] = choose
#             if A[i] == choose:
#                 main_list[i] = swap
#         str1 = ''.join(main_list)
#         return str1

# list1 = ['z','f','g','a','v','z']
# updated_List = list(set(list1))
# updated_List.sort()
# print(updated_List)