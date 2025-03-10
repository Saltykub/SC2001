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

# Example usage
weights = [4, 6, 8]  # Given weights
profits = [7, 6, 9]  # Given profits
C = 14  # Given capacity

# Compute maximum profit
max_profit = knapsack_unbounded(C, weights, profits)
print("Maximum Profit:", max_profit)

weights_btm_up1 = [4, 6, 8]
weights_btm_up2 = [5, 6, 8]
profits_btm_up = [7, 6, 9]
capacity_btm_up = 14

def dp_btm_up(Cpt, Pft, Wgt):
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



result_table1 = dp_btm_up(capacity_btm_up, profits_btm_up, weights_btm_up1)
result_table2 = dp_btm_up(capacity_btm_up, profits_btm_up, weights_btm_up2)
print("Bottom Up Approach (Table 1):", result_table1)
print("Bottom Up Approach (Table 2):", result_table2)