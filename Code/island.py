grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

height = len(grid)
weight = len(grid[0]) if height else 0
sum_ = 0
for h in range(height):
    for w in range(weight):
        if grid[h][w] == 1:
            sum_ += 4
            if h > 0 and grid[h-1][w]:
                sum_ -= 2
            if w > 0 and grid[h][w-1]:
                sum_ -= 2

print(sum_)