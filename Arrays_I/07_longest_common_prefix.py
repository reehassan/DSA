class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        first_word = strs[0]

        for i in range(len(first_word)):

            for word in strs[1:]:

                if i >= len(word) or first_word[i] != word[i]:
                    return first_word[:i]

        return first_word