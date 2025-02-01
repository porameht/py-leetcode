from typing import List

# 283. Move Zeroes
# Hint
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:

# Input: nums = [0]
# Output: [0]


# Constraints:

#     1 <= nums.length <= 104
#     -231 <= nums[i] <= 231 - 1

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    non_zero_index,i = 0,0
    
    # Iterate through the array and move all non-zero elements to the front
    # i will be incremented every loop
    # non_zero_index will be incremented only when a non-zero element is found
    while i < len(nums):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index+=1
        i+=1

# Example Walkthrough (nums = [0,1,0,3,12]):
# 1. i=0: 0 → no swap
# 2. i=1: 1 → swap with index 0 → [1,0,0,3,12], non_zero_index=1
# 3. i=2: 0 → no swap
# 4. i=3: 3 → swap with index 1 → [1,3,0,0,12], non_zero_index=2
# 5. i=4: 12 → swap with index 2 → [1,3,12,0,0], non_zero_index=3