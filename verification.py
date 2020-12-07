# given a user path, return True if the path fits all conditions
def verify_solution(path, board):
    # if the path is empty or it does not end at the starting point
    if len(path) == 0 or path[0] != path[-1]:
        return False

    visited_pearls_counter = 0

    # user solution is now guaranteed to be a simple cycle
    # go through every move in the cycle
    for move in path[:-1]:
        # if the user's current location has a pearl
        if move in board.pearl_locations:
            visited_pearls_counter += 1

    if visited_pearls_counter == len(board.pearl_locations):
        return True
    
    return False