# 242. Valid Anagram

# Given two strings s and t, return true if t is an
# anagram
# of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

# Constraints:

#     1 <= s.length, t.length <= 5 * 104
#     s and t consist of lowercase English letters.

 
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_dict = {}
    t_dict = {}
    
    for char in s:
        # Get current count of character from dictionary (default to 0 if not found)
        # Then increment by 1 and store back in dictionary
        s_dict[char] = s_dict.get(char, 0) + 1
    for char in t:
        t_dict[char] = t_dict.get(char, 0) + 1
    
    return s_dict == t_dict

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))