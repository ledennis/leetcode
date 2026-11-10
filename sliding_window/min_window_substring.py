# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
#
# Constraints:
#
# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
#
#
# Follow up: Could you find an algorithm that runs in O(m + n) time?
#
# Thoughts
# Start with a pointer and need conditions to move the pointer, update the count, and update a map of values in M.
# This will be at least O(n) time with O(m) space. Will think of O(n+) solution later.
# Failed the submission, I was originally getting exact characters but that doesn't work for "aaaaaaaaaaaabbbbbcdd"
# To solve in O(n+m) time then, we need to first find a substring of the exact characters and then find the min substring within it.
# To find the substring within the substring, I will have two pointers, left and right, and move both pointers as long as the condition
# that the substring still exists is true.


def has_enough_letters(s_map, t_map):
    for k in t_map:
        if k not in s_map:
            return False
        if s_map[k] < t_map[k]:
            return False
    return True
def min_window_substring(s: str, t: str):
    letter_map = {}
    for i in t:
        if i not in letter_map:
            letter_map[i] = 1
        else:
            letter_map[i] = letter_map[i] + 1
    s_map = {}
    shortest = s[0] * (len(s) + 1)
    found_shortest = False
    left_pointer = 0
    for i in range(0, len(s), 1):
        if s[i] in letter_map:
            if s[i] not in s_map:
                s_map[s[i]] = 1
            else:
                s_map[s[i]] = s_map[s[i]]+1
            if has_enough_letters(s_map, letter_map):
                keep_moving = True
                while keep_moving:
                    if s[left_pointer] in s_map:
                        if s_map[s[left_pointer]] == letter_map[s[left_pointer]]:
                            keep_moving = False
                        else:
                            s_map[s[left_pointer]] = s_map[s[left_pointer]]-1
                            left_pointer += 1
                    else:
                        left_pointer += 1
                if len(shortest) > len(s[left_pointer: i+1]):
                    found_shortest = True
                    shortest = s[left_pointer: i+1]
    if found_shortest:
        return shortest
    return ""


print(min_window_substring('ADOBECODEBANC', 'ABC'))
print(min_window_substring('a', 'a'))
print(min_window_substring('a', 'aa'))
print(min_window_substring('ab', 'b'))
print(min_window_substring('aaaaaaaaaaaabbbbbcdd', 'abcdd'))
