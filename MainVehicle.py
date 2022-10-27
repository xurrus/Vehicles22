from controllerVehicle import ControllerVehicle
import vehicleAPI as api

controller = ControllerVehicle()

def getPlate():
    plate = ""
    while (True):
        plate = input("Enter plate: ")
        if (len(plate) == 7):
            numeros = plate[0:4]
            letras = plate[4:]
            if (numeros.isdigit()):
                if (letras.isalpha()):
                    break
        print("¡Error entering the plate! (1111xxx)")
    return plate

def getChasis():
    chasis = ""
    while (True):
        chasis = input("Enter chasis (17 characters): ")
        if(len(chasis) == 17):
            break
        print("¡Error entering the chasis! (17 characters)")
    return chasis

while True:
    print("Currently we have ",controller.countVehicles()," vehicles registered")
    print("1.- Add a vehicle")
    print("2.- Delete vehicle")
    print("3.- Add odometer")
    print("4.- Confirm odometer")
    print("5.- List vehicle")
    print("6.- Exit")
    option = int(input("Choose option: "))
    if (option == 6):
        print("BYE")
        break

    #ADD VEHICLE
    elif (option == 1):
        plate = getPlate()
        desc = input("Enter description: ")
        chasis = getChasis()
        driver = input("Enter driver: ")
        if (controller.addVehicle(plate,desc,chasis,driver)):
            print("Vehicle added succesfully")
        else:
            print("Error adding vehicle. The plate already exists!")
    
    #DELETE VEHICLE
    elif (option == 2):
        plate = getPlate()
        if(controller.delVehicle(plate=plate)):
            print("Vehicle deleted succesfully")
        else:
            print("Error deleting vehicle. The plate doesn't exists!")

    #ADD ODOMETER
    elif (option == 3):
        plate = getPlate()
        date = input("Enter the day [dd-mm-yyyy]: ")
        origin = input("Origin city: ")
        destination = input("Destination city: ")
        kms = (api.getDistance(origin,destination)/1000)
        if (controller.addOdometer(plate,date,origin,destination,kms) == True):
            print("Odometer added succesfully!")
        else:
            print("Error adding odometer!")

    #CONFIRM ODOMETERS
    elif (option == 4):
        plate = getPlate()
        date = input("Enter the day [dd-mm-yyyy]: ")
        if (controller.confirmOdometer(plate,date)):
            print("Odometer confirmed!")
        else:
            print("Error confirming the odometer!")
    
    #LIST VEHICLES
    elif (option == 5):
        vehicles = {}
        vehicles = controller.getVehicles()
        for v in vehicles.values():
            print("Plate: ",v.getPlate())
            print("Description: ",v.getDescription())
            print("Chasis: ",v.getChasis())
            print("Driver: ",v.getDriverName())
            print("Unconfirmed odometer: ")
            odometer = v.getOdometers()
            for date, odo in odometer.items():
                print("\t",date,odo[0],odo[1],odo[2])
            print("Total Kms: ",v.getTotalKms())
            print("History: ",v.getHistory())



