# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:
#
# Input: strs = [""]
#
# Output: [[""]]
#
# Example 3:
#
# Input: strs = ["a"]
#
# Output: [["a"]]
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Thoughts
# Anagram is a group of letters that can be rearranged to form different words. An anagram contains a unique set of letters.
# A solution would be to sort each word alphabetically, and to push those words into a hashmap where the key is the sorted word.
# This would be an O(n * nlogn) solution, with O(n) space complexity since you're storing each word

def group_anagram(strs: list[str]):
    anagram_bucket = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_bucket:
            anagram_bucket[sorted_word] = [word]
        else:
            anagram_bucket[sorted_word].append(word)
    buckets = []
    for key in anagram_bucket:
        buckets.append(anagram_bucket[key])
    return buckets

print(group_anagram(["eat","tea","tan","ate","nat","bat"]))
print(group_anagram([""]))
print(group_anagram(["a"]))
