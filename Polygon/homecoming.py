from typing import List
from collections import Counter


def home_coming(souvenirs: List[int], s: int) -> int:
    def count_items(items):
        counter = Counter(items)
        allowed = [item for item in items if counter[item] <= s]
        return len(allowed)

    n = len(souvenirs)
    return max(count_items(souvenirs[a:b + 1])
               for a in range(n)
               for b in range(a, n))


if __name__ == '__main__':
    print("Example:")
    print(home_coming([1, 1, 4, 1, 4, 4], 2))
    # print(home_coming([0, 1, 2, 3, 4, 5, 6, 7], 1))
    # exit(0)
    # These "asserts" are used for self-checking and not for an auto-testing
    assert home_coming([1, 1, 4, 1, 4, 4], 2) == 4, "Example #1"
    assert home_coming([1, 2, 5, 3, 4, 5, 6, 7], 1) == 6, "Example #2"
    assert home_coming([1, 2, 8, 8, 8, 8, 8, 3, 4, 1], 1) == 4, "Example #3"
    print("Coding complete? Click 'Check' to earn cool rewards!")
