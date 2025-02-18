'''Solved using ChatGPT for LLM HW 12'''

def find_incorrect_value(tree):
    # Iterate from the last parent node up to the root (in reverse order).
    for parent_index in reversed(range(len(tree) // 2)):
        parent_value = tree[parent_index]  # Current parent node value.
        left_child = tree[2 * parent_index + 1]  # Value of the left child.
        right_child = tree[2 * parent_index + 2]  # Value of the right child.
        
        # Check if the parent value matches the sum of its children.
        if parent_value != left_child + right_child:
            # Special case: If the root node is incorrect.
            if parent_index == 0:
                return (0, left_child + right_child)  # Root should equal sum of its children.
            
            # Find the grandparent's index.
            grandparent_index = (parent_index - 1) // 2
            # Calculate sibling index of the current parent.
            sibling_index = ((parent_index + 1) ^ 1) - 1
            
            # Calculate what the current parent value should be based on its grandparent and sibling.
            expected_parent_value = tree[grandparent_index] - tree[sibling_index]
            
            # If the parent value is incorrect based on grandparent and sibling.
            if parent_value != expected_parent_value:
                return (parent_index, expected_parent_value)  # Correct parent node.
            else:
                # Otherwise, it's the right child that's incorrect.
                return (2 * parent_index + 2, parent_value - left_child)
    
    # Return None if no incorrect value is found (shouldn't happen with valid input).
    return None