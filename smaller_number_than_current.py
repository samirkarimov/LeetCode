def smallerNumbersThanCurrent(nums):
    
    
    result=[]
    for j in range(len(nums)):
        num=nums[j]
        count = 0
        for i in range(len(nums)):
            if nums[i] < num:
                count += 1
        result.append(count)
    return result
    
    


# Example usage:
nums = [8, 1, 2, 2, 3]
output = smallerNumbersThanCurrent(nums)
print(output)
