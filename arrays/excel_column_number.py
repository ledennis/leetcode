# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
#
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
#
# Example 1:
#
# Input: columnNumber = 1
# Output: "A"
# Example 2:
#
# Input: columnNumber = 28
# Output: "AB"
# Example 3:
#
# Input: columnNumber = 701
# Output: "ZY"
#
# Constraints:
# 1 <= columnNumber <= 2^31 - 1

# Notes:
# There's some formula here with 26
# Example ABC
# (A(1 * 26 * 26) + (B(2*26)) + (C(3))
# 676 + 52 + 3 = 731
# This means that every column is a multiplication of the letter and x amount of previous columns times 26 for each column.

# Example ABCD
# (A(1 * 26 * 26 * 26) + (B( 2 * 26 * 26)) + (C(3 * 26)) + (D(4))
# 17576 + 1352 + 78 + 4 = 19010

# We can always find the last letter by modding the number by 26 and then searching for that letter in an alpha dict
# subtract from total after finding the mod
# increment a counter to mod an exponential of 26 for the next column
# Edgecase
# Z is a weird edgecase that we have to account for and applies when a number is modulo'd by 26, meaning we have to have a special case for it.
# Algorithm runs in O(1) time since the only variable is the columnNumber and the algorithmn does not scale based on that. Memory is O(1) with the static dict.

def find_col_number(columnNumber: int):
    alpha_dict = {
        0: 'Z', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I',
        10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q',
        18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
    }

    if columnNumber <= 26:
        return alpha_dict[columnNumber]
    total = columnNumber
    modded = total % 26
    column_name = alpha_dict[modded]
    total -= modded if modded > 0 else 26
    exp = 1
    while total > 0:
        div = total / 26 ** exp
        next_char_index = div % 26
        column_name = alpha_dict[next_char_index] + column_name
        if next_char_index == 0:
            total -= 26 * 26 ** exp
        else:
            total -= next_char_index * (26 ** exp)
        exp += 1
    return column_name

print(find_col_number(18278))
print(find_col_number(52))
print(find_col_number(1))
print(find_col_number(28))
print(find_col_number(701))
print(find_col_number(19010))