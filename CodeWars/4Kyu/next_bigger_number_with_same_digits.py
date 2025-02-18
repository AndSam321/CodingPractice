def next_bigger(n):
    digits = list(str(n))
    length = len(digits)

    i = length - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    # Check Hehre
    if i < 0:
        return -1
    
    # Find the smallest digit on the right side of digits[i]
    # that is greater than digits[i]
    j = length - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    # Swap 
    digits[i], digits[j] = digits[j], digits[i]

    left = digits[:i + 1]
    right = digits[i + 1:]
    right.reverse()
   
    result = int(''.join(left + right))
    
    return result