'''
why in recursion you don't need to worry about negative cases
ex:- if W<0: (it is false assumption to occur in sub cases, but it never happens because)
As you can see in the above picture(keepNotes in Mobile)
when ever a recursion call happen either the "n" value decrease or weight decrease.
So that in next recursion call it will be calculated/if conditions checks  to the decreased values
which in future it touches to the base condition which we have already declared.
The decreased value indirectly helps the condition if wt[n-1] > w and it gets excuted their itself.
So these two scenarios make no negative cases in dp and we don't write any if conditions for negative cases
'''
def knapsack(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] <= W:
        return max(val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1), knapsack(wt, val, W, n - 1))
    if wt[n - 1] > W:
        return knapsack(wt, val, W, n - 1)


wt = [10, 20, 30]
val = [60, 100, 120]
W = 50
n = 3

maximum = knapsack(wt, val, W, n)
print(maximum)
