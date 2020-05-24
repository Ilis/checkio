import json
from pprint import pprint


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


fill_variants([], count)
pprint(variants)
