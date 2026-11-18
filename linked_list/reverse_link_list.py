# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Example 1:
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:
#
#
# Input: head = [1,2]
# Output: [2,1]
# Example 3:
#
# Input: head = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Thoughts
# Iteratively, the algorithm just needs to iterate through the list next until next is None. O(n) solution.
# Recursively, you create a node and pass it on as a parameter until the latest node is None.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_link_list_param(curr: ListNode | None, prev: ListNode):
    if curr is None:
        return prev
    next = ListNode(curr.val)
    next.next = prev
    return reverse_link_list_param(curr.next, next)

def reverse_link_list(head: ListNode | None):
    if head is None:
        return None
    return reverse_link_list_param(head.next, ListNode(head.val))

def print_list(head: ListNode):
    while head is not None:
        print(head.val)
        head = head.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
# print_list(a)
print_list(reverse_link_list(a))