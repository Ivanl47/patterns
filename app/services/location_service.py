from app.dao import LocationDao, DeviceDao
from .device_service import DeviceService
from app.models import Location
from moduls.tools import VariableTools
from moduls.tools import log_def, LogerHelper

class LocationService:
    __name__ = "LocationService"
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all() -> list:
        return LocationDao.get_all()
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_id(location_id: int) -> Location:
        VariableTools.check_id(location_id, "Location")
        location = LocationDao.get_by_id(location_id)
        return location 
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_property(room: str = None, adress: str = None) -> Location:
        VariableTools.one_can_be_not_none(room, adress)
        if VariableTools.check_not_empty_str(room) and VariableTools.check_not_empty_str(adress):
            location = LocationDao.get_by_property(room, adress)
        elif VariableTools.check_not_empty_str(room):
            location = LocationDao.get_by_room(room)
        elif VariableTools.check_not_empty_str(adress):
            location = LocationDao.get_by_adress(adress)
        else:
            location = None
        return location
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def update(location_id: int, room: str = None, adress: str = None) -> None:
        VariableTools.check_id(location_id, "Location")
        VariableTools.one_can_be_not_none(room, adress)
        
        location = LocationDao.get_by_id(location_id)
        
        if location is None:
            raise ValueError("Location not found")
        if room == location.room and adress == location.adress:
            raise ValueError("No changes detected")
        
        room = VariableTools.compare_to_empty_str(location.room, room)
        adress = VariableTools.compare_to_empty_str(location.adress, adress)
        loc_cur = LocationService.get_by_property(room, adress)
        
        if loc_cur is not None and loc_cur.id != location_id:
            raise ValueError("Location already exists")
        
        LocationDao.update(location_id, room, adress)
            
    @log_def(obj_name=__name__) 
    @staticmethod
    def create(room: str = None, adress: str = None) -> Location:
        
        VariableTools.one_can_be_not_none(room, adress)
        room = VariableTools.compare_to_empty_str(room, "N/A")
        adress = VariableTools.compare_to_empty_str(adress, "N/A")
        
        if LocationDao.get_by_property(room, adress):
            raise ValueError("Location already exists")
        return LocationDao.create(room, adress)
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def delete(location_id: int) -> None:
        VariableTools.check_id(location_id, "Location")
        
        location = LocationDao.get_by_id(location_id)
        if location is None:
            raise ValueError("Location not found")
        
        devices = DeviceService.get_by_property(location_id=location_id, all=True)
        if len(devices) > 0:
            for device in devices:
                DeviceService.delete(device.id)
        LocationDao.delete(location_id)

    @log_def(obj_name=__name__)
    @staticmethod
    def to_dict(id: int) -> dict:
        VariableTools.check_id(id, "Location")
        location = LocationService.get_by_id(id)
        if location is None:
            raise ValueError("Location not found")
        
        return {
            "id": location.id,
            "room": location.room,
            "adress": location.adress
        }






