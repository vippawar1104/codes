def get_average(numbers):
    if not numbers:
        return 0  # Return 0 or raise an exception if preferred
    
    # Check if all elements in the list are numeric
    if not all(isinstance(i, (int, float)) for i in numbers):
        raise ValueError("All elements in the list must be numeric")
    
    total = sum(numbers)
    return total / len(numbers)

print(get_average([1, 2, 3, 4]))
print(get_average([1, "two", 3, 4]))  # This will raise a ValueError
print(get_average([]))
