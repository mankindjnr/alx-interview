#!/usr/bin/python3
"""change comes from within"""


def makeChange(coins, total):
    """the dynamic solution"""
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Iterate through all possible values from 1 to total
    for value in range(1, total + 1):
        for coin in coins:
            if coin <= value:
                # Calculate the minimum number of coins
                # needed for the current value
                min_coins[value] = min(
                    min_coins[value], min_coins[value - coin] + 1)

    # If the final value's minimum coins is still infinity
    # it means it's not possible to make the total
    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]
