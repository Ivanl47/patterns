from app.dao import DeviceDao
from app.models import Device
from .data import Data

class DeviceTest:
    @staticmethod
    def create_test() -> Device:
        data = Data.get_device()
        device = DeviceDao.create(
            name=data["to_delete"]["name"],
            type=data["to_delete"]["type"],
            topic=data["to_delete"]["topic"],
            location_id=data["to_delete"]["location_id"]
        )
        assert device.name == data["to_delete"]["name"]
        assert device.type == data["to_delete"]["type"]
        assert device.topic == data["to_delete"]["topic"]
        assert device.location_id == data["to_delete"]["location_id"]
        
        return device
    
    @staticmethod
    def search_test(device: Device) -> None:
        data = Data.get_device()
        device = DeviceDao.get_by_id(device.id)
        assert device.id == device.id
        assert device.name == device.name
        assert device.type == device.type
        assert device.topic == device.topic
        assert device.location_id == device.location_id
    
    @staticmethod
    def update_test(device: Device) -> None:
        data = Data.get_device()
        device = DeviceDao.update(
            device.id,
            name=data["change"]["name"],
            type=data["change"]["type"],
            topic=data["change"]["topic"],
            location_id=data["change"]["location_id"]
        )
        assert device.id == device.id
        assert device.name == data["change"]["name"]
        assert device.type == data["change"]["type"]
        assert device.topic == data["change"]["topic"]
        assert device.location_id == data["change"]["location_id"]
    
    @staticmethod
    def delete_test(device: Device) -> None:
        DeviceDao.delete(device.id)
        device = DeviceDao.get_by_id(device.id)
        assert device is None
    
    @staticmethod
    def tests():
        obj = DeviceTest.create_test()
        assert obj is not None
        DeviceTest.search_test(obj)
        DeviceTest.update_test(obj)
        DeviceTest.delete_test(obj)
