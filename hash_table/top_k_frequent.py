# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
#
# Output: [1,2]
#
# Example 2:
#
# Input: nums = [1], k = 1
#
# Output: [1]
#
# Example 3:
#
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
#
# Output: [1,2]
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# Thoughts:
# Just from reading the prompt and examples, K most frequent most likely means the most frequent up to K elements.
# Not entirely sure if that makes sense but let's go with it.
# The most intuitive answer would be to create a hashmap and count the number of elements. After going through all elements,
# go through the map and create a list of tuples with count and element. Sort the list by count and return the top K elements.
# Time complexity would be O(n), collecting count by going through n, + O(n), create tuples, + O(nlogn) sorting and space would be O(n) for storing n elements.

def top_k_frequent(nums: list[int], k: int):
    count_map = {}
    for n in nums:
        if n not in count_map:
            count_map[n] = 1
        else:
            count_map[n] = count_map[n] + 1

    tuples = []
    for key in count_map:
        tuples.append((count_map[key], key))

    tuples.sort(reverse=True, key=tuple_sort)
    resp = []
    for i in range(k):
        resp.append(tuples[i][1])
    return resp

def tuple_sort(tup):
    return tup[0]

print(top_k_frequent(nums = [1,1,1,2,2,3], k = 2))
print(top_k_frequent(nums = [1], k = 1))
print(top_k_frequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))
