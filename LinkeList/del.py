class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = ListNode(0)
        while l1 or l2:
            if l1.val > l2.val:
                curr.next = ListNode(l2.val)
                curr.next.next = ListNode(l1.val)
            else:
                curr.next = ListNode(l1.val)
                curr.next.next = ListNode(l2.val)
            l1 = l1.next
            l2 = l2.next
        return curr.next


l1 = ListNode(1)
a = ListNode(2)
b = ListNode(4)
l1.next = a
a.next  = b

l2 = ListNode(1)
a = ListNode(3)
b = ListNode(4)
l2.next = a
a.next = b

sol = Solution()
print(sol.mergeTwoLists(l1,l2))

