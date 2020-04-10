temp_tuple=[[1,3],[2,6],[8,10],[12,15]]
temp_tuple.sort(key=lambda interval: interval[0])
merged = [temp_tuple[0]]
for current in temp_tuple:
    previous = merged[-1]
    if current[0] <= previous[1]:
        previous[1] = max(previous[1], current[1])
    else:
        merged.append(current)
print(temp_tuple)        
print(merged)
