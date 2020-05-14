from typing import List


def create_zigzag(rows: int, cols: int, start: int = 1) -> List[List[int]]:

    if rows == 0:
        return []
    if cols == 0:
        return [[]] * rows

    flat = list(range(start, start + rows * cols))

    data = []
    reverse = False
    while flat:
        data.append(flat[0:cols] if not reverse else flat[cols - 1::-1])
        flat[0:cols] = []
        reverse = not reverse
    return data


if __name__ == '__main__':
    print("Example:")
    print(create_zigzag(3, 3, 5))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert create_zigzag(3, 5) == [
        [1, 2, 3, 4, 5],
        [10, 9, 8, 7, 6],
        [11, 12, 13, 14, 15]
    ]
    assert create_zigzag(5, 1) == [
        [1],
        [2],
        [3],
        [4],
        [5]
    ]
    assert create_zigzag(3, 3, 5) == [
        [5, 6, 7],
        [10, 9, 8],
        [11, 12, 13]
    ]

    # Edge cases
    assert create_zigzag(0, 3) == []
    assert create_zigzag(3, 0) == [[], [], []]
    assert create_zigzag(0, 0) == []

    print("Coding complete? Click 'Check' to earn cool rewards!")
