def bubble(lst):
    snapshots = []
    sorted_list = sorted(lst)
    
    if lst == sorted_list:
        return []
    
    for n in range(len(lst) - 1, 0, -1):
        swapped = False
        
        for i in range(n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                snapshots.append(lst[:])
                swapped = True
        
        if not swapped:
            break
            
    return snapshots