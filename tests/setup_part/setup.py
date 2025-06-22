import random

from app.services import UserService, BrockerService, LocationService, DeviceService, DeviceDataService

class SetupTables:
    
    @staticmethod
    def Base_Location_Services():
        LocationService.create("kitchen", "Lviv, Ukraine")
        LocationService.create("living room", "Lviv, Ukraine")
        LocationService.create("bedroom", "Lviv, Ukraine")
        
        LocationService.create("office", "Kyiv, Ukraine")
        LocationService.create("garage", "Kyiv, Ukraine")
        LocationService.create("garden", "Kyiv, Ukraine")
    
    @staticmethod  
    def Base_Device_Services(list_locations=None):
        min = 1
        max = len(list_locations) if list_locations else 1
        
        DeviceService.create("Kitchen Light", "Light", "kitchen/light", random.randint(min, max))
        DeviceService.create("Living Room Fan", "Fan", "living_room/fan", random.randint(min, max))
        DeviceService.create("Living Room Light", "Light", "living_room/light", random.randint(min, max))
        DeviceService.create("Bedroom Light", "Light", "bedroom/light", random.randint(min, max))
        
        DeviceService.create("Office Light", "Light", "office/light", random.randint(min, max))
        DeviceService.create("Garage Light", "Light", "garage/light", random.randint(min, max))
        DeviceService.create("Garden Light", "Light", "garden/light", random.randint(min, max))
    
    @staticmethod  
    def Base_DeviceData_Services(device_list=None):
        min = 1
        max = len(device_list) if device_list else 1
        
        DeviceDataService.create(
            random.randint(min, max), secure_status=True, 
            temprature=random.uniform(0.4, 35.0), 
            humidity=random.uniform(0.1, 99.9)
        )
        DeviceDataService.create(
            random.randint(min, max), secure_status=False, 
            humidity=random.uniform(0.1, 99.9)
        )
        DeviceDataService.create(
            random.randint(min, max), secure_status=True, 
            humidity=random.uniform(0.1, 99.9)
        )
        DeviceDataService.create(
            random.randint(min, max), secure_status=False, 
            temprature=random.uniform(0.4, 35.0),
        )
    
    @staticmethod
    def Base_User_Services():
        UserService.create("Hetman", "12345678", "0987654321")
        UserService.create("Ivan", "12345678", "0987654322")
        UserService.create("Petro", "12345678", "0987654323")
        UserService.create("Oleg", "12345678", "0987654324")
        UserService.create("Sergiy", "12345678", "0987654325")
        UserService.create("Andriy", "12345678", "0987654326")
        UserService.create("Vasyl", "12345678", "0987654327")
        
    @staticmethod
    def Base_Brocker_Services():
        user = UserService.get_by_property(username="Hetman")[0]
        device = DeviceService.get_by_property(name="Kitchen Light")
        BrockerService.create(device.id, user.id)
        
        user = UserService.get_by_property(username="Ivan")[0]
        device = DeviceService.get_by_property(name="Living Room Fan")
        BrockerService.create(device.id, user.id)
        
        user = UserService.get_by_property(username="Petro")[0]
        device = DeviceService.get_by_property(name="Bedroom Light")
        BrockerService.create(device.id, user.id)