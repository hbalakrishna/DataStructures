class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self,l1, l2):
        carry = 0
        result = ListNode(0)
        curr = result
        while (l1 is not None or l2 is not None):
            sum1 = 0
            l1val = 0 if l1 is None else l1.val
            l2val = 0 if l2 is None else l2.val
            sum1 += l1val + l2val + carry

            carry = 1 if sum1 >= 10 else 0
            sum1 = sum1 % 10 if carry > 0 else sum1
            curr.next = ListNode(sum1)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            curr.next = ListNode()

        return result.next


def mergeTwoLists(self, l1, l2):
    if not l1 and not l2:
        return None

    node = guard_node = ListNode(0)

    while l1 and l2:
        if l1.val <= l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next

    if l1 or l2:
        node.next = l1 or l2

    return guard_node.next
