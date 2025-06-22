from app.dao import DeviceDataDao, DeviceDao, LocationDao, UserDao, BrockerDao
from app.models import DeviceData, Device, Location, User, Brocker

class Data:
    device_data = {
        "common": {
            "device_id": 1,
            "secure_status": True,
            "temprature": 100,
            "humidity": 11
        },
        "to_delete": {
            "device_id": 1,
            "secure_status": True,
            "temprature": 100,
            "humidity": 11
        },
        "change": {
            "device_id": 1,
            "secure_status": False,
            "temprature": 200,
            "humidity": 22
        }
    }
    
    device = {
       "common": {
           "device_id": 1,
           "location_id": 1,
           "name": "test_device",
           "type": "test_type",
           "topic": "test_topic"
       },
       "to_delete": {
           "device_id": 1,
           "location_id": 1,
           "name": "test_device_to_delete",
           "type": "test_type_to_delete",
           "topic": "test_topic_to_delete"
       },
       "change":{
            "device_id": 1,
            "location_id": 1,
            "name": "test_device_change",
            "type": "test_type_change",
            "topic": "test_topic_change"
       }
    }
    
    location = {
        "common": {
            "room": "test_location",
            "adress": "test_address"
        },
        "to_delete": {
            "room": "test_location_to_delete",
            "adress": "test_address_to_delete"
        },
        "change": {
            "room": "test_location_change",
            "adress": "test_address_change"
        }
    }
    
    broker = {
        "common": {
            "device_id": 1,
            "user_id": 1
        },
        "to_delete": {
            "device_id": 1,
            "user_id": 1
        },
        "change": {
            "device_id": 1,
            "user_id": 1
        }
    }
    user = {
        "common": {
            "username": "test_user",
            "password": "test_password",
            "number": "380955512543"
        },
        "to_delete": {
            "username": "test_user_to_delete",
            "password": "test_password_to_delete",
            "number": "380955512523"
        },
        "change": {
            "username": "test_user_change",
            "password": "test_password_change",
            "number": "380952312111"
        }
    }
    
    @staticmethod
    def get_device_data() -> dict:
       return Data.device_data
   
    @staticmethod
    def get_device() -> dict:
       return Data.device
   
    @staticmethod
    def get_location() -> dict:
       return Data.location
    
    @staticmethod
    def get_user() -> dict:
        return Data.user
    
    @staticmethod
    def get_broker() -> dict:
        return Data.broker
#----------------------------------------------------------------------------------
    @staticmethod
    def create_base_location() -> Location:
        location = LocationDao.create(
            room=Data.location["common"]["room"],
            adress=Data.location["common"]["adress"]
        )
        Data.device["common"]["location_id"] = location.id
        Data.device["change"]["location_id"] = location.id
        Data.device["to_delete"]["location_id"] = location.id
        return location
    
    @staticmethod
    def create_base_device() -> Device:
        device = DeviceDao.create(
            location_id=Data.device["common"]["location_id"],
            name=Data.device["common"]["name"],
            type=Data.device["common"]["type"],
            topic=Data.device["common"]["topic"]
        )
        Data.device_data["common"]["device_id"] = device.id
        Data.device_data["change"]["device_id"] = device.id
        Data.device_data["to_delete"]["device_id"] = device.id
        Data.broker["common"]["device_id"] = device.id
        Data.broker["change"]["device_id"] = device.id
        return device
    
    @staticmethod
    def create_base_device_data() -> DeviceData:
        device_data = DeviceDataDao.create(
            device_id=Data.device_data["common"]["device_id"],
            secure_status=Data.device_data["common"]["secure_status"],
            temprature=Data.device_data["common"]["temprature"],
            humidity=Data.device_data["common"]["humidity"]
        )
        return device_data
    
    @staticmethod
    def create_base_device_structure() -> dict:
        location = Data.create_base_location()
        device = Data.create_base_device()
        device_data = Data.create_base_device_data()
        return {
            "location": location,
            "device": device,
            "device_data": device_data
        }
        
    @staticmethod
    def create_base_user() -> User:
        user = UserDao.create(
            username=Data.user["common"]["username"],
            password=Data.user["common"]["password"],
            number=Data.user["common"]["number"]
        )
        Data.broker["common"]["user_id"] = user.id
        Data.broker["change"]["user_id"] = user.id
        return user
    
    @staticmethod
    def create_base_broker() -> Brocker:
        broker = BrockerDao.create(
            id_device=Data.broker["common"]["device_id"],
            id_user=Data.broker["common"]["user_id"]
        )
        return broker
    
    @staticmethod
    def create_base_user_broker() -> dict:
        user = Data.create_base_user()
        broker = Data.create_base_broker()
        return {
            "user": user,
            "broker": broker
        }
        
    @staticmethod
    def create_data_base() -> dict:
        device_structure = Data.create_base_device_structure()
        user_broker = Data.create_base_user_broker()
        return {
            "device_structure": device_structure,
            "user_broker": user_broker
        }