#Andrew Blanchard
#Project 2

class Vehicle:
    #This is the base attributes of both vehicles:
    def __init__(self, make, year, availability):
        self.make = make
        self.year = year
        self.availability = availability

class Car(Vehicle):
    TotalCarCount = 0

    #Builds on the Vehicle class and adopts the Vehicle class attributes.
    def __init__(self, make, year, availability, body_type, number_of_doors):
        super().__init__(make, year, availability) #will use the __init__() method of the parent class Vehicle
        self.body_type = body_type
        self.number_of_doors = number_of_doors
        Car.TotalCarCount += 1

    #Allows me later in the code to make a system of adding new cars.
    @classmethod
    def from_string(cls, car_info):
        make, year, availability, body_type, number_of_doors = car_info.split(",")
        return cls(make, year, availability, body_type, number_of_doors)

    #This just desplays the cars in the CarList
    @staticmethod
    def display_cars(CarList):
        for car in CarList:
            print(f"It is a {car.year} {car.make} {car.body_type}, it has {car.number_of_doors} doors. Availabile: {car.availability}")

class Motorcycle(Vehicle):
    TotalMotorcycleCount = 0

    def __init__(self, make, year, availability, has_sidecar):
        super().__init__(make, year, availability)
        self.has_sidecar = has_sidecar
        Motorcycle.TotalMotorcycleCount += 1

    @classmethod
    def from_string(cls, motercycle_info):
        make, year, availability, has_sidecar = motercycle_info.split(",")
        return cls(make, year, availability, has_sidecar)
    
    @staticmethod
    def display_motorcycles(MotorcycleList):
        for Motor in MotorcycleList:
            print(f"It is a {Motor.year} {Motor.make}. Has sidecar: {Motor.has_sidecar}. Availabile: {Motor.availability}")

#-----------------------------------------------------------------------------------------
#Start of my main code:

#Cars I hardcoded in:
Car1 = Car("Black Honda Civic",2013,True,"sedan",4)
Car2 = Car("Silver Honda Civic",2014,False,"sedan",4)
Motorcycle1 = Motorcycle("Gold Wing Tour",2024,True,False)
Motorcycle2 = Motorcycle("Black Honda Shadow",2020,True, True)

#Stores the make of cars and motercycles respectively
CarList = [Car1,Car2]
MotorcycleList = [Motorcycle1,Motorcycle2]

#The main code:
name = input("\nWelcome to the Boston Police Department's fleet tracking system, please insert your last name: ")
while(True):
    print(f"\nHi Officer {name}! Would you like to: \n 1. See the list of all cars? \n 2. See the list of all motorcycles? \n 3. Add a new vehicle? \n 4. See the count of every vehicle type?")
    value = int(input("\n\tEnter HERE: "))
    if(value <= 4 and value >= 1):
        #Calls on the functions depending on what number was input.
        if(value == 1):
            #Option 1 displays the cars
            Car.display_cars(CarList)

        if(value == 2):
            #Option 2 displays the motorcycles
            Motorcycle.display_motorcycles(MotorcycleList)

        if(value == 3):
            #Option 3 allows you to either add a car or a motorcycle and adds them to their respective lists
            value2 = int(input("Alrighty Officer, would you like to: \n 1. Add a new CAR \n 2. Add a new MOTORCYCLE \n\tEnter HERE: "))
            if(value2 <= 2 and value2 >= 1):
                if(value2 == 1):
                    #Adds a car to a variable, then adds it to the car list.
                    CarAdded = Car.from_string(input("Enter Car Info(make,year,availability,body_type,number_of_doors): "))
                    CarList.append(CarAdded)
                if(value2 == 2):
                    #Same here, but with motorcycles
                    MotorcycleAdded = Motorcycle.from_string(input("Enter Motorcycle Info(make,year,availability,has_sidecar): "))
                    MotorcycleList.append(MotorcycleAdded)

            else:
                print("\nTry Again, invalid selection")

        if(value == 4):
            #Option 4 just adds both counts together alongside just the cars and just the motorcycle counts.
            print(f"There are {Car.TotalCarCount + Motorcycle.TotalMotorcycleCount} vehicles in total: \n{Car.TotalCarCount} are cars, \n{Motorcycle.TotalMotorcycleCount} are motorcycles")
            #This technically works too for some reason, ignore it:      print(f"There are {len(CarList) + len(MotorcycleList)} vehicles in total: \n{len(CarList)} are cars, \n{len(MotorcycleList)} are motorcycles")

    else:
        print("\nTry Again, invalid selection")