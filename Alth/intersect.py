"""
nums1 = [4,9,5]

nums2 = [9,4,9,8,4]
c = []
for i in set(nums1) & set(nums2):
    #x = nums1.count(i) if nums1.count(i) <= nums2.count(i) else nums2.count(i)
    c.extend([i]*(nums1.count(i) if nums1.count(i) <= nums2.count(i) else nums2.count(i)))
print(c)
"""

nums = [0,0,1]
for i in range(len(nums)):
    if nums[i] == 0:
        nums.append(nums.pop(i))
print(nums)