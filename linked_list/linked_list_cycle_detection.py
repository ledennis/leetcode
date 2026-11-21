# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#
# Return true if there is a cycle in the linked list. Otherwise, return false.
#
#
#
# Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:
#
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:
#
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
# Constraints:
#
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
#
#
# Follow up: Can you solve it using O(1) (i.e. constant) memory?
# Thoughts
# There is an algorithm in which name's I forgot, but the idea is the tortoise and the hare.
# One pointer moves one step while another pointer moves two steps, if the two pointers ever meet,
# there is a cycle, otherwise there are no cycles. Will implement first before looking up the algorithm.
# It is called Floyd's Tortoise and Hare algorithm
# Time complexity is O(n) since the list will be scanned twice by both pointers
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def linked_list_cycle_detection(head: Optional[ListNode]):
    if head is None or not head.next or not head.next.next:
        return False
    hare = head.next.next
    tortoise = head
    while hare is not None and tortoise is not None:
        if hare is tortoise:
            return True
        if not hare.next or not hare.next.next:
            return False
        if not tortoise.next:
            return False
        hare = hare.next.next
        tortoise = tortoise.next

    return False

a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)
a.next = b
b.next = c
c.next = d
d.next = b
print(linked_list_cycle_detection(a))