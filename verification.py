from constants import WHITE, BLACK

# given a user path, return True if the path fits all conditions
def verify_solution(path, board):
    # if the path is empty or it does not end at the starting point
    if len(path) == 0 or path[0] != path[-1]:
        return False

    visited_pearls_counter = 0

    # user solution is now guaranteed to be a simple cycle
    # the solution has at least 4 moves
    # go through every move in the cycle
    path = path[:-1]
    print(path)
    for move in path:  
        # if the user's current location has a pearl
        if move in board.pearl_locations:  
            visited_pearls_counter += 1
    
            if board.board[move[0]][move[1]].color == BLACK:  # if the pearl is black
                if black_conditions(move, path) is False:
                    return False
            else:  # the pearl is white
                if white_conditions(move, path) is False:
                    return False

    # check that every pearl has been visited
    if visited_pearls_counter == len(board.pearl_locations):
        return True
    else:
        return False


# check if path turns at black pearl and goes straight before and after
def black_conditions(move, path):
    index = path.index(move)  # O(n)
    if turn_at_black(move, path, index):
        if straight_before_after(move, path, index):
            return True
    return False


# check if path turns 90 degrees on a black pearl
def turn_at_black(move, path, index):
    # approached pearl from left/right. Must go top/down next
    if path[index - 1][0] == path[index][0]:
        print("turned at black")
        return abs(path[index + 1][0] - path[index][0]) == 1

    # approached pearl from top/bottom. Must go left/right next
    if path[index - 1][1] == path[index][1]:
        print("turned at black")
        return abs(path[index + 1][1] - path[index][1]) == 1

    return False


# check if path is straight before and after reaching black pearl
def straight_before_after(move, path, index):
    return True


# check if path goes straight through white pearl and turns before or after
def white_conditions(move, path):
    print("white")
    return True