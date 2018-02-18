import math

# n = 4
# count = 0
#
# for i in range(2, n):
#     count_prime = True
#     for j in range(2, i ):
#         if i % j == 0:
#             count_prime = False
#     if count_prime:
#             count = count + 1
#
# print(count)
#
#
# print(all(n % i for i in range(2, int(math.sqrt(n)) + 1)))

def eratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    count = 0
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, n):
        if prime[p]:
            # print(p)
            count = count + 1
    return count

print(eratosthenes(4))






