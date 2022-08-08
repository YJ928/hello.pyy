price_per_kWh = int(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
number_of_days = int(input("Enter number of billing days: "))
result = price_per_kWh * daily_use * number_of_days * 0.01
print("Estimated bill: $", result)
print()

tariff = int(input("Which tariff? 11 or 31: " ))
if tariff == 11:
    price = 0.244618
else:
    price = 0.136928
daily_use = float(input("Enter daily use in kWh: "))
number_of_days = int(input("Enter number of billing days: "))
result = price * daily_use * number_of_days
print("Estimated bill: $", result)
