def checkio(matrix):
    all_parts = {(i, j, matrix[i][j])
                 for i in range(len(matrix))
                 for j in range(len(matrix[0]))
                 if matrix[i][j] > 0
                 }
    free_parts = set(all_parts)

    # Neighbour parts
    def neighbours(p):
        i_, j_, v_ = p

        return {(i, j, v)
                for i, j, v in all_parts
                if v == v_ and abs(i - i_) + abs(j - j_) == 1}

    # Build groups of parts
    groups = []
    while free_parts:
        group_set = set()
        group_set.add(free_parts.pop())
        group_len_prev, group_len = 0, 1
        # While group still extends
        while group_len_prev < group_len:
            for part in group_set.copy():
                for nb in neighbours(part):
                    group_set.add(nb)
                    free_parts.discard(nb)
            group_len_prev, group_len = group_len, len(group_set)

        groups.append(group_set)

    # Get the answer
    max_group = max(groups, key=len)
    return [len(max_group), list(max_group)[0][2]]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'
