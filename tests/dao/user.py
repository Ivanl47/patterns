from app.dao import UserDao
from app.models import User
from .data import Data

class UserTest:
    @staticmethod
    def create_test() -> User:
        user = UserDao.create(
            username=Data.user["to_delete"]["username"],
            password=Data.user["to_delete"]["password"],
            number=Data.user["to_delete"]["number"]
        )
        
        assert user.username == Data.user["to_delete"]["username"]
        assert user.password == Data.user["to_delete"]["password"]
        assert user.number == Data.user["to_delete"]["number"]
        
        Data.broker["to_delete"]["user_id"] = user.id
        return user
    
    @staticmethod
    def search_test(user: User) -> None:
        data = UserDao.get_by_id(user.id)
        assert data is not None
        assert data.id == user.id
        assert data.username == user.username
        assert data.password == user.password
        assert data.number == user.number
    
    @staticmethod
    def update_test(user: User) -> None:
        updated_user = UserDao.update(
            user.id,
            username=Data.user["change"]["username"],
            password=Data.user["change"]["password"],
            number=Data.user["change"]["number"]
        )
        
        assert updated_user is not None
        assert updated_user.id == user.id
        assert updated_user.username == Data.user["change"]["username"]
        assert updated_user.password == Data.user["change"]["password"]
        assert updated_user.number == Data.user["change"]["number"]
    
    @staticmethod
    def delete_test(user: User = None, id: int = -1) -> None:
        if user is not None:
            deleted_user = UserDao.delete(user.id)
            result = UserDao.get_by_id(user.id)
            assert result is None
        else:
            assert id != -1
            assert id > 0
            deleted_user = UserDao.delete(id)
            result = UserDao.get_by_id(id)
            assert result is None
        
        
    
    @staticmethod
    def tests():
        obj = UserTest.create_test()
        assert obj is not None
        UserTest.search_test(obj)
        UserTest.update_test(obj)
        #UserTest.delete_test(obj)