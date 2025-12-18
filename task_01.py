import timeit

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount, coins=COINS):
    """Returns the optimal set of coins for a given amount using a greedy algorithm"""
    result = {}
    rest = amount

    for coin in coins:
        if rest >= coin:
            count = rest // coin
            result[coin] = count
            rest -= coin * count
    return result


def find_min_coins(amount, coins=COINS):
    """Returns the minimum number of coins needed to form a given amount using dynamic programming."""
    result = {}
    VERY_LARGE_NUMBER = float("inf")

    min_coins = [0] + [VERY_LARGE_NUMBER] * amount
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_coin[i] = coin

    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


def compare_algorithms(amounts, runs=1000):
    """Compare greedy and dynamic programming algorithms for list of amounts."""
    print("\n--- Benchmark (avg seconds per call) ---")
    for amount in amounts:
        greedy_algorithm = (
            timeit.timeit(lambda: find_coins_greedy(amount), number=runs) / runs
        )
        dynamic_programming_algorithm = (
            timeit.timeit(lambda: find_min_coins(amount), number=runs) / runs
        )

        print(
            f"Amount: {amount:7d} | "
            f"Greedy Algorithm: {greedy_algorithm:.8f}s | "
            f"Dynamic Programming Algorithm: {dynamic_programming_algorithm:.8f}s"
        )


if __name__ == "__main__":
    # Test algorithms
    amount = 113
    print("Greedy algorithm:", find_coins_greedy(amount))
    print("Dynamic programming algorithm:    ", find_min_coins(amount))

    amounts_to_test = [10, 234, 1567, 5987, 12345, 20000]
    compare_algorithms(amounts_to_test, runs=2000)
