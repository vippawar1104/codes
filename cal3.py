def get_average(numbers):
    if not numbers:
        return 0  # Return 0 or raise an exception if preferred
    total = sum(numbers)  # Efficient summing
    return total / len(numbers)

print(get_average([1, 2, 3, 4]))
print(get_average([]))
