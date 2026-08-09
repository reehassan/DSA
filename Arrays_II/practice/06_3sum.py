"""
Step 1: Understand the Problem

- Identify input              integer array nums
- Identify required action    return all the triplets from array nums 
- Identify output             nums = [-1,0,1,2,-1,-4] output: [-1,0,1][-1,-1,2]
- Read constraints            
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0
one index from array nums can be used once only
only return the triplets which can be returned zero by summing them up
it should not contain duplicate triplets
"""


# BRUTE FORCE
# nums = [-1,0,1,2,-1,-4]
# -1 + 0 + 1 = 0
# 0 + 1 + 2 = 3 
# 1 + 2 - 1 = 2
# 2 - 1 - 4 = -3

# nums = [-4,-1,-1,0,1,2]
# -4 - 1 - 1 = -6
# -1 -1 + 0 = -2
# -1 + 0 + 1 = 0
# 0 + 1 + 2 = 3

# -1 -1 + 2 = 0


# nums = [0,1,1]
# 0 + 1 + 1 = 2
# 1 + 0 + 1 = 2
# nums = [0,0,0]
# 0 + 0 + 0 = 0

# nums = [-1,0,1,2,-1,-4]

# result = []

# for i from 0 to n-1:
#     for j from i+1 to n-1:
#         for k from j+1 to n-1:

#             sum = nums[i] + nums[j] + nums[k]

#             if sum == 0:
#                 add [nums[i], nums[j], nums[k]] to result

# return result

# Time = O(n)3

