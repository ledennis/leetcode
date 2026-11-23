# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
# Example 1:
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#     1->4->5,
# 1->3->4,
# 2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6
# Example 2:
#
# Input: lists = []
# Output: []
# Example 3:
#
# Input: lists = [[]]
# Output: []
#
#
# Constraints:
#
# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

# Thoughts
# Initial thought is that I need k pointers and each pointer is added to a map as they are gathered, keeping track
# of the smallest number. Once that initial scan is done, you can link the smallest val all together, and add their next
# values to the map. Delete from hash afterward. Next, find the next smallest number and repeat until the hashmap is empty.
# Finding the smallest number would take k time each time. Time would be O(k*n), which sounds pretty bad. Need to save time when
# finding the smallest. 


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def merge_k_sorted_lists(lists: list[ListNode | None]):
    if not lists:
        return None

    smallest = float('inf')
    value_map = {}
    new_head = None
    curr_head = None
    for i in range(len(lists)):
        if lists[i]:
            current_val = lists[i].val
            if current_val not in value_map:
                value_map[current_val] = [lists[i]]
            else:
                value_map[current_val] = value_map[current_val] + [lists[i]]
            if current_val < smallest:
                smallest = current_val

    while len(value_map) > 0:
        heads = value_map[smallest]
        for head in heads:
            if new_head is None:
                new_head = head
                curr_head = new_head
            else:
                curr_head.next = head
                curr_head = curr_head.next
            next_node = head.next
            if next_node:
                while next_node and next_node.val == smallest:
                    curr_head.next = next_node
                    curr_head = curr_head.next
                    next_node = next_node.next
                if next_node:
                    if next_node.val not in value_map:
                        value_map[next_node.val] = [next_node]
                    else:
                        value_map[next_node.val] = value_map[next_node.val] + [next_node]
        del value_map[smallest]
        smallest = float('inf')
        for key in value_map:
            if key < smallest:
                smallest = key

    return new_head

def print_nodes(nodes: ListNode):
    while nodes is not None:
        print(nodes.val)
        nodes = nodes.next

a = ListNode(1)
b = ListNode(4)
c = ListNode(5)
a.next = b
b.next = c
d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
d.next = e
e.next = f
g = ListNode(2)
h = ListNode(6)
g.next = h

i = ListNode(1)
k = ListNode(1)
j = ListNode(2)
i.next = k
k.next = j

l = ListNode(1)
m = ListNode(2)
n = ListNode(2)
l.next = m
m.next = n

# print_nodes(merge_k_sorted_lists([a, d, g]))
print_nodes(merge_k_sorted_lists([i, l]))
