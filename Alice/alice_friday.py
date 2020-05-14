from datetime import datetime as dt


def friday(day):
    return (4 - dt.strptime(day, "%d.%m.%Y").weekday()) % 7


if __name__ == '__main__':
    print("Example:")
    print(friday('23.04.2018'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert friday('23.04.2018') == 4
    assert friday('01.01.1999') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
