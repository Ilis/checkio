from pprint import pprint
from collections import namedtuple


D = {
    'answer': 2878,
    'input': [[[84, 43, 97, 92],
               [25, 3, 34, 21],
               [92, 49, 7, 27],
               [69, 23, 10, 36],
               [1, 36, 62, 51],
               [53, 24, 73, 65],
               [2, 46, 91, 45],
               [68, 51, 48, 30],
               [81, 79, 74, 88],
               [32, 64, 20, 90],
               [8, 51, 32, 21],
               [57, 61, 14, 91],
               [60, 55, 74, 10],
               [2, 79, 59, 64],
               [45, 11, 78, 52],
               [49, 5, 72, 32],
               [17, 93, 65, 39],
               [67, 78, 19, 35],
               [77, 68, 28, 31],
               [57, 81, 65, 17],
               [99, 58, 19, 25],
               [34, 15, 40, 90]],
              45]}

stack_count = 5
stack_size = 5
count = 20

variants = []


def fill_variants(head, rest):

    def add_variant(lst):
        variants.append(tuple(lst))
    if rest == 0:
        add_variant(head + ([0] * (stack_count - len(head))))
        return
    if len(head) == stack_count - 1:
        if rest <= stack_size:
            add_variant(head + [rest])
        return
    for i in range(min(rest, stack_size) + 1):
        fill_variants(head + [i], rest - i)


# fill_variants([], count)
# pprint(variants)

stacks = D["input"][0]
pprint(stacks)

St = namedtuple("St", ["i", "n", "s"])

substacks = []
stack_len = len(stacks[0])
for i, stack in enumerate(stacks):
    for n in range(1, stack_len + 1):
        substacks.append(St(i, n, sum(stack[:n])))
pprint(substacks)
