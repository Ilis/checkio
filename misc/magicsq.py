from itertools import permutations
from copy import deepcopy


def checkio(data):

    def fill_data(data, missed):
        nonlocal size
        new_data = deepcopy(data)
        new_missed = list(missed)
        for i in range(size):
            for j in range(size):
                if new_data[i][j] == 0:
                    new_data[i][j] = new_missed.pop(0)
        return new_data


    def check_magic(square):
        nonlocal size
        nonlocal magic_number
        for i in range(size):
            if sum(square[i][j] for j in range(size)) != magic_number:
                return False
            if sum(square[j][i] for j in range(size)) != magic_number:
                return False
        if sum(square[i][i] for i in range(size)) != magic_number:
            return False
        if sum(square[i][size - 1 - i] for i in range(size)) != magic_number:
            return False
        return True


    magic_numbers = {3: 15, 4: 34, 5: 65}
    size = len(data[0])
    magic_number = magic_numbers[size]
    used_numbers = {i for rows in data for i in rows}
    missed_numbers = set(range(1, size**2 + 1)) - used_numbers

    # Find candidate numbers for rows
    good_rows = []
    for i in range(size):
        good_rows.append([])
        missed_count = data[i].count(0)

        good_rows[i] = []
        for pm in permutations(missed_numbers, missed_count):
            if sum(data[i]) + sum(pm) == magic_number:
                good_rows[i].append(list(pm))

    # Find candidate sequences
    def update_seq(head, tail_lst):
        if not tail_lst:
            if set(head) == missed_numbers:
                good_sequences.append(head)
            return

        for hn in tail_lst[0]:
            update_seq(head + hn, tail_lst[1:])


    good_sequences = []
    update_seq([], good_rows)

    for gs in good_sequences:
        square = fill_data(data, gs)
        if check_magic(square):
            result = square
            break

    return result


if __name__ == '__main__':
    #This part is using only for self-testing.
    def check_solution(func, in_square):
        SIZE_ERROR = "Wrong size of the answer."
        MS_ERROR = "It's not a magic square."
        NORMAL_MS_ERROR = "It's not a normal magic square."
        NOT_BASED_ERROR = "Hm, this square is not based on given template."
        result = func(in_square)
        #check sizes
        N = len(result)
        if len(result) == N:
            for row in result:
                if len(row) != N:
                    print(SIZE_ERROR)
                    return False
        else:
            print(SIZE_ERROR)
            return False
        #check is it a magic square
        # line_sum = (N * (N ** 2 + 1)) / 2
        line_sum = sum(result[0])
        for row in result:
            if sum(row) != line_sum:
                print(MS_ERROR)
                return False
        for col in zip(*result):
            if sum(col) != line_sum:
                print(MS_ERROR)
                return False
        if sum([result[i][i] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False
        if sum([result[i][N - i - 1] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False

        #check is it normal ms
        good_set = set(range(1, N ** 2 + 1))
        user_set = set([result[i][j] for i in range(N) for j in range(N)])
        if good_set != user_set:
            print(NORMAL_MS_ERROR)
            return False
        #check it is the square based on input
        for i in range(N):
            for j in range(N):
                if in_square[i][j] and in_square[i][j] != result[i][j]:
                    print(NOT_BASED_ERROR)
                    return False
        return True


    # testsq = [
    #     [0, 0, 0],
    #     [0, 5, 0],
    #     [0, 0, 0]
    # ]
    # print(checkio(testsq))
    # # print(check_solution(checkio, testsq))
    # exit(0)

    assert check_solution(checkio,
                          [[2, 7, 6],
                           [9, 5, 1],
                           [4, 3, 0]]), "1st example"

    assert check_solution(checkio,
                          [[0, 0, 0],
                           [0, 5, 0],
                           [0, 0, 0]]), "2nd example"

    assert check_solution(checkio,
                          [[1, 15, 14, 4],
                           [12, 0, 0, 9],
                           [8, 0, 0, 5],
                           [13, 3, 2, 16]]), "3rd example"
