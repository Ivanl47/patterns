from app.services import UserService, DeviceService, LocationService, DeviceDataService, BrockerService
from moduls.tools import log_def, VariableTools

class UserActivity:
    
    ################################ BISNES LOGIC #####################################
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_all_data_in_location(location_id: int) -> list:
        VariableTools.check_id(location_id, "Location")
        location = LocationService.get_by_id(location_id)
        print(location.id)
        if not location:
            raise ValueError(f"Location with id {location_id} does not exist.")
        
        devices = DeviceService.get_by_property(location_id=location_id, all=True)
        print(devices)
        data = []
        for device in devices:
            device_data = DeviceDataService.get_all_by_device_id(device.id)
            data.extend(device_data)
        
        return data
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_device_in_location(location_id: int) -> list:
        VariableTools.check_id(location_id, "Location")
        location = LocationService.get_by_id(location_id)
        if not location:
            raise ValueError(f"Location with id {location_id} does not exist.")
        
        devices = DeviceService.get_by_property(location_id, all=True)
        return devices
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_device_by_user(user_id: int) -> list:
        VariableTools.check_id(user_id, "User")
        user = UserService.get_by_id(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} does not exist.")
        
        brockers = BrockerService.get_all_by_property(id_user=user_id)
        devices = []
        for brocker in brockers:
            if not brocker:
                raise ValueError(f"No brockers found for user with id {user_id}.")
            device = DeviceService.get_by_id(brocker.id_device)
            if device:
                devices.append(device)
        
        return devices
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_middle_data_in_location(location_id: int) -> dict:
        VariableTools.check_id(location_id, "Location")
        location = LocationService.get_by_id(location_id)
        if not location:
            raise ValueError(f"Location with id {location_id} does not exist.")
        
        devices = DeviceService.get_by_property(location_id=location_id, all=True)
        data = {
            "temperature": 0.0,
            "humidity": 0.0,
        }
        count = 0
        for device in devices:
            device_data = DeviceDataService.get_all_by_device_id(device.id)
            if not device_data:
                continue
            for data_point in device_data:
                count += 1
                if data_point.temprature >= -999:
                    data["temperature"] += data_point.temprature
                if data_point.humidity >= -999:
                    data["humidity"] += data_point.humidity
        if count == 0:
            raise ValueError(f"No data found for location with id {location_id}.")
        data["temperature"] /= count
        data["humidity"] /= count
        return data
    
    @log_def(obj_name=__name__)
    @staticmethod
    def autorize_user(password: str, username: str = None, number: str = None) -> bool:
        VariableTools.one_can_be_not_none(username, number)
        VariableTools.no_one_can_be_none(password)
        if username:
            user = UserService.aut_for_user(username, password)
        else:
            user = UserService.aut_for_number(number, password)
        return user
    
    @log_def(obj_name=__name__)
    @staticmethod
    def set_data_from_csv(path: str) -> None:
        """
        Set data from CSV file to the database.
        :param path: Path to the CSV file.
        """
        import csv

        VariableTools.no_one_can_be_none(path)
        if not path.endswith('.csv'):
            raise ValueError("The file must be a CSV file.")

        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    user = UserService.create(
                        username=row['user_username'],
                        password=row['user_password'],
                        number=row['user_number']
                    )
                except ValueError as e:
                    print("Already exists user with this username and number")

                try:
                    # Створення локації
                    location = LocationService.create(
                        room=row['location_room'],
                        adress=row['location_adress']
                    )
                except ValueError as e:
                    print("Already exists location with this room and adress")
                    
                try:    
                    # Створення пристрою
                    device = DeviceService.create(
                        name=row['device_name'],
                        type=row['device_type'],
                        topic=row['device_topic'],
                        location_id=location.id
                    )
                except ValueError as e: 
                    print("Already exists device with this name, type and topic in this location")

                try:
                    # Створення DeviceData
                    DeviceDataService.create(
                        device_id=device.id,
                        secure_status=row.get('device_data_secure_status', 'False') == 'True',
                        temprature=float(row.get('device_data_temprature', -999)),
                        humidity=float(row.get('device_data_humidity', -999))
                    )
                except ValueError as e:
                    print("Error creating DeviceData:", e)

                try:
                    # Створення Brocker
                    BrockerService.create(
                        id_device=device.id,
                        id_user=user.id
                    )
                except ValueError as e:
                    print("Already exists brocker with this device and user")
            
            