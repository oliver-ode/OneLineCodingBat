def has22(nums):
    return sum([1 if nums[i]==2 and nums[i+1]==2 else 0 for i in range(len(nums)-1)])>=1