def final_value_after_operations(operations):
    x=0
    for o in operations:
        if o=="++X" or o=="X++":
            x+=1
        else:
            x-=1
    return x
    


# Example usage:
operations = ["++X", "++X", "X++", "X--"]
result = final_value_after_operations(operations)
print(result)
