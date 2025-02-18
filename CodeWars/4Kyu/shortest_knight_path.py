from collections import deque

def knight(p1, p2):
    start = convert_to_coordinate(p1)
    end = convert_to_coordinate(p2)
    
    if start == end:
        return 0  # Already at the destination
    
    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    # BFS and Visited 
    queue = deque([(start[0], start[1], 0)])
    visited = {(start[0], start[1])} 
    
    while queue:
        row, col, steps = queue.popleft()  
        if (row, col) == end:
            return steps
        
        # Move through each move to check
        for move in knight_moves:
            next_row, next_col = row + move[0], col + move[1]
            
            # This is to check if move is out of bounds and if it's not visited
            if 0 <= next_row <= 7 and 0 <= next_col <= 7:
                if (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
    return -1

def convert_to_coordinate(piece):
    col_map = {
        "a": 0, "b": 1, "c": 2, "d": 3,
        "e": 4, "f": 5, "g": 6, "h": 7
    }
    column = piece[0]
    row = piece[1]

    col_index = col_map[column]
    row_index = int(row) - 1

    return (row_index, col_index)