# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
# Example 1:
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:
#
# Input: nums = [1,0,1,2]
# Output: 3
#
#
# Constraints:
#
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# Thoughts
# Has to run in O(n) time so sorting is out of the question. That means that there is a way to go through each element once (or n times)
# to figure out the solution. We do not want to go looking for the next element by searching through the array since it is O(n) time to search.
# Searching in a map is O(1) if search needs to be done. If the array was sorted, then popping off the elements to determine K would take O(n) time.
# An idea would be to see if there exists an N-1 number based on N. Once you searched through the hash map until there is no N-1, then you can
# start counting for consecutive elements. Once an element is accounted for, it should be deleted to reduce time complexity.

def longest_consecutive(nums: list[int]):
    numbers_map = {}
    count = 0
    for n in nums:
        numbers_map[n] = True

    for n in nums:
        if n in numbers_map:
            root = find_root(numbers_map, n)
            consecutive_count = count_consecutive(numbers_map, root)
            count = consecutive_count if consecutive_count > count else count

    return count


def find_root(map, current):
    root = current
    while root-1 in map:
        root = root-1
    return root

def count_consecutive(map, root):
    count = 0
    while root in map:
        count += 1
        del map[root]
        root = root+1
    return count

print(longest_consecutive([100,4,200,1,3,2]))
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))
print(longest_consecutive([1,0,1,2]))
