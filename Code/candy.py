candy = [1,1,2,2,3,3]

if len(candy)/2 > len(set(candy)):
    print(len(set(candy)))
else:
    print(len(candy)/2)