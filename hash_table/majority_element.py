# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
#
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 5 * 10^4
# -109 <= nums[i] <= 10^9
# The input is generated such that a majority element will exist in the array.
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#
# Notes
# Intuitive solution would be to figure out what n/2 is and return back the first number that has more than n/2 occurrences.
# To keep track of the count, we can use a hashmap where there are n keys and keep the count there.
# Follow-up question asks to solve for O(n) time and O(1) space, meaning we can't use a hashmap.
# Guaranteed that there is an element that shows up > n/2 times, meaning (n/2) + 1 times.
# Means that an element can not be majority if there is not enough indexes left to search for
# O(1) space solution will need a pointer to go back to the next element that needs to be searched for

def get_majority_element_hash_map(nums: list[int]):
    if len(nums) == 1:
        return nums[0]

    count_map = {}
    threshold = len(nums)//2
    for n in nums:
        if n not in count_map:
            count_map[n] = 1
        else:
            count_map[n] = count_map[n]+1
            if count_map[n] > threshold:
                return n
    return -1

print(get_majority_element_hash_map([3,2,3]))
print(get_majority_element_hash_map([2,2,1,1,1,2,2]))
print(get_majority_element_hash_map([2,2,1,1,1,1,1,2,2]))

def get_majority_element_no_hash_map(nums: list[int]):
    if len(nums) == 1:
        return nums[0]

    threshold = len(nums)//2
    curr_index = 0
    curr = nums[curr_index]
    count = 0
    next_index = -1
    total_remainder = len(nums)
    while count <= threshold:
        if total_remainder < threshold:
            return curr
        if nums[curr_index] == curr:
            count += 1
            total_remainder -= 1
        elif next_index == -1:
            next_index = curr_index
        curr_index += 1

        if len(nums[curr_index:]) + count - 1 < threshold and next_index > -1:
            curr_index = next_index
            curr = nums[curr_index]
            count = 0
            next_index = -1

    return curr

print(get_majority_element_no_hash_map([3,2,3]))
print(get_majority_element_no_hash_map([6,5,5]))
print(get_majority_element_no_hash_map([2,2,1,1,1,2,2]))
print(get_majority_element_no_hash_map([2,2,1,1,1,1,1,2,2]))