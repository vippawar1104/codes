def get_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)
print(get_average([1, 2, 3, 4]))
print(get_average([]))
