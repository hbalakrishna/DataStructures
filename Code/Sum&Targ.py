numbers=[2,3,4]
target= 100
idx1 = 0
idx2 = 0


for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            idx2 = j
            idx1 = i
        else:
            numbers[i] = 0



print(idx1 + 1, idx2 +1)