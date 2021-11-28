class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverse(self, head):

        prev = None
        curr = head
        temp = prev

        while(curr):

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def print1(self, node):
        while node:
            print(node.val, "==>", end=" ")
            node = node.next


l1 = Node(1)
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)

l1.next = l2
l2.next = l3
l3.next = l4

s = Solution()
s.print1(s.reverse(l1))
