# 125. Valid Palindrome

"""
Phase 1 — Understand
1. Understand the Problem

What is the input?                           A phrase string s
What exact action/operation is required?     Prove if its palindrome by converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward
What is the exact output?                    Return true if it is a palindrome, or false otherwise.

2. Analyze Constraints
What's the input size?                       
       1 <= s.length <= 2 * 105 | need O(n log n) or O(n)
       s consists only of printable ASCII characters
       Alphanumeric characters include letters and numbers


Phase 2 — Brute Force
3. Find the Brute Force Solution
Input: s = "A man, a plan, a canal: Panama"
- convert all uppercase to lowercase by removing alphanumeric chars
- remove spaces
s = s.lowercase()
for char in s:
    if char == " ":
        remove space

for char in s:
    if char == alphanumeric:
        remove alphanumeric char
"""
import re
s = "A man, a plan, a canal: Panama"
s = s.lower()
s = re.sub(r'\W', '', s).lower() 
print(s)
print(s == s[::-1])

"""
Analyze Brute Force Complexity 
Time Complexity = O(n)
Space Complexity = O(n)

7. Identify the Bottleneck
creating string copies
"""

print(s[0])
print(s[10])