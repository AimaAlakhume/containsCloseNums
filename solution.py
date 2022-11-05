def solution(nums, k):
    
    close = False
    
    if len(nums) <= 1:
        return close
    
    positionDict = {}
    
    for i in range(len(nums)):
        if nums[i] not in positionDict:
            positionDict[nums[i]] = i
        else:
            if abs(i - positionDict[nums[i]]) > k:
                positionDict[nums[i]] = i
            else:
                close = True
    
    return close
