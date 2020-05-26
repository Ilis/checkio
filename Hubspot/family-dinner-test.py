from pprint import pprint
from collections import deque
import sys


tests_dir = r"C:\Python\Proj\data"
sys.path.append(tests_dir)


from family_dinner_tests import TESTS


test_stacks = TESTS["Medium"][0]

stacks = test_stacks["input"][0]
plates_count = test_stacks["input"][1]
test_answer = test_stacks["answer"]
pprint(stacks)
print(f"{plates_count = }, {test_answer = }")
stack_len = len(stacks[0])

substacks = []
for i, stack in enumerate(stacks):
    for n in range(1, stack_len + 1):
        substack = (i, n, sum(stack[:n]))
        substacks.append(substack)

queue = deque()
for i, n, b in substacks:
    queue.append((i, n, b, [(i, n)]))

pprint(queue)
