# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#
# Example 1:
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
# Constraints:
#
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

# Thoughts
# Similar to most water, but we need to calculate the empty space between walls that can trap rain water.
# From looking at the picture, I want to be able to use pointers, one that starts at the beginning and the second one that starts after it.
# Move the right pointer until water can't be trapped, this means that the right wall is higher than the second one.
# Along the way, the amount of water trapped needs to be calculated. After that, the right pointer will be the left and
# the right will be right + 1. In the scenario that the left and right are the same height, we should move both pointers until
# the right is smaller or larger. I am going to assume that water can not be held on the edges too. Edge case would be if left has height
# and all rights after are just 0, I might have to keep a tracker for this, or submit and see if that algorithm is ok first.
# This means that time complexity is O(n) and space is O(1).
# Additional notes as I am working on problem
# There are some edge cases
# 1. If the right most vertical is smaller than the current left height, then we need to scrap the total
# 2. In the 4,2,3 case, the left vertical needs to be trimmed down to 3 so that the space between 3,2,3 can be calculated.
# Not entirely sure what the right way to solve this is but any height that doesn't exist at least 2 times needs to be trimmed down.
# This means that I need to create another algorithm that runs in O(n) time to trim down the heights. Still something feels off.
# Question is if I can calculate the volume without trimming the height.
# I can also try calculating the volume for each position in the list. Find the max left vertical and max right vertical and subtract the min of the two.
# If I scan from each point, then it is O(n^2) time complexity. Once the max left and right is found, it can be used as a checkpoint until
# the ith element is greater than right. This will reduce the time complexity to O(n)

# Attempt 1
# def trapped_water(height: list[int]):
#     volume = 0
#     left, right, end = 0, 1, len(height)-1
#     while right < end:
#         while height[left] == height[right]:
#             left += 1
#             right += 1
#         if height[left] < height[right]:
#             left = right
#             right += 1
#         else:
#             current_water = 0
#             highest_right = 0
#             while height[left] > height[right] and right < end:
#                 current_water += height[left] - height[right]
#                 right += 1
#                 highest_right = max(highest_right, height[right])
#             if right == end and height[left] <= height[right]:
#                 volume += current_water
#                 right += 1
#             elif right < end:
#                 volume += current_water
#                 left = right
#                 right += 1
#             else:
#                 height[left] = highest_right
#                 right = left + 1
#     return volume


# Attempt 2
# def trapped_water(height: list[int]):
#     if len(height) < 3:
#         return 0
#
#     volume = 0
#     left_peak_index = 0
#     right_peak_index = find_right_peak(1, height)
#     end = len(height)-1
#     i = 1
#     while i < end:
#         while height[i] < height[left_peak_index] and height[i] < height[right_peak_index]:
#             current_volume = min(height[left_peak_index], height[right_peak_index]) - height[i]
#             print(i, current_volume, height[left_peak_index], height[right_peak_index])
#             volume += min(height[left_peak_index], height[right_peak_index]) - height[i]
#             i += 1
#         if i < end:
#             left_peak_index = i
#             right_peak_index = find_right_peak(i, height)
#             i += 1
#
#     return volume
#
# def find_right_peak(midpoint, height):
#     right = midpoint + 1
#     peak = height[right]
#     peak_index = right
#     while right < len(height)-1:
#         right += 1
#         if height[right] > peak:
#             peak_index = right
#             peak = height[right]
#     return peak_index

# Getting a hint from claude. Revolves around finding the tallest peak for each index and then recalculating the volume after.
# At this point, I'm just gonna do the problem. Still seems O(n^2) to me, but we'll see.
# So I was right that it is still O(n^2). I need to propagate the highest left or right so that the problem is O(n).
# Looks like I can just compute max left for each index, max right for each index, and combine the results.
# This would change the time complexity to O(n)

# Attempt 3
def trapped_water(height: list[int]):
    left_max_map = calculate_left_max(height)
    right_max_map = calculate_right_max(height)
    volume = 0
    for i in range(1, len(height)-1):
        curr = height[i]
        left_max = left_max_map[i]
        right_max = right_max_map[i]
        if left_max > curr and right_max > curr:
            volume += min(left_max, right_max) - curr
    return volume

def calculate_left_max(height):
    max_map = {}
    curr_max = 0
    for i in range(1, len(height)-1):
        left = height[i-1]
        curr_max = max(curr_max, left)
        max_map[i] = curr_max
    return max_map

def calculate_right_max(height) :
    max_map = {}
    curr_max = 0
    for i in range(len(height)-2, 0, -1):
        right = height[i+1]
        curr_max = max(curr_max, right)
        max_map[i] = curr_max
    return max_map

print(trapped_water([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trapped_water([4,2,0,3,2,5]))
print(trapped_water([4,2,3]))
print(trapped_water([5,5,1,7,1,1,5,2,7,6]))