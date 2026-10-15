# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
#
# Example 1:
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
#
# Input: height = [1,1]
# Output: 1
#
#
# Constraints:
#
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

# Thoughts
# Easier to see with an image but thinking about two pointers and this problem, it makes sense to create an algorithm that can calculate the current
# area that the two pointers are at. Intuitively, you would move the left or right based on which one is smaller.
# With this in mind, the time complexity would be O(n) with O(1) space since the only thing to keep track of is the most area.
# In the edge case that there is a tie, I would do a look ahead to find the next tallest vertical line between the left and right.

def most_water(height: list[int]):
    area = 0
    left, right = 0, len(height)-1
    while left < right:
        base = right - left
        left_vertical, right_vertical = height[left], height[right]
        area = max(area, calc_water(left_vertical, right_vertical, base))
        if left_vertical < right_vertical:
            left += 1
        elif left_vertical > right_vertical:
            right -= 1
        else:
            if height[left+1] < height[right-1]:
                right -= 1
            else:
                left += 1

    return area


def calc_water(left: int, right: int, base: int):
    return min(left, right) * base

print(most_water([1,8,6,2,5,4,8,3,7]))
print(most_water([1,1]))
