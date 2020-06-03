from typing import List, Tuple


def rectangles_union(recs: List[Tuple[int]]) -> int:

    def rect_coords(rectangle):
        x1, y1, x2, y2 = rectangle
        return ((x, y) for x in range(x1, x2) for y in range(y1, y2))

    all_coords = set()
    for rec in recs:
        all_coords |= set(rect_coords(rec))

    return len(all_coords)


if __name__ == '__main__':
    print("Example:")
    print(rectangles_union([
        (6, 3, 8, 10),
        (4, 8, 11, 10),
        (16, 8, 19, 11)
    ]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert rectangles_union([
        (6, 3, 8, 10),
        (4, 8, 11, 10),
        (16, 8, 19, 11)
    ]) == 33
    assert rectangles_union([
        (16, 8, 19, 11)
    ]) == 9
    assert rectangles_union([
        (16, 8, 19, 11),
        (16, 8, 19, 11)
    ]) == 9
    assert rectangles_union([
        (16, 8, 16, 8)
    ]) == 0
    assert rectangles_union([

    ]) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
