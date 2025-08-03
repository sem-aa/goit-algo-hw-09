from typing import Dict
import time

# Номінали монет
COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount: int) -> Dict[int, int]:
    """
    Жадібний алгоритм видачі решти
    """
    result = {}
    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
        if amount == 0:
            break
    return result

def find_min_coins(amount: int) -> Dict[int, int]:
    """
    Алгоритм динамічного програмування видачі решти
    """
    # Мінімальна кількість монет для кожної суми
    min_coins = [float('inf')] * (amount + 1)
    # Запам’ятовуємо останню монету для відновлення рішення
    last_coin = [-1] * (amount + 1)

    min_coins[0] = 0

    for coin in COINS:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                last_coin[x] = coin

    result = {}
    curr = amount
    while curr > 0:
        coin = last_coin[curr]
        if coin == -1:
            break  # Неможливо розбити суму
        result[coin] = result.get(coin, 0) + 1
        curr -= coin

    return result

if __name__ == "__main__":
    test_amount = 113

    print("--- Greedy Algorithm ---")
    start = time.time()
    greedy_result = find_coins_greedy(test_amount)
    end = time.time()
    print("Result:", greedy_result)
    print("Time:", end - start)

    print("\n--- Dynamic Programming Algorithm ---")
    start = time.time()
    dp_result = find_min_coins(test_amount)
    end = time.time()
    print("Result:", dp_result)
    print("Time:", end - start)

    # Складність жадібного алгоритму: O(n), де n — кількість номіналів
    # Складність динамічного програмування: O(n * amount), де amount — сума