from app import db
from app.models import Device, DeviceData, Location
from moduls.tools import log_def, LogerHelper

class DeviceDao:
    __name__ = "DeviceDao"
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_id(device_id: int) -> Device: 
        return db.session.query(Device).filter(Device.id == device_id).first()

    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all() -> list:
        return db.session.query(Device).all()
    #################################################################################
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_property(name: str, type: str, topic: str, location_id: int) -> Device:
        device = Device.query.filter_by(
            name=name, type=type, topic=topic, location_id=location_id
            ).first()
        return device
    #################################################################################
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_property_without_name(type: str, topic: str, location_id: int) -> Device:
        device = Device.query.filter_by(
            type=type, topic=topic, location_id=location_id
            ).first()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_property_without_name(type: str, topic: str, location_id: int) -> list:
        device = Device.query.filter_by(
            type=type, topic=topic, location_id=location_id
            ).all()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_property_without_type(name: str, topic: str, location_id: int) -> Device:
        device = Device.query.filter_by(
            name=name, topic=topic, location_id=location_id
            ).first()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_property_without_type(name: str, topic: str, location_id: int) -> list:
        device = Device.query.filter_by(
            name=name, topic=topic, location_id=location_id
            ).all()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_property_without_topic(name: str, type: str, location_id: int) -> Device:
        device = Device.query.filter_by(
            name=name, type=type, location_id=location_id
            ).first()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_property_without_topic(name: str, type: str, location_id: int) -> list:
        device = Device.query.filter_by(
            name=name, type=type, location_id=location_id
            ).all()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_property_without_location(name: str, type: str, topic: str) -> Device:
        device = Device.query.filter_by(
            name=name, type=type, topic=topic
            ).first()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_property_without_location(name: str, type: str, topic: str) -> list:
        device = Device.query.filter_by(
            name=name, type=type, topic=topic
            ).all()
        return device
    #################################################################################
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_name_and_type(name: str, type: str) -> Device:
        device = Device.query.filter_by(name=name, type=type).first()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_name_and_type(name: str, type: str) -> list:
        device = Device.query.filter_by(name=name, type=type).all()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_name_and_topic(name: str, topic: str) -> Device:
        device = Device.query.filter_by(name=name, topic=topic).first()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_name_and_topic(name: str, topic: str) -> list:
        device = Device.query.filter_by(name=name, topic=topic).all()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_type_and_topic(type: str, topic: str) -> Device:
        device = Device.query.filter_by(type=type, topic=topic).first()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_type_and_topic(type: str, topic: str) -> list:
        device = Device.query.filter_by(type=type, topic=topic).all()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_name_and_location(name: str, location_id: int) -> Device:
        device = Device.query.filter_by(name=name, location_id=location_id).first()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_name_and_location(name: str, location_id: int) -> list:
        device = Device.query.filter_by(name=name, location_id=location_id).all()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_type_and_location(type: str, location_id: int) -> Device:
        device = Device.query.filter_by(type=type, location_id=location_id).first()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_type_and_location(type: str, location_id: int) -> list:
        device = Device.query.filter_by(type=type, location_id=location_id).all()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_topic_and_location(topic: str, location_id: int) -> Device:
        device = Device.query.filter_by(topic=topic, location_id=location_id).first()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_topic_and_location(topic: str, location_id: int) -> list:
        device = Device.query.filter_by(topic=topic, location_id=location_id).all()
        return device
    
    #################################################################################
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_name(name: str) -> Device:
        device = Device.query.filter_by(name=name).first()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_name(name: str) -> list:
        device = Device.query.filter_by(name=name).all()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_type(type: str) -> Device:
        device = Device.query.filter_by(type=type).first()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_type(type: str) -> list:
        device = Device.query.filter_by(type=type).all()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_topic(topic: str) -> Device:
        device = Device.query.filter_by(topic=topic).first()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_topic(topic: str) -> list:
        device = Device.query.filter_by(topic=topic).all()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_location(location_id: int) -> Device:
        device = Device.query.filter_by(location_id=location_id).first()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_location(location_id: int) -> list:
        device = Device.query.filter_by(location_id=location_id).all()
        return device
    #################################################################################
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def create(
        name: str,
        type: str,
        topic: str,
        location_id: int
        ) -> Device:
        
        device = Device(
            name=name,
            type=type,
            topic=topic,
            location_id=location_id
        )
        db.session.add(device)
        db.session.commit()
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def update(
        device_id: int,
        name: str,
        type: str,
        topic: str,
        location_id: int
        ) -> Device:
        device = DeviceDao.get_by_id(device_id)
        device.name = name
        device.type = type
        device.topic = topic
        device.location_id = location_id
        db.session.commit()
        
        return device
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def delete(device_id):
        device = DeviceDao.get_by_id(device_id)
        if device:
            db.session.delete(device)
            db.session.commit()