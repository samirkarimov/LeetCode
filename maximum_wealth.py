def maximumWealth(accounts):
    total_moneys=[]
    for c_accounts in accounts:
      total_moneys.append(sum(c_accounts))
    return max(total_moneys)


# Example usage:
accounts = [
    [1, 2, 3],
    [3, 2, 1],
    [4, 5, 6]
]
result = maximumWealth(accounts)
print(result)
