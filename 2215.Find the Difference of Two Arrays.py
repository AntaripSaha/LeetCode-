nums1 = [1,2,3]
nums2 = [2,4,6]
a = set(nums1)
b = set(nums2)
print([list(a - b), list(b - a)])
