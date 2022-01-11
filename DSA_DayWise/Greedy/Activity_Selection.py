n=47
start = [86,32,31,98,37,65,98,71,99,58,59,32,52,69,15,75,4,86,57,36,83,18,58,50,43,29,98,53,80,5,89,73,8,97,17,100,9,21,55,55,32,74,60,32,87,72,54]
end =[126,112,134,138,89,118,107,124,126,83,133,64,124,109,108,132,111,95,82,106,86,118,82,78,92,55,128,121,118,95,94,110,111,146,124,148,95,146,109,61,93,126,74,76,110,78,91]
count = 0
combine = []
for i in range(n):
        combine.append([start[i],end[i]])
combine.sort(key=lambda x: x[1])
final = [combine[0]]
count = 1
end = combine[0][1]
for i in range(1,n):
    if combine[i][0]>end:
        final.append(combine[i])
        count+=1
        end = combine[i][1]
print(combine)
print(final)
print(count)







'''
This method also working 
{in for loop if prev<jobs[i][0] makes this work} 
originally i have kept <= so check  that once
def maximumMeetings(self,n,start,end):
        """
        Function to find the maximum number of meetings that can be performed in a meeting room.
        Here strategy is to sort the jobs according to end time.
        """
        jobs = [(start[i], end[i]) for i in range(n)]
        jobs.sort(key=lambda x: x[1])
        count, prev = 0, 0
        
        for i in range(n):
            if prev < jobs[i][0]:
                count += 1
                prev = jobs[i][1]
                
        return count
'''










#todo: Previoud way
# n=8
# start = [75250,50074,43659,8931,11273,27545,50879,77924]
# end =[112960,114515,81825,93424,54316,35533,73383,160252]
# count = 0
# combine = []
# for i in range(n):
#         combine.append([start[i],end[i]])
# combine.sort(key=lambda x: x[1])
# prev = combine[0]
# todo = True
# for i in range(n-1):
#     if (combine[i][0]<combine[i+1][0] and combine[i][1]<=combine[i+1][0]) or (prev[1]<=combine[i][0]):
#         if (combine[0][0] < combine[1][0] and combine[0][1] <= combine[1][0]):
#             todo = False
#
#         prev = combine[i]
#         count +=1


# for i in range(n-1):
#     if (combine[i][1] <= combine[i+1][0]) or (combine[i][1]<=prev[1]):
#         prev = combine[i]
#         print(combine[i])
#
#         count+=1
# print(combine)
# print(todo)
# if todo:
#     print(count+1)
# else:
#     print(count)