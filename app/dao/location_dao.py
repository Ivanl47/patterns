from app import db
from app.models import Location
from moduls.tools import log_def, LogerHelper


class LocationDao:
    __name__ = "LocationDao"
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all() -> list:
        return Location.query.all()

    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_id(location_id: int) -> Location:
        location = Location.query.get(location_id)
        return location

    @log_def(obj_name=__name__) 
    @staticmethod
    def create(room: str, adress: str) -> Location:
        new_location = Location(room=room, adress=adress)
        db.session.add(new_location)
        db.session.commit()
        return new_location

    @log_def(obj_name=__name__) 
    @staticmethod
    def update(location_id: int, room: str, adress: str) -> Location:
        location = LocationDao.get_by_id(location_id)
        location.room = room
        location.adress = adress
        db.session.commit()
        return location
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_property(room: str, adress: str) -> Location:
        location = Location.query.filter_by(room=room, adress=adress).first()
        return location
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_room(room: str) -> list:
        location = Location.query.filter_by(room=room).first()
        return location
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_by_adress(adress: str) -> Location:
        location = Location.query.filter_by(adress=adress).first()
        return location
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_room(room: str) -> list:
        location = Location.query.filter_by(room=room).all()
        return location
    
    @log_def(obj_name=__name__) 
    @staticmethod
    def get_all_by_adress(adress: str) -> list:
        location = Location.query.filter_by(adress=adress).all()
        return location

    @log_def(obj_name=__name__) 
    @staticmethod
    def delete(location_id: int) -> bool:
        location = LocationDao.get_by_id(location_id)
        db.session.delete(location)
        db.session.commit()
        return True