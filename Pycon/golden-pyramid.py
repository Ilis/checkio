def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    # Shadow pyramid base
    shadow = [list(pyramid[-1])]

    # Build rest of the pyramid cumulative
    for lvl in pyramid[-2::-1]:
        # Build level
        shadow_lvl = [v + max(shadow[0][i], shadow[0][i + 1])
                      for i, v in enumerate(lvl)]
        # Put level on top of the pyramid
        shadow.insert(0, shadow_lvl)

    # Answer is the top value of shadow pyramid
    return shadow[0][0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
