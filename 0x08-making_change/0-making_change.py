#!/usr/bin/python3
def makeChange(coins, total):
    # Initialize a list to store the minimum number of coins for each value from 0 to 'total'
    # Initialize all values with a value larger than 'total' to represent infinity
    min_coins = [float('inf')] * (total + 1)
    
    # The minimum number of coins needed to make change for 0 is 0
    min_coins[0] = 0
    
    # Iterate through each coin value
    for coin in coins:
        # For each value from 'coin' to 'total', update the minimum number of coins needed
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
    
    # If the value at 'total' is still infinity, it means we cannot make change
    if min_coins[total] == float('inf'):
        return -1
    
    # Otherwise, return the minimum number of coins needed to make change for 'total'
    return min_coins[total]

# Example usage:
coins = [1, 2, 5]
total = 11
result = makeChange(coins, total)
print(result)  # Output should be 3 (11 = 5 + 5 + 1)
