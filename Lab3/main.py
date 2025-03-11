weights1 = [4, 6, 8]
weights2 = [5, 6, 8]
profits = [7, 6, 9]
capacity = 14

def knapsack_unbounded(C, weights, profits, max_profits=None):
    if max_profits is None:
        max_profits = {}
    
    # if Capacity is 0, unable to fit any items inside
    if C == 0:
        return 0
    
    if C in max_profits:
        return max_profits[C]
    
    max_profit = 0

    # try fitting each item inside
    for i in range(len(weights)):
        if C >= weights[i]:
            # compare if max_profit with fitting extra item is greater than if item is fit in
            max_profit = max(max_profit, profits[i] + knapsack_unbounded(C - weights[i], weights, profits, max_profits))
    
    max_profits[C] = max_profit
    return max_profit


# Compute maximum profit
max_profit = knapsack_unbounded(capacity, weights1, profits)
print("Maximum Profit:", max_profit)


def knapsack_btm_up(Cpt, Pft, Wgt):
    #initialize table size capacity +1
    dp = [0] * (Cpt+ 1)
    
    #store number types of items in n
    n = len(Wgt)

    # loop from 1 to capacity
    for i in range(1, Cpt+1):
        # loop every item type in n
        for item in range(n):
            #check if item can fit in knapsack
            if Wgt[item] <= i:
                #max takes highest value 
                # current best profit VS profit of current item + best profit for remaining 
                # best profit for remaining has been calculated prior when running through loop
                dp[i] = max(dp[i], Pft[item] + dp[i - Wgt[item]])
    return dp[Cpt]



result_table1 = knapsack_btm_up(capacity, profits, weights1)
result_table2 = knapsack_btm_up(capacity, profits, weights2)
print("Bottom Up Approach (Table 1):", result_table1)
print("Bottom Up Approach (Table 2):", result_table2)

#2D matrix, easier to track but take more space? capacity * len(profits)
def knapsack_2D(Cpt, Pft, Wgt):
    
    # matrix capacity and profit
    dp = [[0 for _ in range(Cpt + 1)] for _ in range(len(Pft) + 1)]

    # calculate maximum profit for each 
    # item index and knapsack weight.
    for i in range(len(Pft) - 1, -1, -1):
        for j in range(1, Cpt + 1):

            take = 0
            #if capacity - weight of current item > 0 we take
            if j - Wgt[i] >= 0:
                take = Pft[i] + dp[i][j - Wgt[i]]
            #compare with next item
            noTake = dp[i + 1][j]

            dp[i][j] = max(take, noTake)
    #max profit is in dp[0][capacity]
    return dp[0][Cpt]

print(knapsack_2D(capacity, profits, weights1))  
print(knapsack_2D(capacity, profits, weights2))  