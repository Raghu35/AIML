"""Level 1: Conditionals, loops, functions, and scope."""

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print("Grade:", grade)

for i in range(1, 4):
    print("Loop value:", i)

count = 0
while count < 3:
    print("While loop count:", count)
    count += 1

message = "Hello"


def greet(name):
    global message
    message = f"Hello {name}"
    return message

print(greet("Nina"))
print("Message outside function:", message)
