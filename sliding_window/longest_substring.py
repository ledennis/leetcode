# Given a string s, find the length of the longest substring without duplicate characters.
#
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
# Constraints:
#
# 0 <= s.length <= 105
# s consists of English letters, digits, symbols and spaces.
#
# Thoughts
# To make the time complexity O(n), the algorithm needs to be able to keep track the current letters in the substring.
# The window would move based on the next character, if a character that already existed prior to the next character occurs,
# the window would shrink from the left until that character is removed. I am think that if a hashmap was used to keep track of the
# index of the latest for each character, the substring can be recalculated. O(n) time complexity and O(n) space

def longest_substring(s: str) -> int:
    if len(s) <= 1:
        return len(s)

    letter_map = {}
    longest = 0
    current = 0
    start = 0

    for i in range(0, len(s)):
        if s[i] not in letter_map:
            current += 1
            letter_map[s[i]] = i
        else:
            longest = max(longest, current)
            while s[start] != s[i] and start < i-1:
                del letter_map[s[start]]
                start += 1
                current -= 1
            start += 1

    return max(longest, current)

print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))
print(longest_substring("ccbbcc"))
print(longest_substring("baaabca"))
