def calculate_fibonacci_pair(n):
    # Base case
    if n == 0:
        return (0, 1)
    elif n == 1:
        return (1, 1) 
    
    # Recursive case
    fib_n_half, fib_n_half_plus_one = calculate_fibonacci_pair(n // 2)

    current_fib = fib_n_half * (2 * fib_n_half_plus_one - fib_n_half)
    next_fib = fib_n_half_plus_one * fib_n_half_plus_one + fib_n_half * fib_n_half
    
    if n % 2 == 0:
        return (current_fib, next_fib)
    else:
        return (next_fib, current_fib + next_fib)

def fib(n):
    if n >= 0:
        return calculate_fibonacci_pair(n)[0]
    else:
        absolute_fib = calculate_fibonacci_pair(-n)[0]
        return -absolute_fib if n % 2 == 0 else absolute_fib