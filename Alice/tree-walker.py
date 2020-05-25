def tree_walker(tree, target):

    def walk(subtree):
        nonlocal count

        if subtree == target:
            count += 1
            return

        if isinstance(subtree, list):
            for item in subtree:
                walk(item)
        if isinstance(subtree, dict):
            for item in subtree.values():
                walk(item)

    count = 0
    walk(tree)
    return count


if __name__ == '__main__':
    print("Example:")
    print(tree_walker([1, "2", 3, [[3], 1, {1: "one"}]], 1))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert tree_walker([1, "2", 3, [[3], 1, {1: "one"}]], 1) == 2, "1st"
    assert tree_walker({"one": 1, "two": [{1: "one", 2: "two"}, 1, "1", "one"]}, 1) == 2, "2nd"
    assert tree_walker({"one": [1, 2], "two": [{1: "one", 2: "two"}, [1, 2], "1", "one"]}, [1, 2]) == 2, "3rd"
    assert tree_walker(5, 5) == 1, "4th"
    assert tree_walker([5, 6, 2, "1"], 1) == 0, "5th"
    assert tree_walker([[dict()], [[[3], [3, 5]]], [], []], 3) == 2, "6th"
    assert tree_walker([{1: "one"}, {2: "two"}, "two", ["two", {"two": "one"}]], "two") == 3, "7th"
    print("Coding complete? Click 'Check' to earn cool rewards!")
