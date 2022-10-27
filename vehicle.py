class Vehicle:

    def __init__(self,plate,desc,chasis,driver):
        self.__plate = plate
        self.__description = desc
        self.__chasis = chasis
        self.__driverName = driver
        self.__odometers = {}
        self.__totalKms = 0
        self.__history = ""
        
    def getPlate(self):
        return self.__plate
    def getDescription(self):
        return self.__description
    def setDescription(self, desc):
        self.__description = desc
    def getChasis(self):
        return self.__chasis
    def getDriverName(self):
        return self.__driverName
    def getOdometers(self):
        return self.__odometers
    def getTotalKms(self):
        return self.__totalKms
    def getHistory(self):
        return self.__history

    def addOdometer(self,date,origin,destination,kms):
        self.__odometers[date] = (origin,destination,kms)

    def confirmOdometer(self,date):
        details = self.__odometers.pop(date)
        self.__history += str(details[0])+"-"+str(details[1])+"-"+str(details[2])
        self.__history += "\n"
        self.__totalKms += details[2]
