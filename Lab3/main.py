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
