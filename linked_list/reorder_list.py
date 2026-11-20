# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000
# Thoughts
# After looking at the problem, it looks like I can create a queue for the first half and a stack for the second half, and connect the nodes
# starting from the stack and then queue. Travel through the nodes to find len n, and then back through the nodes, and then linking
# the two data structures. Time O(n) Space O(n)
# Misunderstood the problem, I can only manipulate the nodes by changing the pointers.

# I think the answer revolves around being able to look ahead to do in place manipulation. Swap the next with the last and do that until there
# isn't enough last to swap. This would be O(n) solution since the algorithm will run through the entire node list to find the last node everytime

from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def reorder_list(head: ListNode | None):
#     if head is None:
#         return None
#
#     head_copy = head
#     count = 0
#     while head_copy is not None:
#         count += 1
#         head_copy = head_copy.next
#
#     halfway = count // 2
#     head_two = head
#     new_count = 0
#     first_half = deque()
#     second_half = []
#     while head_two is not None:
#         if new_count < halfway:
#             first_half.append(head_two.val)
#         else:
#             second_half.append(head_two.val)
#         new_count += 1
#         head_two = head_two.next
#
#     new_head = None
#     next = None
#     while first_half and second_half:
#         first = ListNode(first_half.popleft())
#         second = ListNode(second_half.pop())
#         first.next = second
#         if new_head is None:
#             new_head = first
#             next = first.next
#         else:
#             next.next = first
#             next = next.next.next
#
#     while first_half:
#         new_node = ListNode(first_half.pop())
#         next.next = new_node
#         next = next.next
#
#     while second_half:
#         new_node = ListNode(second_half.pop())
#         next.next = new_node
#         next = next.next
#
#     return new_head

def reorder_list(head: ListNode | None):
    if head is None:
        return None

    head_copy = head
    while True:
        copy_copy = head_copy
        second_last = copy_copy
        if not second_last.next or not second_last.next.next:
            return head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next.next = head_copy.next
        head_copy.next = second_last.next
        second_last.next = None
        head_copy = head_copy.next.next

    return head

def print_nodes(nodes: ListNode):
    while nodes is not None:
        print(nodes.val)
        nodes = nodes.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
# d.next = e

print_nodes(reorder_list(a))
