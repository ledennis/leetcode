# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# Example 1:
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:
#
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:
#
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

# Notes
# words and spaces, only the last space matters.
# Can a string end with just a space? If so, find the previous space as long as the index is more than -1 the last space (meaning there are multiple spaces).
# This is possible given example 2.
# If there are no spaces, return s
# Solution is O(n) where n is the length of s. Algorithmn will have to search all of s to find spaces.
# Python has a split method that will return a list of words from s where the input is the separator. To make it "harder", we can look at the first solution of finding the space indices
# Edge cases:
# # multiple spaces at end
# # no spaces

def len_of_last_word (s: str):
    last_space_index = s.rfind(' ')
    if last_space_index < 0:
        return len(s)

    if last_space_index == len(s)-1:
        next_space_index = s.rfind(' ', 0, len(s) - (len(s) - last_space_index))
        while next_space_index == last_space_index - 1:
            last_space_index = next_space_index
            next_space_index = s.rfind(' ', 0, len(s) - (len(s) - last_space_index))
        return last_space_index - next_space_index - 1

    return len(s[last_space_index+1::])

print(len_of_last_word("Hello World"))
print(len_of_last_word("   fly me   to   the moon  "))
print(len_of_last_word("luffy is still joyboy"))
