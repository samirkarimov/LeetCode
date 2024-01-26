def count_pairs(nums, target):
    nums.sort()
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]<target:
                count+=1
    return count

            

        
            


# Example usage:
nums = [1, 3, 2, 4, 5]
target = 6
result = count_pairs(nums, target)
print(result)
