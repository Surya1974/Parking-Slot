import os
from ParkingSpace import ParkingSpace

os.system('cls' if os.name=='nt' else 'clear')

parking_space = ParkingSpace()

print("Enter 1 to assign a parking slot")
print("Enter 2 to retrieve the parking spot number of a particular vehicle")
print("Enter 'q' or 'quit' to exit the application")

while True:
    user_input = input()
    
    if  user_input.lower() == "q" or user_input.lower() == "quit": break
    
    try: 
        if user_input == "1":
            vehicleNumber = input("Enter the vehicle number - ")
            parking_space.assignParkingSlot(vehicleNumber)
            print("Vehicle is succesfully assigned.")
        elif user_input == "2":
            vehicleNumber = input("Enter the vehicle number - ")
            parking_slot = parking_space.retrieveParkingSlot(vehicleNumber)
            print(f"The parking slot is at level {parking_slot.level}, spot {parking_slot.spot}")
        else:
            print("Enter a valid option.")
            continue
    except Exception as e:
        print(e)
    print("\nEnter a new choice.")
