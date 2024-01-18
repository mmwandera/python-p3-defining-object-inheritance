
# lib/vehicle.py

# Step 1: Defining the Superclass
# Instances of Vehicle initialize with a wheel size and number. We also have go() and fill_up_tank() instance methods that describe some common vehicle behavior.

class Vehicle:
    
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        return "filling up!"

