from collections import defaultdict


data = [
        [
            {'user': 1, 'rating': 0},
            {'user': 2, 'rating': 10},
            {'user': 1, 'rating': 20},
            {'user': 3, 'rating': 10}
        ],
        [
            {'user': 4, 'rating': 4},
            {'user': 2, 'rating': 80},
            {'user': 1, 'rating': 20},
            {'user': 1, 'rating': 10}
        ],
    ]


def group(lst):
    user_ratings = defaultdict(int)
    for el in lst:
        u, r = el["user"], el["rating"]
        user_ratings[u] += r
    return [{"user": u, "rating": r} for u, r in user_ratings.items()]


op = [group(d) for d in data]
print(op)
