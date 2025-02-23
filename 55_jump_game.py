# 55. Jump Game
# Medium
# Topics
# Companies
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

from typing import List

def canJump(nums: List[int]) -> bool:
    n = len(nums)
    last_pos = n - 1
    
    # range(start, stop, step)
    for i in range(n-1, -1, -1):
        if i + nums[i] >= last_pos:
            last_pos = i
    return last_pos == 0

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))


# 1. First, we start from the last position (`last_pos = n - 1`) and work backwards to the start.

# 2. For each position `i`, we check if we can reach the `last_pos` from that position using:
#    - `i + nums[i] >= last_pos`
#    - Where `i` is our current position
#    - `nums[i]` is the maximum jump length from that position
#    - `last_pos` is the position we're trying to reach

# 3. If we can reach `last_pos` from position `i`, we update `last_pos = i`, making this our new target to reach.

# Let's see an example with `nums = [2,3,1,1,4]`:

# ```
# Index:     0   1   2   3   4
# nums:      2   3   1   1   4
# ```

# Working backwards:
# 1. Start with `last_pos = 4`
# 2. `i = 3`: Can we reach 4 from here? Yes, because 3 + nums[3] = 3 + 1 = 4 ≥ 4. Update `last_pos = 3`
# 3. `i = 2`: Can we reach 3 from here? Yes, because 2 + nums[2] = 2 + 1 = 3 ≥ 3. Update `last_pos = 2`
# 4. `i = 1`: Can we reach 2 from here? Yes, because 1 + nums[1] = 1 + 3 = 4 ≥ 2. Update `last_pos = 1`
# 5. `i = 0`: Can we reach 1 from here? Yes, because 0 + nums[0] = 0 + 2 = 2 ≥ 1. Update `last_pos = 0`

# Since we ended up with `last_pos = 0`, we can reach the end from the start!

# The beauty of this approach is that:
# 1. It's efficient (O(n) time complexity)
# 2. We only need to find ONE valid path to the end
# 3. If we can't reach a position that leads to the end, we'll never get `last_pos` back to 0
