"""Level 1: Strings, lists, tuples, sets, and dictionaries."""

message = "python is fun"
print("Uppercase:", message.upper())
print("Split:", message.split())
print("Slice:", message[0:6])

numbers = [1, 2, 3, 4]
numbers.append(5)
print("List:", numbers)
print("List length:", len(numbers))

coordinates = (10, 20)
print("Tuple:", coordinates)

items = {"apple", "banana", "apple"}
print("Set:", items)

student = {"name": "Riya", "age": 20, "grade": "A"}
print("Dictionary:", student)
print("Name:", student["name"])
student["city"] = "Pune"
print("Updated dictionary:", student)
