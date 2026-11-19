# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#
#
# Example 1:
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#
#
# Constraints:
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
# Thoughts
# Have two pointers from each list, link the nodes by whichever pointer is smaller until both pointers are empty
# O(n) time complexity solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_list(list1: ListNode | None, list2: ListNode | None):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    pointer_one, pointer_two = list1, list2
    head = None
    linker = None

    while pointer_one is not None and pointer_two is not None:
        current = None
        if pointer_one.val <= pointer_two.val:
            current = ListNode(pointer_one.val)
            pointer_one = pointer_one.next
        else:
            current = ListNode(pointer_two.val)
            pointer_two = pointer_two.next

        if head is None:
            head = current
            linker = head
        else:
            linker.next = current
            linker = linker.next

    if pointer_one is not None:
        linker.next = pointer_one
    if pointer_two is not None:
        linker.next = pointer_two

    return head

def print_nodes(nodes: ListNode):
    while nodes is not None:
        print(nodes.val)
        nodes = nodes.next

a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
a.next = b
b.next = c

d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
d.next = e
e.next = f

print_nodes(merge_two_sorted_list(a, d))
