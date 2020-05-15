def middle(text):
    text_len = len(text)
    if text_len < 3:
        return text[:]
    p = (text_len - 1) // 2
    return text[p:-p]


if __name__ == '__main__':
    print("Example:")
    print(middle('example'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert middle('example') == 'm'
    assert middle('test') == 'es'
    assert middle('very-very long sentence') == 'o'
    assert middle('I') == 'I'
    assert middle('no') == 'no'
    print("Coding complete? Click 'Check' to earn cool rewards!")
