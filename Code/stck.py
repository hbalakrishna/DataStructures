prices = [1,2,3]

if len(prices)<2:
    print(0)

i = len(prices) - 1
ans = 0
largest = prices[i]

while i>=0:
    if prices[i]>=largest:
        largest = prices[i]
    else:
        ans+= largest - prices[i]
        largest = prices[i]
    i = i - 1

print(ans)

