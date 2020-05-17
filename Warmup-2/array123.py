def array123(nums):
    return sum([1 if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3 else 0 for i in range(len(nums)-2)])>=1