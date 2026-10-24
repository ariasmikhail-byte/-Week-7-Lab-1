print("Minutes\tCalories burned")

for minutes in range(5, 31, 5):
    calories = minutes * 3.6
    print(f"{minutes}\t{calories:.1f}")