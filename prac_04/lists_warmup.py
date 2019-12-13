numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0])  # 3
print(numbers[-1])  # 2
print(numbers[3])  # 1
print(numbers[:-1])  # [3, 1, 4, 1, 5, 9]
print(numbers[3:4])  # [1]
print(5 in numbers)  # True
print(7 in numbers)  # False
print("3" in numbers)  # False
print(numbers + [6, 5, 3])  # [3, 1, 4, 1, 5, 9, 6, 5, 3]
numbers[0] = "ten"  # Change the first element of numbers to “ten”
numbers[6] = 1  # Change the last element of numbers to 1
print(numbers[2:7])  # Get all the elements from numbers except the first two
print(9 in numbers)  # Check if 9 is an element of numbers
