def knapsack(wt, val, W, n):
    if n == 0 or W == 0:
        t[n][W] = 0
        return t[n][W]
    if t[n][W] != -1:
        return t[n][W]
    if wt[n - 1] <= W:
        t[n][W] = max(val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1), knapsack(wt, val, W, n - 1))
        return t[n][W]
    if wt[n - 1] > W:
        t[n][W] = knapsack(wt, val, W, n - 1)
        return t[n][W]  


n = 3
W = 50
wt = [10, 20, 30]
val = [60, 100, 120]
t = [[-1] * (W + 1)] * (n + 1)
maximum = knapsack(wt, val, W, n)
print(maximum)
