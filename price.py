
while True:
    try:
        distance = float(input("Distance > "))
        # Check if the distance is correct
        if distance >= 0:
            break  # Exit the loop if a valid distance is entered
        else:
            print("Distance must be a non-negative number.")
    except ValueError:
        print("The value of distance is invalid. Please enter a number!!!")

while True:
    try:
        car_fuel_consumption = float(input("Vehicle Fuel Consumption > "))
        # Check if the car fuel consumption is correct
        if car_fuel_consumption >= 0:
            break  # Exit the loop if a valid car fuel consumption is entered
        else:
            print("Fuel consumption must be a non-negative number.")
    except ValueError:
        print("The value of fuel consumption is invalid. Please enter a number!!!")

while True:
    try: 
        price_per_litre = float(input("Price per litre > "))
        if price_per_litre >= 0:
            break
        else:
            print("Price pe litre must be a non-negative number.")
    except ValueError:
        print("The value of price per litre is invalid. Please enter a number!!!")

price_for_single_trip = (distance/100) * car_fuel_consumption * price_per_litre
price_for_return = ((distance/100) * car_fuel_consumption * price_per_litre) * 2

rounded_price_for_single_trip = round(price_for_single_trip, 2)
rounded_price_for_return = round(price_for_return, 2)

print("")
print("Distance of a single trip: " + str(distance) + "km")
print("Vehicle fuel consumption : " + str(car_fuel_consumption) + "l/100")
print("Price per litre : " + str(price_per_litre))
print("")
print(f"Your Vehicle consume {car_fuel_consumption} litres per 100 Kilometres")
print("The fuel needed for your single trip is : " + str(rounded_price_for_single_trip))
print("The fuel needed for your return trip is : " + str(rounded_price_for_return))
print("")
