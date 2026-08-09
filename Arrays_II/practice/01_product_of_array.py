"""
1. Understand the Problem

- What is the input?                     integer array nums
- What operation/action is required?     return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
- What is the exact output?
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

- Constraints:
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
- Target Complexity
Time: O(n)
Space: O(1) extra space
"""

"""
3. Find a Basic Solution
Example 1
Input: nums = [1,2,3,4]  array of int called nums

i = 0 skipped and 2 * 3 * 4 = 24
i = 1 skipped and 1 * 3 * 4 = 12
i = 2 skipped and 1 * 2 * 4 = 8
i = 3 skipped and 1 * 2 * 3 = 6

Output: nums = [24, 12, 8, 6]

Example 2
Input: nums = [-1,1,0,-3,3] array of int called nums

i = 0 skipped and 1 * 0 * -3 * 3 = 0
i = 1 skipped and-1 * 0 * -3 * 3 = 0
i = 2 skipped and-1 * 1 * -3 * 3 = 9
i = 3 skipped and-1 * 1 *  0 * 3 = 0
i = 4 skipped and-1 * 1 *  0 *-3 = 0

Output: nums = [0,0,9,0,0]

Brute Force:
Time Complexity = O(n²)
Space Complexity = O(1)

but we need O(1)

4. Identify the Bottleneck
we are repeating multiplication

| Index | Left Product | Reason                                      |
| ----: | -----------: | ------------------------------------------- |
|     0 |            1 | Nothing on the left, so use 1               |
|     1 |            1 | Product of numbers before index 1 → `1`     |
|     2 |            2 | Product of numbers before index 2 → `1×2`   |
|     3 |            6 | Product of numbers before index 3 → `1×2×3` |
"""

# 1. Create answer array of same length as nums

# 2. Set left_product = 1

# 3. Traverse nums from left to right:

#        answer[i] = left_product

#        left_product = left_product * nums[i]


# 4. Set right_product = 1

# 5. Traverse nums from right to left:

#        answer[i] = answer[i] * right_product

#        right_product = right_product * nums[i]


# 6. Return answer

# Time: O(n)

# Space: O(1) extra space
