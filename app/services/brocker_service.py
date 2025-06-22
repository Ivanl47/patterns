from app.models import Brocker
from app.dao import BrockerDao, UserDao, DeviceDao, LocationDao, DeviceDataDao
from moduls.tools import log_def, VariableTools
# from .user_service import UserService
# from .device_service import DeviceService

class BrockerService:
    __name__ = "BrockerService"
    
    @log_def(obj_name=__name__)
    @staticmethod
    def create(id_device: int, id_user: int) -> Brocker:
        VariableTools.check_id(id_device, "Device")
        VariableTools.check_id(id_user, "User")
        user = UserDao.get_by_id(id_user)
        device = DeviceDao.get_by_id(id_device)
        
        if not device:
            raise ValueError(f"Device with id {id_device} does not exist.")
        if not user:
            raise ValueError(f"User with id {id_user} does not exist.")
        
        brocker = BrockerDao.create(id_device, id_user)
        return brocker
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_all() -> list[Brocker]:
        return BrockerDao.get_all()
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_by_id(id: int) -> Brocker:
        VariableTools.check_id(id, "Brocker")
        return BrockerDao.get_by_id(id)
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_by_property(id_device: int = None, id_user: int = None) -> Brocker:
        return BrockerDao.get_by_property(id_device, id_user)
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_all_by_property(id_device: int = None, id_user: int = None) -> (Brocker | list | None):
        data = BrockerDao.get_all()
        if id_device is not None and id_user is not None:
            return BrockerDao.get_by_property(id_device, id_user)
        elif id_device is not None:
            return [item for item in data if item.id_device == id_device]
        elif id_user is not None:
            return [item for item in data if item.id_user == id_user]
        else:
            return data
    
    @log_def(obj_name=__name__)
    @staticmethod
    def update(id: int, id_device: int = None, id_user: int = None) -> None:
        VariableTools.check_id(id, "Brocker")
        
        brocker = BrockerDao.get_by_id(id)
        id_device = VariableTools.compare_to_empty_int(brocker.id_device, id_device)
        id_user = VariableTools.compare_to_empty_int(brocker.id_user, id_user)
        
        user = UserDao.get_by_id(id_user)
        device = DeviceDao.get_by_id(id_device)
        
        if not brocker:
            raise ValueError(f"Brocker with id {id} does not exist.")
        if not device:
            raise ValueError(f"Device with id {id_device} does not exist.")
        if not user:
            raise ValueError(f"User with id {id_user} does not exist.")
        
        brocker = BrockerDao.update(id, id_device, id_user)
    
    @log_def(obj_name=__name__)
    @staticmethod
    def delete(id: int) -> None:
        VariableTools.check_id(id, "Brocker")
        brocker = BrockerService.get_by_id(id)
        if not brocker:
            raise ValueError(f"Brocker with id {id} does not exist.")
        
        BrockerDao.delete(id)
        
    @log_def(obj_name=__name__)
    @staticmethod
    def to_dict(id: int) -> dict:
        VariableTools.check_id(id, "Brocker")
        brocker = BrockerDao.get_by_id(id)
        if not brocker:
            raise ValueError(f"Brocker with id {id} does not exist.")
        
        return {
            "id": brocker.id,
            "id_device": brocker.id_device,
            "id_user": brocker.id_user
        }
   