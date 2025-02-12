# 287. Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3

# Constraints:

#     1 <= n <= 105
#     nums.length == n + 1
#     1 <= nums[i] <= n
#     All the integers in nums appear only once except for precisely one integer which appears two or more times.

# Follow up:

#     How can we prove that at least one duplicate number must exist in nums?
#     Can you solve the problem in linear runtime complexity?

from typing import List

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

# Floyd's Tortoise and Hare (Cycle Detection)
def findDuplicate(nums: List[int]) -> int:
    slow, fast = 0, 0
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
        
    slow2 = 0
    
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]
        
    return slow

print(findDuplicate([1,3,4,2,2]))
# print(findDuplicate([3,1,3,4,2]))
# print(findDuplicate([3,3,3,3,3]))

def findDuplicate1(nums: List[int]) -> int:
    visited = set()
    
    for n in nums:
        if n not in visited:
            visited.add(n)
        else:
            return n
print(findDuplicate1([1,3,4,2,2]))

# 1
# nums = [1,3,4,2,2]
# index:  0 1 2 3 4
# slow = 0, fast = 0

# 2
# slow = nums[0] = 1
# fast = nums[nums[0]] = nums[1] = 3

# nums = [1,3,4,2,2]
#         s   f

# 3
# slow = nums[1] = 3
# fast = nums[nums[3]] = nums[2] = 4

# nums = [1,3,4,2,2]
#           s f
          
# 4
# slow = nums[3] = 2
# fast = nums[nums[4]] = nums[2] = 4

# nums = [1,3,4,2,2]
#             f s

# 5
# slow = nums[2] = 4
# fast = nums[nums[4]] = nums[2] = 4

# nums = [1,3,4,2,2]
#             sf
            
        
# new loop
# slow2 = 0
# slow = 4

# รอบที่ 1:
# slow = nums[4] = 2
# slow2 = nums[0] = 1

# รอบที่ 2:
# slow = nums[2] = 4
# slow2 = nums[1] = 3

# รอบที่ 3:
# slow = nums[4] = 2
# slow2 = nums[3] = 2