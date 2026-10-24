weight = float(input("Enter the package weight in kilograms: "))

while weight <= 0 or weight > 20:
    print("Weight must be greater than 0 and not more than 20 kilograms.")
    weight = float(input("Enter the package weight in kilograms: "))

distance = float(input("Enter the shipping distance in miles: "))

while distance < 10 or distance > 3000:
    print("Distance must be between 10 and 3,000 miles.")
    distance = float(input("Enter the shipping distance in miles: "))

if weight <= 2:
    rate = 1.10
elif weight <= 6:
    rate = 2.20
elif weight <= 10:
    rate = 3.70
else:
    rate = 4.80

charge = distance / 500 * rate
print(f"Shipping charge: ${charge:.2f}")