from app.dao import DeviceDataDao
from app.models import DeviceData
from .data import Data

class DeviceDataTest:
    
    @staticmethod
    def create_test() -> DeviceData:
        data = Data.get_device_data()
        device = DeviceDataDao.create(
            device_id=data["to_delete"]["device_id"],
            secure_status=data["to_delete"]["secure_status"],
            temprature=data["to_delete"]["temprature"],
            humidity=data["to_delete"]["humidity"]
        )
        assert device.device_id == data["to_delete"]["device_id"]
        assert device.secure_status == data["to_delete"]["secure_status"]
        assert device.temprature == data["to_delete"]["temprature"]
        assert device.humidity == data["to_delete"]["humidity"]
        assert device.time is not None
        
        return device
    
    @staticmethod
    def search_test(device_data: DeviceData) -> None:
        data = Data.get_device_data()
        device = DeviceDataDao.get_by_id(device_data.id)
        assert device.id == device_data.id
        assert device.device_id == device_data.device_id
        assert device.secure_status == device_data.secure_status
        assert device.temprature == device_data.temprature
        assert device.humidity == device_data.humidity
        assert device.time == device_data.time
        
    @staticmethod
    def update_test(device_data: DeviceData) -> None:
        data = Data.get_device_data()
        device = DeviceDataDao.update(
            device_data.id,
            device_id=data["change"]["device_id"],
            secure_status=data["change"]["secure_status"],
            temprature=data["change"]["temprature"],
            humidity=data["change"]["humidity"]
        )
        assert device.id == device_data.id
        assert device.device_id == data["change"]["device_id"]
        assert device.secure_status == data["change"]["secure_status"]
        assert device.temprature == data["change"]["temprature"]
        assert device.humidity == data["change"]["humidity"]
        
    @staticmethod
    def delete_test(device_data: DeviceData) -> None:
        DeviceDataDao.delete(device_data.id)
        device = DeviceDataDao.get_by_id(device_data.id)
        assert device is None
    
    @staticmethod
    def tests():
        obj = DeviceDataTest.create_test()
        assert obj is not None
        DeviceDataTest.search_test(obj)
        DeviceDataTest.update_test(obj)
        DeviceDataTest.delete_test(obj)
        
