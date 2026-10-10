# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
#
#
# Constraints:
#
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# Thoughts
# Need to strip the input of all non-alphanumeric characters and to lowercase all characters
# Two pointers, start and beginning, will compare the two and make sure they are the same.
# Once the pointers intersect or are start is greater than end, the algo should return true
# O(n) time complexity and O(1) space since it is going through each n once and there is no structure being created

def valid_palindrome(s: str):
    stripped_text = "".join(filter(str.isalnum, s.lower()))
    start = 0
    end = len(stripped_text)-1
    while start != end and start < end:
        if stripped_text[start] == stripped_text[end]:
            start += 1
            end -= 1
        else:
            return False

    return True

print(valid_palindrome("A man, a plan, a canal: Panama"))
print(valid_palindrome("race a car"))
print(valid_palindrome(""))
print(valid_palindrome("0P"))
