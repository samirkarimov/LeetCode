def maxWidthOfVerticalArea(points):
    points.sort()
    distances=[]
    for i in range(len(points)-1):
        distances.append(points[i+1][0]-points[i][0])
    return max(distances)
    


# Example usage:
points = [[8, 7], [9, 9], [6, 4], [9, 7]]
result = maxWidthOfVerticalArea(points)
print(result)
