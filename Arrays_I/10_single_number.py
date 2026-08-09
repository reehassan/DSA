class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        for num in nums:
            result^=num

        return result

sol1 = Solution()
print(sol1.singleNumber([3,2,3,2,4,5,4]))