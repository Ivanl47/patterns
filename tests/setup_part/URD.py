import random
import time

from app.services import UserService, BrockerService, LocationService, DeviceService, DeviceDataService

class URDTables:
    
    @staticmethod
    def Test_Location_Services():
        pass
    
    @staticmethod
    def Test_Device_Services():
        cur_device = DeviceService.get_by_property(name="test_device")
        cur_location = LocationService.get_by_property(room="garden", adress="Kyiv, Ukraine")
        DeviceService.update(cur_device.id, topic="empty")
        DeviceService.update(cur_device.id, name="Garden Light Updated", location_id=cur_location.id)
        time.sleep(15)
        DeviceService.delete(cur_device.id)
    
    @staticmethod
    def Test_DeviceData_Services():
        cur_device = DeviceDataService.get_by_id(2)
        DeviceDataService.create(
            device_id=1, 
            secure_status=True, 
            temprature=random.uniform(0.4, 35.0), 
            humidity=random.uniform(0.1, 99.9)
        )
        DeviceDataService.create(
            device_id=1, 
            secure_status=False, 
            humidity=random.uniform(0.1, 99.9)
        )
        list_data = DeviceDataService.get_all_by_device_id(1)
        for data in list_data:
            print(f"DeviceData: {data.id}, Device ID: {data.device_id}, Secure: {data.secure_status}, "
                  f"Temperature: {data.temprature}, Humidity: {data.humidity}")
        print(f"DeviceData: {cur_device.id}")
        DeviceDataService.update(
            cur_device.id, 
            secure_status=True, 
            temprature=100.0, 
            humidity=-59
        )
        time.sleep(15)
        DeviceDataService.delete(cur_device.id)
        
    @staticmethod
    def Test_User_Services():
        user = UserService.get_by_property(username="test_user")[0]
        
        UserService.update(
            user.id, 
            username="NormName", 
            password="new_password", 
            number="4545454545"
        )
        ready = UserService.aut_for_user(username=user.username, password="new_password1")
        print(f"1 - User auth result: {ready}")
        ready = UserService.aut_for_user(username=user.username, password="new_password")
        print(f"2 - User auth result: {ready}")
        
        UserService.update(
            user.id, 
            username="completely_new_name",
        )
        
        time.sleep(15)
        UserService.delete(user.id)
        
    @staticmethod
    def Test_Brocker_Services():
        obj = BrockerService.get_all_by_property(id_device=1)[0]
        print(f"Brocker: {obj.id}, Device ID: {obj.id_device}, User ID: {obj.id_user}")
        

        data_device = BrockerService.get_all_data_in_location(location_id=1)
        for data in data_device:
            print(f"Brocker Data: {data.id}, secure_status: {data.secure_status} temp: {data.temprature}, humidity: {data.humidity}")
        
        BrockerService.update(
            obj.id, 
            id_device=2, 
            id_user=1
        )
        
        obj = BrockerService.get_by_id(obj.id)
        print(f"Brocker: {obj.id}, Device ID: {obj.id_device}, User ID: {obj.id_user}")
        BrockerService.delete(obj.id)
        
            