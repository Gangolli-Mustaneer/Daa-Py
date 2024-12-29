def knapsack(w, wt, val, n):
    if n == 0 or w == 0:
        return 0

    if wt[n-1] > w:
        return knapsack(w, wt, val, n-1)
    else:
        return max(val[n-1] + knapsack(w - wt[n-1], wt, val, n-1), knapsack(w, wt, val, n-1))

prof = [60, 100, 120]
weight = [10, 20, 30]
w = 50

new_profit = knapsack(w, weight, prof, len(prof))
print("Maximum profit:", new_profit)