def find_secret_number(low, high, guess_bot):
    left = low
    right = high
    
    # Binary Search
    
    while left <= right:
        mid = left + (right - left) // 2  
        response = guess_bot.guess_number(mid)
        
        if response == 'Smaller':
            right = mid - 1
        elif response == 'Larger':
            left = mid + 1
        elif response == 'Correct':
            return mid
        elif response == 'You failed, you bring great shame to your family name':
            return None  
        elif response == "What are you, deaf?":
            return mid  
            
    return None 