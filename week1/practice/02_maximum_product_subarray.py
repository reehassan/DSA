"""
1. Understand the Problem

- What is the input?                        integer array nums
- What operation/action is required?        find a that has the largest product
- What is the exact output?                 return the product

2. Analyze Constraints

- Identify allowed complexity               Time = O(n), Space = O(1)

3. Find a Basic Solution

- Think of the simplest correct approach first
SOLUTION:
nums = [2,3,-2,4]
creating subarrays and finding products
[2] = 2
[3] = 3
[-2]= -2
[4] = 4

[2,3] = 6
[3,-2] = -6
[-2,4] = -8


[2,3,-2] = -12
[3,-2,4] = -24

[2,3,-2,4] = -48

Largest subarray product = [2,3] = 6

- Identify its time and space complexity | time = O(n3), space = O(1)


4. Identify the Bottleneck
- What operation is making it slow?                         recalculating the whole array again and again
- Is there repeated searching, comparison, or calculation?  repeated calculatin 
- What work is being repeated unnecessarily?                we can keep the previous computed product multiply it by next

5. Find Opportunities for Optimization

- Can I **store information** instead of recalculating it?                           yes we can store current subarray prduct in variable called product
- What information would make this problem easier if I remembered it?                the product of current subarray
- Can previous results help future calculations?                                     yes. Instead of multiplying the entire subarray again, multiply the previous product by the new element. 
- Can I process the data in a different direction (left-to-right / right-to-left)?   no. The bottleneck is repeated multiplication, not traversal direction.
- Can I maintain a running value instead of recomputing?                             yes. Maintain a running product while extending the subarray.


6. Recognize the Pattern
Pattern:
✓ Dynamic Programming (State Compression)
Reason:
At each index, the answer depends on previously computed maximum and minimum products, so we reuse previous state instead of recomputing.

7. Write Pseudocode
1. If nums has only one element:

       Return that element


2. Initialize:

       currentMax = nums[0]
       currentMin = nums[0]
       globalMax  = nums[0]


3. Traverse the array from index 1 to the end:

       Save currentMax in a temporary variable

       currentMax =
           maximum of:
               current number
               currentMax × current number
               currentMin × current number

       currentMin =
           minimum of:
               current number
               temporaryMax × current number
               currentMin × current number

       globalMax =
           maximum(globalMax, currentMax)


4. Return globalMax
"""