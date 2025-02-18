'''
We can check if it's a winning or losing position by XORing all the pile sizes together. 

https://math.stackexchange.com/questions/1870129/why-is-nim-solvable-with-the-xor-operator

I utilized this source for help with solving the problem and coming up with a solution. By checking/XOR each move,
we can see if the nim_sum is 0, which is losing position -> done by the desired pile size subtracted by the current pile XOR by the nim_sum.
'''
def choose_move(board):
    nim_sum = 0
    for pile_size in board:
        nim_sum ^= pile_size
 # Check to see if we have a winning move
    for pile_index, current_pile_size in enumerate(board):
        desired_pile_size = current_pile_size ^ nim_sum # Checking which pile to go
        if desired_pile_size < current_pile_size: 
            straws_to_remove = current_pile_size - desired_pile_size # Making the straws to remove however we need to take out
            
            return [pile_index, straws_to_remove]