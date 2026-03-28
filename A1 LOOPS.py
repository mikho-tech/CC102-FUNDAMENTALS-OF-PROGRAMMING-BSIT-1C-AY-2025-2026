total = 0
numbers = []

while True:
    user = input("Enter a number(or 'total' to finish): ")
    if user.lower() == 'total':
        print("Calculating total...")
        break

    number = int(user)
    numbers.append(number)

    if number == 0:
        total = 0
        print(f"({number} RESET. Total is: {total})")

    elif number % 2 == 0:
        total += number
        print(f"({number} is even → ADDED. Total is: {total})")

    else:
        total -= number
        print(f"({number} is odd → SUBTRACTED. Total is: {total})")

print("--- Summary of all numbers you entered ---")
for i in numbers:
    if i == 0:
        print(f"{i} → RESET THE TOTAL")
    elif i % 2 == 0:
        print(f"{i} → EVEN (WAS ADDED)")
    else:
        print(f"{i} → ODD (WAS SUBTRACTED)")