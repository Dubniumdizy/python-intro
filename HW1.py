"""Temperature Conversion Application.

This script offers interactive tools to safely convert numerical temperature 
readings seamlessly between the Celsius, Fahrenheit, and Kelvin scales.
"""

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Converts a Fahrenheit temperature reading into its Celsius equivalent.

    Args:
        fahrenheit (float): The input temperature scale in Fahrenheit.

    Returns:
        float: The calculated temperature value in Celsius.
    """
    return (fahrenheit - 32) * 5 / 9


def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts a Celsius temperature reading into its Fahrenheit equivalent.

    Args:
        celsius (float): The input temperature scale in Celsius.

    Returns:
        float: The calculated temperature value in Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius: float) -> float:
    """Converts a Celsius temperature reading into its Kelvin equivalent.

    Args:
        celsius (float): The input temperature scale in Celsius.

    Returns:
        float: The calculated temperature value in Kelvin.
    """
    return celsius + 273.15


def kelvin_to_celsius(kelvin: float) -> float:
    """Converts a Kelvin temperature reading into its Celsius equivalent.

    Args:
        kelvin (float): The input temperature scale in Kelvin.

    Returns:
        float: The calculated temperature value in Celsius.
    """
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """Converts a Fahrenheit reading into Kelvin by routing through Celsius.

    Args:
        fahrenheit (float): The input temperature scale in Fahrenheit.

    Returns:
        float: The calculated temperature value in Kelvin.
    """
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """Converts a Kelvin reading into Fahrenheit by routing through Celsius.

    Args:
        kelvin (float): The input temperature scale in Kelvin.

    Returns:
        float: The calculated temperature value in Fahrenheit.
    """
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main() -> None:
    """Manages the user interface workflow and executes choices continuously.

    This loop runs indefinitely, providing temperature conversion options
    until the user selects the designated option to exit the program.
    """
    # Define the menu as a clean, single multi-line string block
    menu_text = """
Temperature converter
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
7. Exit program
"""

    while True:
        print(menu_text)
        choice = input("which conversion do you want to do?  ")

        if choice == "7":
            print("Exiting program. Goodbye!")
            break

        if choice == "1":
            temperature = float(input("enter temperature in Celsius: "))
            result = celsius_to_fahrenheit(temperature)
            print("that corresponds to", result, "Fahrenheit")
            
        elif choice == "2":
            temperature = float(input("enter temperature in Fahrenheit: "))
            result = fahrenheit_to_celsius(temperature)
            print("that corresponds to", result, "Celsius")
            
        elif choice == "3":
            temperature = float(input("enter temperature in Celsius: "))
            result = celsius_to_kelvin(temperature)
            print("that corresponds to", result, "Kelvin")
            
        elif choice == "4":
            temperature = float(input("enter temperature in Kelvin: "))
            result = kelvin_to_celsius(temperature)
            print("that corresponds to", result, "Celsius")
            
        elif choice == "5":
            temperature = float(input("enter temperature in Fahrenheit: "))
            result = fahrenheit_to_kelvin(temperature)
            print("that corresponds to", result, "Kelvin")
            
        elif choice == "6":
            temperature = float(input("enter temperature in Kelvin: "))
            result = kelvin_to_fahrenheit(temperature)
            print("that corresponds to", result, "Fahrenheit")
            
        else:
            print("invalid choice")


if __name__ == "__main__":
    main()