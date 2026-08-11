# 347. Top K Frequent Elements
"""
Step 1: Understand the Problem

- Identify input                  integer array nums and an integer k
- Identify required action        return the k most frequent elements
- Identify output                 nums = [1,1,1,2,2,3], k = 2  then 1 = 3, 2 = 2, 3 = 1, most frequent k nums are {1,2}
- Read constraints
 return the answer in any order
 1 <= nums.length <= 105
 lentgh of nums should be greater then or equal to 1 AND less then or equal to 100000
 -104 <= nums[i] <= 104
 k is in the range [1, the number of unique elements in the array]
 It is guaranteed that the answer is unique.
 time complexity must be better than O(n log n), where n is the array's size
"""
from collections import Counter

nums = [2, 3, 4, 3, 2, 2, 4, 4]
counts = Counter(nums)

k = 2

top_k_tuples = counts.most_common(k)

top_k_elements = [item[0] for item in top_k_tuples]

print(top_k_elements) 
