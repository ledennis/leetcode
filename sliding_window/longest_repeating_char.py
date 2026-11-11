# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
#
#
#
# Example 1:
#
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:
#
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length
# Thoughts
# Seems pretty tricky. First thought that comes into mind is to have a pointer for each new character that is introduced so that
# that's the next start. Use k as a counter to keep track of changeable characters, once k is 0, count the remainder of valid characters.
# Start at the new start afterwards. There needs to be an optimization on the start though I think, otherwise the time complexity can be
# O(n^2). Can also do a check on the rest of the string to end the algorithm if max length is greater than what remains.

# def longest_repeating_char(s: str, k: int):
#     start = 0
#     curr_longest = 0
#     replace_counter = k
#     has_new_start = False
#     s_length = len(s)-1
#     while start < s_length:
#         char = s[start]
#         curr = start
#         curr_start = start
#         longest = 1
#         while replace_counter > 0 and curr < s_length:
#             if s[curr+1] != char:
#                 replace_counter -= 1
#                 if not has_new_start:
#                     start = curr + 1
#                     has_new_start = True
#             longest += 1
#             curr += 1
#         while curr < s_length and s[curr+1] == char:
#             longest += 1
#             curr += 1
#         if replace_counter > 0 and curr_start > 0:
#             left_pointer = curr_start
#             while replace_counter > 0 and left_pointer > 0:
#                 if s[left_pointer-1] != char:
#                     replace_counter -= 1
#                 longest += 1
#                 left_pointer -= 1
#         curr_longest = max(longest, curr_longest)
#         if not has_new_start:
#             start += 1
#         has_new_start = False
#         replace_counter = k
#     return curr_longest
#
# print(longest_repeating_char('ABAB', 2))
# print(longest_repeating_char('AABABBA', 1))
# print(longest_repeating_char('ABBB', 1))

# More thoughts
# The previous algorithm only moves right. In the scenario of "ABBB", it needs to be able to move left. After seeing this example,
# I think it makes more sense to find the longest repeating substring first, and then slide the window left or right depending on k.
# Keep track of longest substrings and then compute which one has the greater repeating characters, This would make the algorithm O(n) time.
# I would need to store the start and end for each of the longest. Question is how to determine if going left or right is better.
# Just gonna go with look ahead and choosing the max for now.

# def longest_repeating_char_ranges(s: str):
#     longest = 0
#     start_end_indices = []
#     for i in range(0, len(s)):
#         char = s[i]
#         curr = i
#         count = 1
#         while curr + 1 < len(s)-1 and s[curr+1] == char:
#             count += 1
#             curr += 1
#         if count == longest:
#             start_end_indices.append([i, curr])
#         elif count > longest:
#             start_end_indices.clear()
#             start_end_indices.append([i, curr])
#             longest = count
#
#     return start_end_indices
#
# def longest_look_ahead(curr_range: list, s: str,  k: int):
#     left = curr_range[0]
#     right = curr_range[1]
#     count = k
#     char = s[left]
#     while count > 0:
#         if left > 0:
#
#
#
# def longest_repeat_char(s: str, k: int):
#     longest_substrings = longest_repeating_char_ranges(s)

# More more thoughts
# Saw a tip on the discussion on leetcode, tip was O(26n) = O(n). 26 represents the english alphabet so we can sliding window
# for each letter and return the max out of all letters. Store the letters in a list and process each one.

def longest_repeating_char(s: str, k: int):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    longest = 0
    for l in letters:
        replaceable = k
        count = 0
        start = 0
        for i in range(0, len(s)):
            if s[i] == l:
                count += 1
            else:
                if replaceable > 0:
                    replaceable -= 1
                    count += 1
                else:
                    longest = max(count, longest)
                    while replaceable == 0 and start <= i and start < len(s):
                        if s[start] != l:
                            replaceable += 1
                        count -= 1
                        start += 1
                    if start == i:
                        replaceable = k
                        count = 0
                    replaceable -= 1
                    count += 1
        longest = max(count, longest)

    return longest

print(longest_repeating_char('ABAB', 2))
print(longest_repeating_char('AABABBA', 1))
print(longest_repeating_char('ABBB', 1))
print(longest_repeating_char('AAAA', 0))
