string1 = 'banana'
# frequency table
dict1 = {
    'a':3,
    'b':1,
    'n':2,
}
s = 'strawberry'

for char in s:
    print(char)
count = {}
count = {
    'a':1,
    'b':1,
    'e':1,
    'r':2,
    's':1,
    't':1,
    'w':1,
    'y':1,
}
print(count['r'])
# count['r'] += 3
# # print(count['r'])
# # print('l' in count)


# 1. If length of s is not equal to length of t:
#        Return False

# 2. Create an empty dictionary s_count to store character frequencies of s

# 3. Create an empty dictionary t_count to store character frequencies of t

# 4. For every character in s:
       
#        If character exists in s_count:
#             Increase its count by 1
       
#        Else:
#             Add character to s_count with count 1


# 5. For every character in t:
       
#        If character exists in t_count:
#             Increase its count by 1
       
#        Else:
#             Add character to t_count with count 1


# 6. Compare s_count and t_count

# 7. If both dictionaries are equal:
#        Return True
#    Otherwise:
#        Return False