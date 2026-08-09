# 169. Majority Element
# input = nums array of size n
# action= find majority element, majority elements are which appear more then (n/2) times
# outputs = 
# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        n = len(nums)

        for element in nums:
            if element in count:
                count[element] += 1
            else:
                count[element] = 1

        for key, value in count.items():
            if value > n // 2:
                return key
            
sol1 = Solution()
print(sol1.majorityElement([3,2,3]))

# Time Complexity = O(n)
# Space Complexity = O(n)
# # but we want O(1)
# 1. Set candidate = None

# 2. Set count = 0

# 3. For every number in nums:

#        If count == 0:

#             candidate = number

#        If number == candidate:

#             count = count + 1

#        Else:

#             count = count - 1


# 4. Return candidate
