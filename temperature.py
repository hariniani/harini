def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def temperature_converter():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    
    choice = int(input("Choose an option (1-6): "))

    if choice < 1 or choice > 6:
        print("Invalid choice. Please select a number between 1 and 6.")
        return

    temperature = float(input("Enter the temperature value: "))

    if choice == 1:
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {result:.2f}°F")
    elif choice == 2:
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {result:.2f}°C")
    elif choice == 3:
        result = celsius_to_kelvin(temperature)
        print(f"{temperature}°C is equal to {result:.2f}K")
    elif choice == 4:
        result = kelvin_to_celsius(temperature)
        print(f"{temperature}K is equal to {result:.2f}°C")
    elif choice == 5:
        result = fahrenheit_to_kelvin(temperature)
        print(f"{temperature}°F is equal to {result:.2f}K")
    elif choice == 6:
        result = kelvin_to_fahrenheit(temperature)
        print(f"{temperature}K is equal to {result:.2f}°F")

# Run the temperature converter
temperature_converter()
