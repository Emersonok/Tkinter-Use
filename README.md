from functools import reduce

def multiply_values(number):
    return reduce(lambda x, y: x * y, number)

# Example usage
result = multiply_values([2, 3, 4])
print(result) # Output: 24

