# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#
# Example 1:
# Input: s = "leetcode"
# Output: 0
#
# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.
#
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
#
# Example 3:
# Input: s = "aabb"
# Output: -1
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only lowercase English letters.

# Notes
# The description of this problem sucks. First non-repeating character means the first unique character where the character does not repeat throughout the string.
# Create a hashmap where the letters are keys and each letter has a count. Loop through the string again and return the first index where the count is 1 else -1
# O(n) time since there are two loops through the string and O(n) space where n is equal to the amount of letters in s

def first_unique_char(s: str):
    letter_map = {}

    for char in s:
        if char not in letter_map:
            letter_map[char] = 1
        else:
            letter_map[char] = letter_map[char]+1

    for index in range(len(s)):
        if letter_map[s[index]] == 1:
            return index

    return -1

print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))
print(first_unique_char("dddccdbba"))
