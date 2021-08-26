def min_coin_count(value, coin_list):
    # 누적 동전 개수
    count = 0

    # coin_list 정렬: sorted(coin_list, reverse=True)
    for coin in coin_list:
        count += value // coin
        value = value % coin
    return count

default_coin_list = [500, 100, 50, 10]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))