# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#
# Constraints:
#
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

# Thoughts
# Brute force solution is to choose go through every triplet combination and see if it equals 0. O(n^3) complexity.
# I already want to sort the array since it is more likely to find the 3rd number in between. With that in mind,
# I am thinking that the initial number can start from the middle and then two pointer can be implemented to see if there is a
# combination. Feels like some sort of merge algorithm can be done so it might be good to look up the optimal solution after.
# Quick problem is how to guarantee that duplicate triplets won't be generated with this approach, so I will implement an O(n^2)
# solution by using and move from there. ANOTHER thought, is to create a map where the key is the value and the map holds all the
# indices that that value lives in. This way, a lookup can be done to save O(n) time and make it O(1). This also guarantees that
# the algorithm only goes through each element one time when it finds the triplet combinations using the double pointer method.
# Once the pointers have a difference of 2, the algorithm should end. This means that the algorithm will run in O(n+nlogn) time with O(n) space.

# def three_sum(nums: list[int]):
#     triplets = []
#     sorted_nums = sorted(nums)
#     print(sorted_nums)
#
#     index_map = {}
#     for i, n in enumerate(sorted_nums):
#         if n not in index_map:
#             index_map[n] = [i]
#         else:
#             index_map[n] = index_map[n] + [i]
#
#     start = 0
#     end = len(sorted_nums) - 1
#     alternate = True
#     while start <= end-2:
#         i = sorted_nums[start]
#         k = sorted_nums[end]
#         j = 0-(i+k)
#         if j in index_map:
#             indices = index_map[j]
#             def different_index(x):
#                 if x != start and x > start and x != end and x < end:
#                     return True
#                 return False
#             filtered_indices = list(filter(different_index, indices))
#             if len(filtered_indices) > 0:
#                 triplets.append([i, k, j])
#         if alternate:
#             start = start + 1
#             alternate = False
#         else:
#             end = end - 1
#             alternate = True
#     return triplets

# Thoughts pt2
# Interestingly enough, I was headed in the right direction but the duplicates made the problem harder. I tried implementing some logic
# to search within the indices stored in a hashmap but duplicates still occurred. To improve, I should iterate at the beginning and
# start the two pointer search from there.

def three_sum(nums: list[int]):
    triplets = []
    sorted_nums = sorted(nums)
    end = len(sorted_nums)

    for i in range(len(sorted_nums) - 2):
        if sorted_nums[i] > 0:
            break # not possible to find a combination that adds to 0 since the number is positive

        if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
            continue # skipping duplicates once they are processed

        left = i + 1
        right = end - 1
        while left < right:
            total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                triplets.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                left += 1
                right -= 1
                while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                    left += 1
                while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                    right -= 1
    return triplets

print(three_sum([-1,0,1,2,-1,-4]))
print(three_sum([0,1,1]))
print(three_sum([0,0,0]))
