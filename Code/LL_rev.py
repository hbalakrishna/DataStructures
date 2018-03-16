class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        set_ = set()
        prev = ListNode(0)
        while head:
            if head.val in set_:
                prev.next = head.next
            else:
                set_.add(head.val)
                prev = head
            head = head.next

        return prev

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

lllist = ListNode(1)
lllist2 = ListNode(2)
lllist.next = lllist2

rev = Solution()
print(rev.deleteDuplicates(lllist))