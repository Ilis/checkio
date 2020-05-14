from random import choice


def checkio(attempts):
    all_numbers = set(range(1, 101))
    all_divisors = set(range(2, 11))

    # Filter numbers
    numbers = set(all_numbers)
    for r, d in attempts:
        valid_numbers = {n for n in all_numbers if n % d == r}
        numbers &= valid_numbers

    # Filter devisors
    divisors = all_divisors - {d for r, d in attempts}

    # Guess divisor and number
    next_divisor = choice(list(divisors))
    next_number = choice(list(numbers))

    return [next_divisor, next_number]


if __name__ == '__main__':
    # This part is using only for self-checking
    # and not necessary for auto-testing
    MAX_ATTEMPT = 8

    def initial_referee(data):
        data["attempt_count"] = 0
        data["guess"] = 0
        return data

    def check_solution(func, goal, initial):
        prev_steps = [initial]
        for attempt in range(MAX_ATTEMPT):
            divisor, guess = func(prev_steps[:])
            if guess == goal:
                return True
            if divisor <= 1 or divisor > 10:
                print("You gave wrong divisor range.")
                return False
            if guess < 1 or guess > 100:
                print("You gave wrong guess number range.")
                return False
            prev_steps.append((goal % divisor, divisor))
        print("Too many attempts.")
        return False

    assert check_solution(checkio, 47, (2, 5)), "1st example"
    assert check_solution(checkio, 94, (3, 7)), "2nd example"
    assert check_solution(checkio, 52, (0, 2)), "3rd example"
