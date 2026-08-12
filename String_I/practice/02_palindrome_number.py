# 9. Palindrome Number

# Phase 1 — Understand
"""

1. Understand the Problem

What is the input?                           integer x
What exact action/operation is required?     eturn true if x is a palindrome (an integer is a palindrme when it reads same forward and backward)
What is the exact output?                    true if x is a palindrme false if its not
eg:
x = 1221
palindrome = 1221
True

x = -292
palindrome = 291-
False

2. Analyze Constraints

What's the input size (n ≤ 10? ≤ 10³? ≤ 10⁵? ≤ 10⁹?) 2 * 10 power 9
needs
n ≤ ~10⁹ → need O(log n) or O(1)
a negative number never be a palindrome cause the minus sign breaks the symmatry
"""

# Phase 2 — Brute Force
"""

3. Find the Brute Force Solution

checking if a number after reversing stays the same
return true if yes otherwise false


4. Write Brute Force Pseudocode

x = 1221
reverse_x = x.reverse()
if x == reverse_x:
    return true
else:
    false

5. Implement Brute Force Code

6. Analyze Brute Force Complexity

Time = O(1)
Space = O(1)
"""
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    
    reversed_x = int(str(x)[::-1])
    
    return x == reversed_x

"""
Phase 3 — Optimize

7. Identify the Bottleneck
we cannt convert the integr t string to reverse it
"""