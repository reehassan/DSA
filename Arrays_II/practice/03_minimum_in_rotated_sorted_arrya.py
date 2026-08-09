# 153. Find Minimum in Rotated Sorted Array
# a sorted array means every element is less then next element
nums = [1,2,3,4,5,6,7]

# for i in nums[:]:
#     print(nums[i] < nums[i]+1)
print(nums[0])
print(nums[1])

left = 0
right = len(nums) - 1
print(nums[right])