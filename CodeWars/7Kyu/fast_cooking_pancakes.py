'''Solved by ChatGPT for LLM HW 12'''

def cook_pancakes(n, m):
    if n <= m:
        return 2  # Each pancake still needs 2 minutes regardless of pan size
    else:
        total_sides = n * 2  # Total number of sides to cook
        batches = -(-total_sides // m)  # Ceiling division for batches
        return batches