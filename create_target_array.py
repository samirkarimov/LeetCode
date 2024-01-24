def createTargetArray(nums, index):
    target=[]
    for i in range(len(nums)):
        target=target[:index[i]]+[nums[i]]+target[index[i]:]
    return target
       


# Example usage:
nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]




result = createTargetArray(nums, index)
print(result)
