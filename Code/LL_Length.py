class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function is in LinkedList class. It inserts
    # a new node at the beginning of Linked List.
    def push(self, new_data):
        # 1 & 2: Allocate the Node &
        #     Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    # This function counts number of nodes in Linked List
    # iteratively, given 'node' as starting node.
    def getCount(self):
        temp = self.head  # Initialise temp
        count = 0  # Initialise count

        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count

    def reverseList(self):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        temp = self.head
        prev = None

        if not temp:
            return []

        while temp:
            res = Node(temp.data)
            res.next = prev
            prev = res
            temp = temp.next

        return res

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next



    def removeDup(self):
        set_ = set()
        tmp = self.head
        while tmp:
            set_.add(tmp.data)
        return set_

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        slow_ = head
        fast = head

        while fast and fast.next:
            slow_ = slow_.next
            fast = fast.next.next
            if slow_ == fast:
                return True

        return False

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        slow_ = head
        fast = head

        while fast and fast.next:
            slow_ = slow_.next
            fast = fast.next.next
            if slow_ == fast:
                break

        if fast == None or fast.next == None:
            return None

        slow_ = head
        while slow_ != fast:
            slow_ = slow_.next
            fast = fast.next

        return fast

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        startA = headA
        startB = headB
        lengthA, tailA = self.getLength(headA)
        lengthB, tailB = self.getLength(headB)

        if tailA != tailB:
            return None

        if lengthA > lengthB:
            longer = startA
            shorter = startB
        else:
            longer = startB
            shorter = startA

        diff = abs(lengthA - lengthB)

        while longer != None and diff > 0:
            longer = longer.next
            diff = diff - 1

        while shorter != longer:
            shorter = shorter.next
            longer = longer.next

        return shorter

    def getLength(self, List):

        count_ = 1
        if not List:
            return count_

        current = List
        while current.next != None:
            count_ += 1
            current = current.next

        return count_, current

def intersectionList(head1, head2):
    while head1:
        while head2:
            if head1.data == head2.data:
                print("Intersection  at Point {0}".format(head2.data))
                break
            head2 = head2.next
        head1 = head1.next
    print("No Intersection")





if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(1)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    print("Count of nodes is :", llist.getCount())

    print("List Values is", llist.reverseList())
    print("Set of dups is")
    remove_dup = llist.removeDup()
    print(remove_dup)


