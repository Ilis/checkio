from typing import Tuple
from math import factorial


def permutation_index(numbers: Tuple[int])->int:
    # Weights as factorials and extra 0
    weights = [factorial(i) for i in range(len(numbers) - 1, 0, -1)] + [0]

    # Registers as a count of values far and less than current
    registers = []
    for i, n in enumerate(numbers):
        registers.append(sum(1 for x in numbers[i:] if x < n))

    # Index as a sum of weighted registers
    n = sum(r * w for r, w in zip(registers, weights))
    return n + 1


if __name__ == '__main__':
    assert permutation_index((9,)) == 1
    assert permutation_index((5, 7)) == 1
    assert permutation_index((2, 4, 3, 1)) == 12
    assert permutation_index((7, 5)) == 2
    assert permutation_index((3, 2, 1)) == 6
    assert permutation_index((3, 1, 2)) == 5
    assert permutation_index((5, 3, 0, 9)) == 15
    assert permutation_index((1, 2, 0)) == 4
    assert permutation_index((2, 0, 1)) == 5
    assert permutation_index((2, 1, 3, 0, 4, 5)) == 271
    assert permutation_index((6, 8, 3, 4, 2, 1, 7, 5, 0)) == 279780
    assert permutation_index((0, 4, 7, 5, 8, 2, 10, 6, 3, 1, 9, 11)) == 12843175
    assert permutation_index((9, 0, 6, 2, 5, 7, 12, 10, 3, 8, 11, 4, 13, 1, 14)) == 787051783737
    assert permutation_index((9, 0, 6, 17, 8, 12, 11, 1, 10, 14, 3, 15, 2, 13, 16, 7, 5, 4)) == 3208987196401056
    assert permutation_index((15, 13, 14, 6, 10, 5, 19, 16, 11, 0, 9, 18, 2, 17, 4, 20, 12, 1, 3, 7, 8)) == 38160477453633042937
    assert permutation_index((9, 5, 4, 12, 13, 17, 7, 0, 23, 16, 11, 8, 15, 21, 2, 3, 22, 1, 10, 19, 6, 20, 14, 18)) == 238515587608877815254677
    assert permutation_index((16, 17, 10, 23, 4, 22, 7, 18, 2, 21, 13, 6, 9, 8, 19, 3, 25, 12, 26, 24, 14, 1, 0, 20, 15, 5, 11)) == 6707569694907742966546817183
    print('The local tests are done. Click on "Check" for more real tests.')
