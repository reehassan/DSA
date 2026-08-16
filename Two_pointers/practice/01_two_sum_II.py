# 167. Two Sum II - Input Array Is Sorted

"""
what is input ?          1-indexed array of integers numbers, that is already sorted in non-decreasing order
what action ?            find two numbers such that they add up to a specific target number
what output?             Input: numbers = [2,7,11,15], target = 9 then Output: [1,2]

constraints:
    2 <= numbers.length <= 3 * 104
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.

TARGETED:
Time Complexity = O(n)
Space Complexity = O(1)

"""
# BRUTE FORCE

def twoSum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

twoSum([3,4,2,2],4)
# Time Complexity = O(n^2)
# Space Complexity = O(1)
# but the optimal solution is O(n) by using two pointers approach
