def goes_after(word: str, first: str, second: str) -> bool:
    i1, i2 = word.find(first), word.find(second)
    return i1 > -1 and i2 == i1 + 1


if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'o'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') is True
    assert goes_after('world', 'l', 'o') is False
    assert goes_after('panorama', 'a', 'n') is True
    assert goes_after('list', 'l', 'o') is False
    assert goes_after('', 'l', 'o') is False
    assert goes_after('list', 'l', 'l') is False
    print("Coding complete? Click 'Check' to earn cool rewards!")
