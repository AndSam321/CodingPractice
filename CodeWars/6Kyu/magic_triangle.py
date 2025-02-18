'''
Used itertools to check each position and possible permutation. If it isn't filled, fill it with the current permutation
'''

from itertools import permutations

def valid_perm(perm):
    # Checks if it could be a valid answer
    line1_sum = perm[0] + perm[1] + perm[2] + perm[3]  # First line (0, 1, 2, 3)
    line2_sum = perm[3] + perm[4] + perm[5] + perm[6]  # Second line (3, 4, 5, 6)
    line3_sum = perm[6] + perm[7] + perm[8] + perm[0]  # Third line (6, 7, 8, 0)
    
    return line1_sum == line2_sum == line3_sum

def magic_triangle_solutions(puzzle):
    solution = []
    # Find the unused numbers (those not in the puzzle)
    unused_numbers = {i for i in range(1, 10) if i not in puzzle}
    all_permutations = permutations(unused_numbers)

    for perm in all_permutations:
        perm_index = 0  # Current position in the permutation
        current_puzzle = []

        # Fill the puzzle with numbers from the current permutation
        for num in puzzle:
            if num != 0:
                current_puzzle.append(num)
            else:
                current_puzzle.append(perm[perm_index])
                perm_index += 1  # Move to the next number in the permutation

        # Check if it is valid
        if valid_perm(current_puzzle):
            solution.append(current_puzzle)

    return solution