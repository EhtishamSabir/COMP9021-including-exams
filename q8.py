def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.

    Conjunctions of inputs will be tested, so hard coding will not help.

    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''

    numbers = []

    for row in square:
        row_sum = 0
        for elem in row:
            row_sum += elem
        if row_sum in numbers:
            return False
        else:
            numbers.append(row_sum)

    for i in range(len(square)):
        col_sum = 0
        for j in range(len(square)):
            col_sum += square[j][i]

        if col_sum in numbers:
            return False
        else:
            numbers.append(col_sum)

    diagonal_sum_1 = 0
    diagonal_sum_2 = 0

    for i in range(len(square)):
        diagonal_sum_1 += square[i][i]

    if diagonal_sum_1 in numbers:
        return False

    else:
        numbers.append(diagonal_sum_1)

    for i in range(len(square)):
        diagonal_sum_2 += square[i][len(square) - 1 - i]

    if diagonal_sum_2 in numbers:
        return False

    else:
        return True


if __name__ == '__main__':
    import doctest

    doctest.testmod()
