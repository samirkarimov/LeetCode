def destCity(paths):
    city_chains=[]
    for i in range(len(paths)):
        current=paths[i]
        for j in range(len(paths)):
            if current[1]==paths[j][0]:
                city_chains.append(current)
    for path in paths:
        if path not in city_chains:
            return path[1]
    return False
                


# Example usage:
paths = paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
result = destCity(paths)
print(result)
