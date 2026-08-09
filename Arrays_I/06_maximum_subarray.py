class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = nums[0]
        maximum_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)

            if current_sum > maximum_sum:
                maximum_sum = current_sum

        return maximum_sum


solution1 = Solution()
print(solution1.maxSubArray([1,2,-3,-9,10,20,-12]))
