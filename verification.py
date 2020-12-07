from constants import BLACK

# given a user path, return True if the path fits all conditions
def verify_solution(path, board):
    # if path is empty or path does not end at starting point
    if len(path) == 0 or path[0] != path[-1]:
        return False

    visited_pearls_counter = 0

    # user solution is now guaranteed to be a simple cycle
    path = path[:-1]  # end location is same as start

    # go through every move in the cycle
    for index in range(len(path)):  # O(number of moves)
        # if the user's current location has a pearl
        if path[index] in board.pearl_locations:  # O(number of pearls)
            visited_pearls_counter += 1

            # check conditions of the path based on the pearl color
            # each element in path list is a tuple of two indices
            if board.get_content_at(path[index][0], path[index][1]).color == BLACK:
                if black_conditions(path, index) is False:
                    return False
            else:  # the pearl is white
                if white_conditions(path, index) is False:
                    return False

    # check if every pearl has been visited
    return visited_pearls_counter == len(board.pearl_locations)


# check if path turns at black pearl and goes straight before AND after
def black_conditions(path, index):
    if turned_at_point(path, index):
        if straight_at_point(path, index - 1) and straight_at_point(path, (index + 1) % len(path)):
            return True
    return False


# check if path goes straight through white pearl and turns before OR after
def white_conditions(path, index):
    if straight_at_point(path, index):
        if turned_at_point(path, index - 1) or turned_at_point(path, (index + 1) % len(path)):
            return True    
    return False


# check if the path makes a turn at the given location
def turned_at_point(path, index):
    # approached pearl from left/right. Must go top/down next
    if path[index - 1][0] == path[index][0]:
        return abs(path[(index + 1) % len(path)][0] - path[index][0]) == 1

    # approached pearl from top/bottom. Must go left/right next
    if path[index - 1][1] == path[index][1]:
        return abs(path[(index + 1) % len(path)][1] - path[index][1]) == 1

    return False


# check if the path goes straight through the given location
def straight_at_point(path, index):
    # straight path can be horizontal or vertical
    horizontal_straight = path[index][0] == path[index - 1][0] == path[(index + 1) % len(path)][0]
    vertical_straight = path[index][1] == path[index - 1][1] == path[(index + 1) % len(path)][1]

    return horizontal_straight or vertical_straight
