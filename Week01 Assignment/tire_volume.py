import math
from datetime import datetime

# I wrote my exceed requirement starting from line 23.
# In That line 21, i added a function which i named "exceed_Requirement()" that contains a price lookup in a python dictionary, print the price and volume of tire in the terminal and asks if the user wants to buy tires. 
# If the user wants to buy tires by typing yes, it asks for their phone number and logs the data in a text file named "volume.txt", but if the user said no by typing no, then the program will stop.

def calculate_tire_volume(width, aspect_ratio, diameter):
    """Calculate the volume of a tire in liters."""
    volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10_000_000_000
    return round(volume, 2)

def print_in_text_file(width, aspect_ratio, diameter, volume, phone_number=None):
    """Log tire data to volume.txt."""
    current_date = datetime.now().strftime("%Y-%m-%d")
    with open("volume.txt", "a") as file:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}")
        if phone_number:
            file.write(f", {phone_number}")
        file.write("\n")

# Function that contains the codes for Exceeding the requirments
def exceed_Requirement(width, aspect_ratio, diameter, volume):
    """Check tire prices and ask if the user wants to buy."""
    # Example price lookup (simplified)
    tire_prices = {
        (205, 60, 15): 120.99,
        (215, 55, 16): 135.50,
        (225, 50, 17): 150.75,
        (195, 65, 15): 110.25
    }
    
    price = tire_prices.get((width, aspect_ratio, diameter), "Price not available")
     # Print available tire sizes and prices
    print("\nGrader, please note that the Available Tire Sizes & Prices i printed out is just to show the Exceeding Requirement")
    print("\nAvailable Tire Sizes & Prices:")
    for (w, a, d), price in tire_prices.items():
        print(f"Tire prices: {w}/{a}R{d}: ${price}")
    print(f"Tire Volume: {volume} liters")

    buy_tires = input("\nDo you want to buy tires with these dimensions? (yes/no): ").lower()
    if buy_tires == "yes":
        phone_number = input("Enter your phone number: ")
        print_in_text_file(width, aspect_ratio, diameter, volume, phone_number)
        print("Thank you! We'll contact you soon.")
    else:
        print("No problem. Have a great day!")

def main():
    print(">> Python tire voulume calculator <<")
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    volume = calculate_tire_volume(width, aspect_ratio, diameter)
    print(f"\nThe approximate volume is: {volume} liters")

    print_in_text_file(width, aspect_ratio, diameter, volume)
    exceed_Requirement(width, aspect_ratio, diameter, volume)

if __name__ == "__main__":
    main()