# arrays and indices
nums = [2,7,11,15]
indx = [0,1, 2, 3]

# for num in nums:
#     print(num)

for index, num in enumerate(nums):
    print(index,num)

seen = {
    2:0,
    7:1,
    4:2
}

print(4 in seen)

# 1. Create empty dictionary:
#        seen = {}

# 2. For each index, number in nums:

#        complement = target - number

#        If complement exists in seen:

#             return [seen[complement], index]

#        Else:

#             Store number and index in seen

# 3. Return answers