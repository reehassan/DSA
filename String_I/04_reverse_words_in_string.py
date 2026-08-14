class Solution(object):

  def reverseWords(self, s):
    """:type s: str

    :rtype: str
    """
    # Split automatically handles multiple spaces and trims edges
    words = s.split()

    # Reverse the list of words in-place
    words.reverse()

    # Join the words with a single space
    return " ".join(words)
