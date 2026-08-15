# 20. Valid Parentheses

# Phase 1 — Understand
"""

1. Understand the Problem

What is the input?                                        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
What exact action/operation is required?
Determine if the input string is valid:
An input string is valid if |

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

What is the exact output?
Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false



2. Analyze Constraints
1 <= s.length <= 104                          NEED O(n²) OR O(n log n) OR O(n)
s consists of parentheses only '()[]{}'.
"""


# Phase 2 — Brute Force
"""

3. Find the Brute Force Solution

4. Write Brute Force Pseudocode

5. Implement Brute Force Code

6. Analyze Brute Force Complexity
"""

def isValid(s: str) -> bool:
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")
    
    return s == ""

print(isValid("([])"))  
print(isValid("([)]")) 