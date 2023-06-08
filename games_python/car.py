class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if self.is_running:
            print("The car is already running.")
        else:
            self.is_running = True
            print("The car has been started.")

    def stop(self):
        if not self.is_running:
            print("The car is already stopped.")
        else:
            self.is_running = False
            print("The car has been stopped.")

    def drive(self, distance):
        if self.is_running:
            print(f"The {self.make} {self.model} is driving {distance} miles.")
        else:
            print("Please start the car first.")
