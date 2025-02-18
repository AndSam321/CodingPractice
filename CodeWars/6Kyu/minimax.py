'''
First, I began creating a function to run the evaluation of the tree. The list of values hold the spot that we are at in the tree
Then, the for loop goes through each node and checks if it is an instance of a leaf, if it is a leaf, we append it to values
Otherwise, we recurse back up the tree by adding 1. I ran into some issues here because I didn't know how to move the levels in the tree.
Bottom checks to see if we are at the max level, then we just return max values to show the root level, otherwise return
the min values because it's the vice versa.
'''

def minimax(tree):
    # Start the minimax evaluation at the root (level 0).
    return evaluate_minimax(tree, 0)


def evaluate_minimax(tree, level):
    # Hold values of where we are at
    values = []

    # Iterating through each node in the tree
    for node in tree:
        if isinstance(node, int):
            # If the node is a leaf, append it to the list
            values.append(node)
        else:
            # Otherwise, we check the node and go to the next level
            values.append(evaluate_minimax(node, level + 1))

    # At the root, return the max value
    if level == 0:
        best_value = max(values)  # Root level is always maximizing.
        best_move_index = values.index(best_value) + 1  # Moves start at 1, so add 1
        return best_value, best_move_index

    # Maximizing the player move
    if level % 2 == 0:
        return max(values)

    # Minimizing the computer move
    return min(values)


print(minimax([1, 3, 2]))
