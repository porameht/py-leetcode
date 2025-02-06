# 229. Majority Element II

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.


# Example 1:

# Input: nums = [3,2,3]
# Output: [3]

# Example 2:

# Input: nums = [1]
# Output: [1]

# Example 3:

# Input: nums = [1,2]
# Output: [1,2]

# Constraints:

#     1 <= nums.length <= 5 * 104
#     -109 <= nums[i] <= 109

# Follow up: Could you solve the problem in linear time and in O(1) space?

def majorityElement(nums):
    candidate1 = None
    candidate2 = None
    count1 = 0
    count2 = 0
    
    # Boyer-Moore Voting Algorithm
    # First pass: Find potential candidates
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    
    print(candidate1, candidate2, 'candidate1, candidate2', 'first pass')
    print(count1, count2, 'count1, count2', 'first pass')
    # Second pass: Verify candidates
    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
            
    print(count1, count2, 'count1, count2', 'second pass')
        
    result = []
    
    if count1 > len(nums) // 3:
        result.append(candidate1)
    print(result, 'result', 'count1 > len(nums) // 3')
    if count2 > len(nums) // 3:
        result.append(candidate2)
    print(result, 'result', 'count2 > len(nums) // 3')
    
    return result

print(majorityElement([3,2,3]))
print(majorityElement([1]))
print(majorityElement([1,2]))
print(majorityElement([1,1,2,2,3,3,4,4,4,4]))