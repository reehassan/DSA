class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        result = 0

        for num in nums:
            result ^= num

        for num in range(0, n + 1):
            result ^= num

        return result