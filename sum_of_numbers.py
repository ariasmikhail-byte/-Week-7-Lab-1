number = int(input("Enter a positive integer: "))

while number <= 0:
    print("Enter a number greater than 0.")
    number = int(input("Enter a positive integer: "))

total = 0

for value in range(1, number + 1):
    total = total + value

print(f"The sum is {total}.")