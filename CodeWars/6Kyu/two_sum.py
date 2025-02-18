def two_sum(numbers, target):
    dict = {}
    n = len(numbers)

    for i in range(n):
        diff = target - numbers[i] 
        if diff in dict:
            return (dict[diff], i)
        dict[numbers[i]] = i
    return []