# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
# Constraints:
#
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109

# Notes: Brute force solution would be to go through each number in the array and add itself to every other number until it equals the target val
# This solution would be O(n^2), which is usually never optimal
# Another possible solution would be to push all values onto a hashmap with the value as the key and the index as the value. Then go through
# each index to see if the subtraction of target - nums[i] exists within the hashmap. Look up is O(1) so the complexity and space would be O(n).

def two_sum(nums, target):
    if len(nums) == 2:
        return [0,1]
    value_ind_map = {}
    for i, val in enumerate(nums):
        value_ind_map[val] = i

    for i, val in enumerate(nums):
        diff = target - val
        if diff in value_ind_map and value_ind_map[diff] != i:
            return [i, value_ind_map[diff]]

    return -1

print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))
