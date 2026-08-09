class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

sol1 = Solution()
print(sol1.containsDuplicate([3,5,2,1,4]))
print(sol1.containsDuplicate([3,5,2,1,1,4]))
print(sol1.containsDuplicate([0]))