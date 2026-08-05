class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], index]

            else:
                seen[num] = index