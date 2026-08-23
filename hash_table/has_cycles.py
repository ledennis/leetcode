# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
#
# Example 1:
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
# Constraints:
#
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.
#
#
# Follow up: Can you solve it using O(1) (i.e. constant) memory?

# Notes
# All node values should be unique to search for cycles given a linked list. Create a hash table where keys are the val and if a key exist, then there is a cycle.
# O(n) time because every node has to be searched through to discover if there is a cycle and O(n) memory for each node stored in the hash table.
# Follow up: Use tortoise and the hare pointers to find a cycle. Two pointers where one moves one step and the other moves two steps, if the val's match, then a cycle exist.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycles(node: ListNode) -> bool:
    if node.next is None:
        return False
    return detect_cycle(node.next, node.next.next)
def detect_cycle(tortoise: ListNode, hare: ListNode) -> bool:
    if tortoise is None or tortoise.next is None or hare is None or hare.next is None:
        return False
    if tortoise is hare:
        return True
    return detect_cycle(tortoise.next, hare.next.next)

nodeA = ListNode(3)
nodeB = ListNode(2)
nodeC = ListNode(0)
nodeD = ListNode(-4)
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeB

print(has_cycles(nodeA))

nodeE = ListNode(1)
nodeF = ListNode(0)
nodeE.next = nodeF
nodeF.next = nodeE

print(has_cycles(nodeE))

nodeG = ListNode(1)
print(has_cycles(nodeG))