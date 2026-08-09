# # An array called a list in python stores multiple values in order
# nums = [1,2,4,5]
# #index= 0 1 2 3

# print(nums[0])
# print(nums[:])
# print(nums[-1])

# nums[-1] = 89
# print(nums[-1])

# for num in nums:
#     print(num)

# nums2 = [10, 30, 40, 59, 69, 32, 43, 54, 0]
# for i in range(len(nums2)):
#     print(i, nums2[i])

# if nums2[i] == 0:
#     print("zero")
# else:
#     print("non zero")


# nums3 = [3, 4]

# nums3[0], nums3[1] = nums3[1], nums3[0]

# print(nums3)

# nums = [2,3,4,5]
# nums[0] = 10 # no new list created

# print(nums)

# nums = [7, 3, 1]
# print(nums[2]) 1 will be printed

# nums = [5, 4, 3]
# nums[1] = 8 # 4 will be replaced by 8

# nums = [4, 0 , 9]
# for x in nums:
#     print(x)

# nums = [2, 6]

# nums[0], nums[1] = nums[1], nums[0]
# print(nums)

# What is the input? list(array) of integers called nums which can be : all zeros = no change, already zeros at the end = no change, one element = no change, 0 in between integers like nums = [2,3,0,3,5,0,0,5]
# What is the output? nums = [2,3,3,5,5,0,0,0]
# What are the rules? 
# Move every 0 to the end.
# Keep non-zero numbers in the same order.
# Modify the original array (in-place).
# Don't create another list.
# 1. Set write = 0

# 2. For every index read in the array

# 3. If nums[read] is not 0

# 4. Swap nums[read] with nums[write]

# 5. Increment write

# 6. Continue until read reaches the end of the array