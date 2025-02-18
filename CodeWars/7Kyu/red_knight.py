'''Solved by ChatGPT for LLM HW 12
'''
def red_knight(N, P):
    knight_pos = 0
    knight_vertical = N  # 0 for White, 1 for Black
    pawn_pos = P
    
    while True:
        # If the knight catches a pawn at this position
        if knight_pos == pawn_pos:
            pawn = "White" if knight_vertical == 0 else "Black"
            return (pawn, knight_pos)
        
        # Move Red Knight: 2 steps forward, 1 step vertical
        knight_pos += 2
        knight_vertical = 1 - knight_vertical  # Toggle between 0 and 1
        
        # Move pawns: 1 step forward
        pawn_pos += 1