peoples = {
    "Jackie": 176,
    "Wilson": 185,
    "Saersha": 165,
    "Roman": 185,
    "Abram": 169,
    }

for _name, height in peoples.items():
    print(height)


def tallest_people(**men):
    print(men)
    max_height = max(height for _name, height in men.items())
    names = sorted([name for name, height in men.items()
                    if height == max_height])
    for name in names:
        print(f"{name} : {max_height}")


tallest_people(**peoples)
