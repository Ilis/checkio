from typing import Iterable


def median_three(els: Iterable[int]) -> Iterable[int]:

    # Median of three
    def mot(a, b, c):
        return sorted([a, b, c])[1]

    return [els[i] if i < 2 else mot(els[i - 2], els[i - 1], els[i])
            for i in range(len(els))]


if __name__ == '__main__':
    print("Example:")
    print(list(median_three([1, 2, 3, 4, 5, 6, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
