class Solution:
    def JobScheduling(self, Jobs, n):
        checking  = []
        main_list = []
        for i in range(n):
            main_list.append([Jobs[i].id, Jobs[i].deadline, Jobs[i].profit])
        MAXI = -10e7
        for i in range(n):
            if main_list[i][1]>MAXI:
                MAXI = main_list[i][1]
        print(MAXI)
        #print(main_list)
        main_list.sort(key=lambda x:x[2],reverse=True)
        print(main_list)
        for i in range(MAXI):
            checking.append(-1)
        print(checking)
        for i in range(n):
            index_value = main_list[i][1]
            profit = main_list[i][2]
            if checking[index_value-1]==-1:
                checking[index_value-1] = profit
            else:
                while(True):
                    index_value = index_value-1
                    if index_value<=0:
                        break
                    if checking[index_value-1]==-1:
                        checking[index_value-1] = profit
                        break
        count = 0
        count_value = 0
        for i in range(MAXI):
            if checking[i]!=-1:
                count+=1
                count_value = count_value+checking[i]
        return [count,count_value]
        #print(checking)
        # print(type(Jobs))
        # for i in range(n):
        #     print(Jobs[i].id, Jobs[i].deadline, Jobs[i].profit)
        # dic = {}
        # for i in range(n):
        #     dic[Jobs[i].deadline] = []
        # print(type(dic[Jobs[i].deadline]))
        # for i in range(n):
        #     a = dic[Jobs[i].deadline]
        #     a.append(Jobs[i].profit)
        #     dic[Jobs[i].deadline] = a
        # print(dic)
        # mini = 10e7
        # maxi = -10e7
        # full_list = []
        # multilist = []
        # for i in range(n):
        #     if Jobs[i].deadline < mini:
        #         mini = Jobs[i].id
        #     if Jobs[i].deadline > maxi:
        #         maxi = Jobs[i].deadline
        #     if Jobs[i].deadline not in full_list:
        #         full_list.append(Jobs[i].deadline)
        #     if Jobs[i].deadline in dic.keys() and len(dic[Jobs[i].deadline])>1:
        #         multilist.append(Jobs[i].deadline)
        # # print(mini)
        # # print(maxi)
        # # print(full_list)
        # # print(list(set(multilist)))
        # count = 0
        # multilist = list(set(multilist))
        # multilist.sort(reverse=True)
        # for i in range(mini,maxi+1):
        #     if i in dic.keys():
        #         if i in multilist:
        #             count =
        #return [2, 60]

        # code here


# {
#  Driver Code Starts
# Initial Template for Python 3
# import atexit
# import io
# import sys


# Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        info = list(map(int, input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3 * i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit = info[3 * i + 2]
        ob = Solution()
        res = ob.JobScheduling(Jobs, n)
        print(res[0], end=" ")
        print(res[1])
# } Driver Code Ends

# 1
# 4
# 1 4 20 2 1 10 3 1 40 4 1 30
# 5
# 1 2 100 2 1 19 3 2 27 4 1 25 5 1 15
# 1 56 288 2 27 435 3 67 401 4 64 368 5 94 248 6 54 361 7 43 108 8 96 167 9 73 251 10 96 170 11 14 156 12 78 184 13 61 370 14 77 424 15 68 397 16 40 375 17 36 218

