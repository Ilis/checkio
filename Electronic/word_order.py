def words_order(text: str, words: list) -> bool:
    text_list = text.split()
    positions = {}
    try:
        for word in words:
            positions[word] = text_list.index(word)
    except ValueError:
        return False

    return words == sorted(positions, key=positions.get)


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) is True
    assert words_order('hi world im here', ['here', 'world']) is False
    assert words_order('hi world im here', ['world']) is True
    assert words_order('hi world im here', ['world', 'here', 'hi']) is False
    assert words_order('hi world im here', ['world', 'im', 'here']) is True
    assert words_order('hi world im here', ['world', 'hi', 'here']) is False
    assert words_order('hi world im here', ['world', 'world']) is False
    assert words_order('hi world im here', ['country', 'world']) is False
    assert words_order('hi world im here', ['wo', 'rld']) is False
    assert words_order('', ['world', 'here']) is False
    print("Coding complete? Click 'Check' to earn cool rewards!")
