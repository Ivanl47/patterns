from app.models import DeviceData
from app.dao import DeviceDataDao
from moduls.tools import VariableTools, log_def

class DeviceDataService:
    __name__ = "DeviceDataService"
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_all() -> list:
        return DeviceDataDao.get_all()

    @log_def(obj_name=__name__)
    @staticmethod
    def get_by_id(device_data_id: int) -> DeviceData:
        
        device_data = DeviceDataDao.get_by_id(device_data_id)
        return device_data

    @log_def(obj_name=__name__)
    @staticmethod
    def create(device_id: int, 
        secure_status: bool = False,
        temprature: float = -999.0,
        humidity: float = -999.0
    ) -> DeviceData:
        VariableTools.check_id(device_id, "DeviceData")
        VariableTools.one_can_be_not_none(secure_status, temprature, humidity)
        VariableTools.least_must_be_not_none_float(temprature, humidity)
        device_data = DeviceDataDao.create(device_id, secure_status, temprature, humidity)
        return device_data
        
    @log_def(obj_name=__name__)
    @staticmethod
    def update(
        device_data_id: int,
        device_id: int = None,
        secure_status: bool = None,
        temprature: float = None,
        humidity: float = None
    ) -> DeviceData:
        VariableTools.check_id(device_data_id, "DeviceData")
        data = DeviceDataDao.get_by_id(device_data_id)
        VariableTools.least_must_be_not_none(
            device_id, secure_status, temprature, humidity
        )
        if device_id is not None:
            VariableTools.check_id(device_id, "Device")
        device_id = VariableTools.compare_to_empty_int(data.device_id, device_id)
        secure_status = VariableTools.compare_to_empty_bool(data.secure_status, secure_status)
        temprature = VariableTools.compare_to_empty_float(data.temprature, temprature)
        humidity = VariableTools.compare_to_empty_float(data.humidity, humidity)
        
        
        DeviceDataDao.update(
            device_data_id,
            device_id=device_id,
            secure_status=secure_status,
            temprature=temprature,
            humidity=humidity
        )
        
    @log_def(obj_name=__name__)
    @staticmethod
    def get_all_by_device_id(device_id: int) -> list:
        VariableTools.check_id(device_id, "Device")
        device_data = DeviceDataDao.get_all()
        
        if device_data is None:
            raise ValueError("Device data not found")
        result = [data for data in device_data if data.device_id == device_id]
        return result
    
    @log_def(obj_name=__name__)
    @staticmethod
    def delete(device_data_id: int) -> None:
        VariableTools.check_id(device_data_id, "DeviceData")
        device_data = DeviceDataDao.get_by_id(device_data_id)
        
        if device_data is None:
            raise ValueError("Device data not found")
        
        DeviceDataDao.delete(device_data.id)
        
    @log_def(obj_name=__name__)
    @staticmethod
    def to_dict(id: int) -> dict:
        VariableTools.check_id(id, "DeviceData")
        device_data = DeviceDataService.get_by_id(id)
        
        if device_data is None:
            raise ValueError("Device data not found")
        
        return {
            "id": device_data.id,
            "device_id": device_data.device_id,
            "secure_status": device_data.secure_status,
            "temprature": device_data.temprature,
            "humidity": device_data.humidity
        }
    