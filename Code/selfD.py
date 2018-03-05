x = 22
ans = []

for i in range(1, x + 1):
    if len(str(i)) == 0:
        ans.append(i)
    else:
        cnt_ = 0
        for k in range(len(str(i))):
            if int(str(i)[k]) == 0:
                break
            if i % int(str(i)[k]) == 0:
                cnt_ += 1

        if cnt_ == len(str(i)):
            ans.append(i)

print(ans)