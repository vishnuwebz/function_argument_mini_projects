# 4 calculator with operation type

def calculate(operation="add", *nums):
    if operation  == "add":
        print("Sum:", sum(nums))
    elif operation == "multiply":
        result = 1
        for n in nums:
            result *= n
        print("Product:", result)
    else:
        print("unsupported operation")

calculate("add", 5, 10, 15)
calculate("multiply", 2, 3, 4)

"""
Sum: 30
Product: 24
"""