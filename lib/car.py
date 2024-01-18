from vehicle import Vehicle

# Step 2: Defining the Subclass
# We use Vehicle as an argument for the Car class to note that Car inherits from Vehicle.
class Car(Vehicle):

    # Step 3: Overwriting Inherited Methods
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    
print(Car.__bases__)
# (<class 'vehicle.Vehicle'>,)