# def primes(n):
#     primfac = []
#     d = 2
#     while d*d <= n:
#         while (n % d) == 0:
#             primfac.append(d)  # supposing you want multiple factors repeated
#             n //= d
#         d += 1
#     if n > 1:
#        primfac.append(n)
#     return primfac
#
# ans = primes(9)
# chk = [1, 2, 3, 5]
# cnt = 0
#
# for i in ans:
#     if i in chk:
#         cnt += 1
#
# if cnt==len(ans):
#     print("Ugly")
# else:
#     print("not Ugly")

print(5 % 2 == 0 < 5)
