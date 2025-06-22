from app.dao import LocationDao
from app.models import Location
from .data import Data

class LocationTest:
    @staticmethod
    def create_test() -> Location:
        data = Data.get_location()
        location = LocationDao.create(
            room=data["to_delete"]["room"],
            adress=data["to_delete"]["adress"],
        )
        assert location.room == data["to_delete"]["room"]
        assert location.adress == data["to_delete"]["adress"]
        
        return location
    
    @staticmethod
    def search_test(location: Location) -> None:
        data = Data.get_location()
        location = LocationDao.get_by_id(location.id)
        assert location.id == location.id
        assert location.room == location.room
        assert location.adress == location.adress
    
    @staticmethod
    def update_test(location: Location) -> None:
        data = Data.get_location()
        location = LocationDao.update(
            location.id,
            room=data["change"]["room"],
            adress=data["change"]["adress"]
        )
        assert location.id == location.id
        assert location.room == data["change"]["room"]
        assert location.adress == data["change"]["adress"]
    
    @staticmethod
    def delete_test(location: Location) -> None:
        LocationDao.delete(location.id)
        location = LocationDao.get_by_id(location.id)
        assert location is None
    
    @staticmethod
    def tests():
        obj = LocationTest.create_test()
        assert obj is not None
        LocationTest.search_test(obj)
        LocationTest.update_test(obj)
        LocationTest.delete_test(obj)