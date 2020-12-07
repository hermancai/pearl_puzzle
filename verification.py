# given a user path, return True if the path fits all conditions
def verify_solution(path, board):
    if len(path) == 0 or path[0] != path[-1]:
        return False

    return True