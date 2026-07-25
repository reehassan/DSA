class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums = [0,1,0,3,12]
        write = 0
        for read in nums:
            if read != 0:
                nums[read] = nums[write]
                write+=write