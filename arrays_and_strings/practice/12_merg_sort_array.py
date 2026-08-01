# 88. Merge Sorted Array

# aarays = lists in python
# in this problem we are going to use indexing heavily
# nums = [10,20,30,40,50]
# index= [0 ,1 , 2, 3, 4]

# print(nums[0])
# print(nums[-1])
# print(nums[:3])

# pointer = variable storing the index 
# i = 1 # nums list 20
# i += 1 # nums list 30

# 1. Set i = m - 1
#    (pointer to the last real element in nums1)

# 2. Set j = n - 1
#    (pointer to the last element in nums2)

# 3. Set k = m + n - 1
#    (pointer to the last empty position in nums1)

# 4. While i >= 0 AND j >= 0:

#        If nums1[i] >= nums2[j]:

#             nums1[k] = nums1[i]

#             i = i - 1

#        Else:

#             nums1[k] = nums2[j]

#             j = j - 1

#        k = k - 1


# 5. While j >= 0:

#        nums1[k] = nums2[j]

#        j = j - 1
#        k = k - 1