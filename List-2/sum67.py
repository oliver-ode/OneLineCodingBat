def sum67(nums):
    return (lambda skip: sum(skip.append(True) or 0 if num==6 else skip.append(False) or 0 if num==7 and skip[-1] else 0 if skip[-1] else num for num in nums))([False])