# subarray
# # a contineus part of array
# nums = [1,2,3,4]
# subarrays = [[1][2][3][4][1,2][2,3][3,4][1,2,3][2,3,4][1,2,3,4]]

current_sum = 0
nums = [1,2,-5,3,4]
for num in nums:
    current_sum+=num
print(current_sum)


# 1. Set current_sum = nums[0]

# 2. Set maximum_sum = nums[0]

# 3. For every number from index 1 to the end of the array:

#     a. Set current_sum to the larger of:
#        - current_sum + current_number
#        - current_number

#     b. If current_sum > maximum_sum:
#            maximum_sum = current_sum

# 4. Return maximum_sum