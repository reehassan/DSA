# arrays = lists in python
# eg
# arr = [3,4,35]

# a list store elements inorder and each char has index

s = ['a', 'b', 'c', 'd','$']
#i =  0    1    2    3   4
# print(s[1])

# s[-1] = 'e'

# # swapping elements to reverse array(list) of string
# s[0], s[4] = s[4], s[0]
# s[1], s[3] = s[3], s[1]

# # a pointer is just an variable storing an index
# left = 0
# right = len(s)-1
# # print(right)
# copy = s.copy()
# print(reversed(copy))

# s = ["h","i"]

# print(s[0]) # h is printed

# s = ["h","e","l","l","o"]
# s[0],s[4] = s[4],s[0] swapping method
# s[1],s[3] = s[3],s[1]
# new = s[::-1] slicing method
# print(new)

left = 3 # when move become 4
right = 8 # when move become 7

# s = ["a","b","c","d","e"] e and a swapped first
# left >= right used in odd array case
# left > right used in even array case
# s[2] = "Z" yes its in place as we are not creating another string just replacing with char Z at index 2
# new = s[::-1] no its not in place as its another new array and s is been sliced here

# time complexity = as input gets bigger, how does the no of operations grow in our code to write it effiectly
# s = ["h","e","l","l","o"] for this problem only 2 swaps are needed
#  for 10 char only 5 swaps are needed, for 100 50 swaps, for 1000 only 500 swaps are needed so
# number of swaps = n / 2, in notaion O(n/2) but we ignore constant factors like 1/2
# so O(n/2) = O(n) time complexity

# space complexity = how much extra memory does my algorithm use
# Space Complexity = O(1)

# pseudocode
# 1. Set left = 0

# 2. Set right = len(s) - 1

# 3. While left < right:

#     a. Swap s[left] and s[right]

#     b. Increment left by 1

#     c. Decrement right by 1

# 4. End