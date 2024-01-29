def count_jewels_in_stones(jewels, stones):
    count=0
    for s in stones:
        for j in jewels:
            if s==j:
                count+=1
            
    return count

# Example usage:
jewels = "aA"
stones = "aAAbbbb"
result = count_jewels_in_stones(jewels, stones)
print(result)
