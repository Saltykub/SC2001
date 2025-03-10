def knapsack_unbounded(C, weights, profits, memo=None):
    if memo is None:
        memo = {}
    
    # Base case: If capacity is zero, max profit is zero
    if C == 0:
        return 0
    
    # If already computed, return stored result
    if C in memo:
        return memo[C]
    
    max_profit = 0
    
    # Try including each item if it fits in the remaining capacity
    for i in range(len(weights)):
        if C >= weights[i]:
            max_profit = max(max_profit, profits[i] + knapsack_unbounded(C - weights[i], weights, profits, memo))
    
    # Store result in memoization dictionary
    memo[C] = max_profit
    return max_profit

# Example usage
weights = [4, 6, 8]  # Given weights
profits = [7, 6, 9]  # Given profits
C = 14  # Given capacity

# Compute maximum profit
max_profit = knapsack_unbounded(C, weights, profits)
print("Maximum Profit:", max_profit)
