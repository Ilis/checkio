def digit_stack(commands):

    class DigitStack:
        def __init__(self):
            self.stack = []
            self.total = 0

        def push(self, x):
            self.stack.append(x)

        def pop(self):
            self.total += self.stack.pop() if self.stack else 0

        def peek(self):
            self.total += self.stack[-1] if self.stack else 0

    ds = DigitStack()

    for command in commands:
        if command.startswith("PUSH"):
            ds.push(int(command.split()[-1]))
        elif command.startswith("POP"):
            ds.pop()
        elif command.startswith("PEEK"):
            ds.peek()

    return ds.total


if __name__ == '__main__':
    print("Example:")
    print(digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                       "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
