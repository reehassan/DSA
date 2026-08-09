class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        currentMax = nums[0]
        currentMin = nums[0]
        globalMax = nums[0]

        for element in nums[1:]:

            tempMax = currentMax

            currentMax = max(
                element,
                currentMax * element,
                currentMin * element
            )

            currentMin = min(
                element,
                tempMax * element,
                currentMin * element
            )

            globalMax = max(globalMax, currentMax)

        return globalMax