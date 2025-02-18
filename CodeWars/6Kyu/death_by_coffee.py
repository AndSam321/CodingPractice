'''Solved by Claude LLM for HW 12'''
def coffee_limits(year, month, day):
    def has_dead(n):
        # Convert to hexadecimal (uppercase) and check for "DEAD"
        return "DEAD" in hex(n)[2:].upper()
    
    def check_limit(increment):
        health = h  # Start with initial health
        for cups in range(1, 5001):
            health += increment  # Add coffee effect
            if has_dead(health):
                return cups
        return 0  # No effect after 5000 cups
    
    # Initial health number in YYYYMMDD format
    h = int(f"{year:04d}{month:02d}{day:02d}")
    
    # Check both coffee types independently
    cafe_limit = check_limit(0xCAFE)    # Use hex value for regular coffee
    decaf_limit = check_limit(0xDECAF)  # Use hex value for decaf
    
    return [cafe_limit, decaf_limit]

# Test cases
test_cases = [
    ((1950, 1, 19), [2645, 1162]),  # John
    ((1965, 12, 11), [111, 0]),     # Susan
    ((1964, 11, 28), [0, 11]),      # Elizabeth
    ((1965, 9, 4), [0, 0])          # Peter
]

for (year, month, day), expected in test_cases:
    result = coffee_limits(year, month, day)
    name = {
        (1950, 1, 19): "John",
        (1965, 12, 11): "Susan",
        (1964, 11, 28): "Elizabeth",
        (1965, 9, 4): "Peter"
    }.get((year, month, day))
    print(f"{name}: Expected {expected}, Got {result}")