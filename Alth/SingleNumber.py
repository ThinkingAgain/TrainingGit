def singleNumber(nums):
    nums.sort()
    #print(nums)
    lo = 0
    hi = len(nums)-1
    while(lo < hi):
        #print(nums[lo:hi+1])
        mid = (lo + hi)//2
        #print(mid, nums[mid-1:mid+2])
        if nums[mid] == nums[mid+1]:
            if (hi-mid+1)%2 != 0:
                lo = mid
            else:
                hi = mid-1
        elif nums[mid] == nums[mid -1]:
            if (mid-lo+1)%2 != 0 :
                hi = mid
            else:
                lo = mid+1
        else:
            return nums[mid]
    return nums[lo]

nums = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]
print(singleNumber(nums))