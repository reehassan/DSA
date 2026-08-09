"""
383. Ransom Note

1. Understand the Problem

- What is the input?                     strings ransomNote and magazine
- What operation/action is required?     return true if ransomNote can be constructed by using the letters from magazine and false otherwise
- What is the exact output?
Input: ransomNote = "aa", magazine = "aab"
True
Input: ransomNote = "ikea", magazine = "eacik"
True
Input: ransomNote = "aa", magazine = "ab"
False
- Constraints:
    Each letter in magazine can only be used once in ransomNote.
    1 <= ransomNote.length, magazine.length <= 105 | lentgh of ransomNote should be greater then or equal to 1, magazine lentgh should be les then or equal to 105
    ransomNote and magazine consist of lowercase English letters.

2. Analyze Constraints

- Identify allowed complexity.
Time Complexity = O(n + m), where n = lentgh of ransomnote, m = lentgh of magazine
Space Complexity = O(1) or O(k)

3. Pattern
Hashmaps
# """

# 1. Create empty dictionary:

#        count = {}

# 2. For every character in magazine:

#        If character exists in count:

#             count[character] += 1

#        Else:

#             count[character] = 1


# 3. For every character in ransomNote:

#        If character does not exist in count
#        OR count[character] == 0:

#             return False

#        Else:

#             count[character] -= 1


# 4. Return True