# 9. Palindrome Number
# Solved
# Easy
# Topics
# Companies
# Hint

# Given an integer x, return true if x is a
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

# Constraints:

#     -231 <= x <= 231 - 1

 
# Follow up: Could you solve it without converting the integer to a string?

def isPalindrome(x):
    if x < 0:
        return False
    
    reverse = 0
    xcopy = x
    
    while x > 0:
        reverse = (reverse * 10) + (x % 10)
        x = x // 10
        
    return reverse == xcopy

print(isPalindrome(121))

# 1. x = 123, reverse = 0
# First iteration:
# reverse = (0 * 10) + (123 % 10) = 3
# x = 123 // 10 = 12
# 3. Second iteration:
# reverse = (3 * 10) + (12 % 10) = 32
# x = 12 // 10 = 1
# Third iteration:
# reverse = (32 * 10) + (1 % 10) = 321
# x = 1 // 10 = 0
# Loop ends since x = 0
# Compare reverse (321) with xcopy (123) → return False