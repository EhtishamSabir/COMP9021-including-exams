def pascal_triangle_line(n):
    '''
    Recall: it is the list of binomial coefficients that give the
    number of ways of choosing k objects out of n - 1 for 0 <= k < n.

    >>> pascal_triangle_line(1)
    [1]
    >>> pascal_triangle_line(2)
    [1, 1]
    >>> pascal_triangle_line(3)
    [1, 2, 1]
    >>> pascal_triangle_line(4)
    [1, 3, 3, 1]
    >>> pascal_triangle_line(5)
    [1, 4, 6, 4, 1]
    >>> pascal_triangle_line(6)
    [1, 5, 10, 10, 5, 1]
    >>> pascal_triangle_line(7)
    [1, 6, 15, 20, 15, 6, 1]
    >>> pascal_triangle_line(8)
    [1, 7, 21, 35, 35, 21, 7, 1]
    '''
    row = [1]
    listn = [list(row) * i for i in range(1, n + 1)]
    for i in range(n):
        for j in range(i + 1):
            if i == 0 or j == 0 or j == i:
                listn[i][j] = 1
            else:
                listn[i][j] = int(listn[i - 1][j - 1]) + int(listn[i - 1][j])

    print(listn[n - 1])
    return


if __name__ == '__main__':
    import doctest
    doctest.testmod()
