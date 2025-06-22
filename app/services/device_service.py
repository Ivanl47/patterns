from app.dao import DeviceDao, DeviceDao
from app.models import Device, Device
from .device_data_service import DeviceDataService
from .brocker_service import BrockerService
from moduls.tools import log_def, VariableTools

class DeviceService:
    __name__ = "DeviceService"
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_all() -> list:
        return DeviceDao.get_all()

    @log_def(obj_name=__name__)
    @staticmethod
    def get_by_id(device_id: int) -> Device:
        VariableTools.check_id(device_id)
        device = DeviceDao.get_by_id(device_id)
        return device
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_by_property(
            name: str = None, type: str = None, topic: str = None, location_id: int = None, all: bool = False
        ) -> (Device | list | None):
        VariableTools.one_can_be_not_none(name, type, topic, location_id)
        name_status = VariableTools.check_not_empty_str(name)
        type_status = VariableTools.check_not_empty_str(type)
        topic_status = VariableTools.check_not_empty_str(topic)
        location_id_status = location_id is not None
        if location_id_status:
            VariableTools.check_id(location_id)

        if name_status and type_status and topic_status and location_id_status:
            if all:
                data = DeviceDao.get_all_by_property(name, type, topic, location_id)
            else:
                data = DeviceDao.get_by_property(name, type, topic, location_id)
        elif not name_status and type_status and topic_status and location_id_status:
            if all:
                data = DeviceDao.get_all_by_property_without_name(type, topic, location_id)
            else:
                data = DeviceDao.get_by_property_without_name(type, topic, location_id) 
        elif name_status and not type_status and topic_status and location_id_status:
            if all:
                data = DeviceDao.get_all_by_property_without_type(name, topic, location_id)
            else:
                data = DeviceDao.get_by_property_without_type(name, topic, location_id)
        elif name_status and type_status and not topic_status and location_id_status:
            if all:
                data = DeviceDao.get_all_by_property_without_topic(name, type, location_id)
            else:
                data = DeviceDao.get_by_property_without_topic(name, type, location_id)
        elif name_status and type_status and topic_status and not location_id_status:
            if all:
                data = DeviceDao.get_all_by_property_without_location(name, type, topic)
            else:
                data = DeviceDao.get_by_property_without_location(name, type, topic)
        elif name_status and type_status and not topic_status and not location_id_status:
            if all:
                data = DeviceDao.get_all_by_name_and_type(name, type)
            else:
                data = DeviceDao.get_by_name_and_type(name, type)
        elif name_status and not type_status and topic_status and not location_id_status:
            if all:
                data = DeviceDao.get_all_by_name_and_topic(name, topic)
            else:
                data = DeviceDao.get_by_name_and_topic(name, topic)
        elif not name_status and type_status and topic_status and not location_id_status:
            if all:
                data = DeviceDao.get_all_by_type_and_topic(type, topic)
            else:
                data = DeviceDao.get_by_type_and_topic(type, topic)
        elif name_status and not type_status and not topic_status and location_id_status:
            if all:
                data = DeviceDao.get_all_by_name_and_location(name, location_id)
            else:
                data = DeviceDao.get_by_name_and_location(name, location_id)
        elif not name_status and type_status and not topic_status and location_id_status:
            if all:
                data = DeviceDao.get_all_by_type_and_location(type, location_id)
            else:
                data = DeviceDao.get_by_type_and_location(type, location_id)
        elif not name_status and not type_status and topic_status and location_id_status:
            if all:
                data = DeviceDao.get_all_by_topic_and_location(topic, location_id)
            else:
                data = DeviceDao.get_by_topic_and_location(topic, location_id)
        elif name_status and not type_status and not topic_status and not location_id_status:
            if all:
                data = DeviceDao.get_all_by_name(name)
            else:
                data = DeviceDao.get_by_name(name)
        elif not name_status and type_status and not topic_status and not location_id_status:
            if all:
                data = DeviceDao.get_all_by_type(type)
            else:
                data = DeviceDao.get_by_type(type)
        elif not name_status and not type_status and topic_status and not location_id_status:
            if all:
                data = DeviceDao.get_all_by_topic(topic)
            else:
                data = DeviceDao.get_by_topic(topic)   
        elif not name_status and not type_status and not topic_status and location_id_status:
            if all:
                data = DeviceDao.get_all_by_location(location_id)
            else:
                data = DeviceDao.get_by_location(location_id)
        else:
            return None
        return data

    @log_def(obj_name=__name__)
    @staticmethod
    def create(name: str, type: str, topic: str, location_id: int) -> Device:
        VariableTools.no_one_can_be_none(name, type, topic, location_id)
        if DeviceService.get_by_property(name, type, topic):
            raise ValueError("Device already exists")
        return DeviceDao.create(name, type, topic, location_id)

    @log_def(obj_name=__name__)
    @staticmethod
    def update(
        device_id: int,
        name: str = None,
        type: str = None,
        topic: str = None,
        location_id: int = None
    ) -> None:
        VariableTools.check_id(device_id, "Device")
        device = DeviceDao.get_by_id(device_id)
        
        if device is None:
            raise ValueError("Device not found")
        
        if name == device.name and type == device.type and topic == device.topic:
            raise ValueError("No changes detected")
        if DeviceService.get_by_property(name, type, topic, location_id):
            raise ValueError("Device already exists")
        
        name = VariableTools.compare_to_empty_str(device.name, name)
        type = VariableTools.compare_to_empty_str(device.type, type)
        topic = VariableTools.compare_to_empty_str(device.topic, topic)
        location_id = VariableTools.compare_to_empty_str(device.location_id, location_id)
        
        DeviceDao.update(device_id, name, type, topic, location_id)

    @log_def(obj_name=__name__)
    @staticmethod
    def delete(device_id: int, device: Device = None) -> None:
        VariableTools.check_id(device_id, "Device")
        device = DeviceDao.get_by_id(device_id)
        if device is None:
            raise ValueError("Device not found")
        
        data = DeviceDataService.get_all_by_device_id(device_id)
        brocker = BrockerService.get_all_by_property(id_device=device_id)
        
        if data is not None:
            for d in data:
                DeviceDataService.delete(d.id)
                
        if brocker is not None:
            for b in brocker:
                BrockerService.delete(b.id)
        
        DeviceDao.delete(device_id)
        
    @log_def(obj_name=__name__)
    @staticmethod
    def to_dict(id: int) -> dict:
        VariableTools.check_id(id, "Device")
        device = DeviceService.get_by_id(id)
        if device is None:
            raise ValueError("Device not found")
        
        return {
            "id": device.id,
            "name": device.name,
            "type": device.type,
            "topic": device.topic,
            "location_id": device.location_id
        }
