from collections import Counter

nums = [2, 3, 4, 3, 2, 2, 4, 4]
counts = Counter(nums)

k = 2

top_k_tuples = counts.most_common(k)

top_k_elements = [item[0] for item in top_k_tuples]

print(top_k_elements) 