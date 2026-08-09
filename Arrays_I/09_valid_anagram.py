class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_count = {}
        t_count = {}

        for char in s:
            if char in s_count:
                s_count[char] += 1
            else:
                s_count[char] = 1

        for char in t:
            if char in t_count:
                t_count[char] +=1
            else:
                t_count[char] = 1
        if s_count == t_count:
            return True
        else:
            return False

sol1 = Solution()
print(f"Is Anagram: {sol1.isAnagram('ananab','banana')}")