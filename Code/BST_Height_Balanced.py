def heightBal(node):
    if not node:
        return 0

    left_height = heightBal(node.left)

    if left_height == -1:
        return -1

    right_height = heightBal(node.right)

    if right_height == -1:
        return -1

    if (abs(left_height - right_height)>1):
        return -1

    return 1+max(right_height + left_height)



