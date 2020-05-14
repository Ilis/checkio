from typing import Iterable


def flood_area(diagram: str) -> Iterable[int]:

    vector = {'\\': -1, '_': 0, '/': 1}

    # Calc relief
    relief = [0]
    level = 0
    for c in diagram:
        level += vector[c]
        relief.append(level)

    min_level = min(relief)
    for i, d in enumerate(relief):
        relief[i] -= min_level

    # Get lowlands
    lowlands = []
    i = 0
    while i < len(relief) - 1:
        if relief[i + 1] >= relief[i]:
            i += 1
            continue
        try:
            j = relief[i + 1:].index(relief[i])
            lowlands.append(relief[i:i + j + 2])
            i += j
        except ValueError:
            i += 1

    # Calc flood
    def flood(lowland):
        bank = lowland[0]
        water = 0
        # counting triangles
        for point, prev in zip(lowland[1:], lowland[:-1]):
            water += (bank - point) * 2
            if prev > point:
                water += 1
            elif prev < point:
                water -= 1
        # returning squares
        return water // 2

    floods = [flood(lowland) for lowland in lowlands]

    return floods


if __name__ == '__main__':
    print("Example:")
    print(list(flood_area(r'\\//')))
    print(list(flood_area(r'/\\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/')))
    assert list(flood_area(r'\\//')) == [4], 'valley'
    assert list(flood_area(r'/\\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/')) == [4, 2, 1, 19, 9], 'mountains'
    assert list(flood_area(r'_/_\_')) == [], 'hill'

    print("Coding complete? Click 'Check' to earn cool rewards!")
