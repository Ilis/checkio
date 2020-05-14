def average_mark(*marks):
    average = sum(marks) / len(marks)
    return round(average, 1)


print(average_mark(3, 3, 5, 5))
