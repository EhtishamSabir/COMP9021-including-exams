import sys


def betrothed_pair(n):
    '''
    A pair of natural numbers (m, n) is a Betrothed pair if:
    - the sum of the proper divisors of n is one more than m;
    - the sum of the proper divisors of m is one more than n.
    For instance, (48, 75) is a Betrothed pair since
    - the proper divisors of 48 are 1, 2, 3, 4, 6, 8, 12, 16 and 24
    - the proper divisors of 75 are 1, 3, 5, 15 and 25
    - 1 + 2 + 3 + 4 + 6 + 8 + 12 + 16 + 24 = 76
    - 1 + 3 + 5 + 15 + 25 = 49

    You can assume that n is an integer at least equal to 0.
    Will not be tested for n greater than 10_000.

    >>> betrothed_pair(0)
    The least number >= 0 that is the first member of a Betrothed pair is 48
    The Betrothed itself is (48, 75)
    >>> betrothed_pair(50)
    The least number >= 50 that is the first member of a Betrothed pair is 75
    The Betrothed itself is (75, 48)
    >>> betrothed_pair(100)
    The least number >= 100 that is the first member of a Betrothed pair is 140
    The Betrothed itself is (140, 195)
    '''

    def sum_of_divisors(div_sum):
        d_num = div_sum
        lst = []

        for i in range(1, d_num):
            if not d_num % i:
                lst.append(i)

        return sum(lst)

    if n < 0:
        sys.exit()
    num = n

    while True:
        x = sum_of_divisors(num)
        y = sum_of_divisors(x - 1)

        if num + 1 is y:
            print(f'The least number >= {n} that is the first member of a Betrothed pair is {num}')
            print(f'The Betrothed itself is ({num}, {x - 1})')
            break
        else:
            num += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
