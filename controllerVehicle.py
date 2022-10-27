from vehicle import Vehicle

class ControllerVehicle():

    #CONSTUCTOR
    def __init__(self):
        #Key:Plate - Value:VehicleObject
        self.__vehicles={}

    #1 ADD VEHICLE
    def addVehicle(self,plate,desc,chasis,driver):
        if plate in self.__vehicles:
            return False
        newVehicle = Vehicle(plate,desc,chasis,driver)
        self.__vehicles[plate] = newVehicle
        return True

    #2 DELETE VEHICLE
    def delVehicle(self, plate):
        if plate not in self.__vehicles:
            return False
        
        self.__vehicles.pop(plate)
        return True

    #COUNT VEHICLES
    def countVehicles(self):
        return len(self.__vehicles)

    #3 ADD ODOMETER
    def addOdometer(self,plate,date,origin,destination,kms):
        if plate not in self.__vehicles:
            return False
        vehicle = self.__vehicles[plate]
        vehicle.addOdometer(date,origin,destination,kms)
        return True

    #5 RETURN LIST VEHICLES
    def getVehicles(self):
        return self.__vehicles

    #4 CONFIRM ODOMETER
    def confirmOdometer(self,plate,date):
        if plate not in self.__vehicles:
            return False
        vehicle = self.__vehicles[plate]
        if date not in vehicle.getOdometers():
            return False
        vehicle.confirmOdometer(date)
        return True

    