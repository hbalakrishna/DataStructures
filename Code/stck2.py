a = [7, 1, 5, 3, 6, 4]
# [7, 6, 4, 3, 1]


# get_min = min(a)
# idx = a.index(get_min)
# if idx == len(a):
#     print(0)
# else:
#     print(max(a[idx:]) - get_min)
min_profit = float('inf')
max_profit = 0

for x in a:
    min_profit = min(min_profit, x)
    profit = x - min_profit
    max_profit = max(max_profit, profit)
print(max_profit)
