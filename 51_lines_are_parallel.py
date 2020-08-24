def lines_are_parallel(l1, l2):
    if l1 == l2:
        return True
    if l1[0]/l2[0] == l1[1]/l2[1]:
        return True
    else: return False

lines_are_parallel([2, 4, 1], [4, 2, 1])