import time
import random

def display(text, delay=1):
    """
    Display the given text with an optional delay.

    Parameters:
    text (str): The text to display.
    delay (float): Optional. The delay in seconds before displaying the next text.
    """
    print(text)
    time.sleep(delay)

def boot_up():
    """
    Simulate the boot-up sequence.
    """
    display("Initializing boot sequence...")
    display("BIOS starting up...", 2)
    display("Checking hardware components...")
    display("Loading operating system...", 3)
    display("Welcome! Server is up and running.")

def hack_process():
    """
    Simulate the hacking process.
    """
    print("Hello, who do you want to hack?")
    target = input("hack: ")
    print("OK, I will hack " + target + ".")
    print("Connecting...")
    time.sleep(5)
    print("Collecting info...")
    time.sleep(3)
    print("Installing virus...")
    time.sleep(9)
    print("Removing traces...")
    time.sleep(1)
    print("Done!")
    print("Hack was successful")
    print("Your attempt has been logged.")

def generate_robux():
    """
    Simulate the generation of robux with a percentage display and random delay.
    """
    print("What is your roblox username?")
    rbxusername = input("name here: ")
    print("Enter the amount of robux you want for " + rbxusername + ".")
    amountofrobux = int(input("amount: "))
    
    print("Generating robux for " + rbxusername + "...")
    for i in range(1, amountofrobux + 1):
        percentage = (i / amountofrobux) * 100
        print(f"Generating: {percentage:.2f}% complete")
        time.sleep(random.uniform(0.1, 0.5))  # Random delay between 0.1 and 0.5 seconds
    
    print(f"Generated {amountofrobux} robux for {rbxusername}.")
    print("Process completed.")

if __name__ == "__main__":
    boot_up()

    while True:
        hack1 = input("Free robux or hack anyone? (Type 'exit' to quit): ")
        
        if hack1.lower() == "hack anyone":
            hack_process()
        elif hack1.lower() == "free robux":
            generate_robux()
        elif hack1.lower() == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose 'hack anyone', 'free robux', or 'exit'.")
