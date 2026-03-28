numbers = []

for i in range(1, 10):
    numbers.append(i)

print ("Original list:", numbers)
print ("Length of list:", len(numbers))

y = 1

while y < len(numbers):
    if numbers.count(numbers[y]) > 1:
        numbers.remove(numbers[y])
    else:
        y = y + 1

print("The list with unique elements:")
print(numbers)

