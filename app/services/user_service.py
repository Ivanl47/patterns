from app.models import User
from app.dao import UserDao
from .brocker_service import BrockerService
from moduls.tools import VariableTools, log_def

class UserService:
    __name__ = "UserService"
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_all() -> list:
        return UserDao.get_all()
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_by_id(user_id: int) -> User:
        VariableTools.check_id(user_id, "User")
        return UserDao.get_by_id(user_id)
    
    @log_def(obj_name=__name__)
    @staticmethod
    def get_by_property(username: str = None, number: str = None) -> list:
        data = UserService.get_all()
        if username and number:
            return [user for user in data if user.username == username and user.number == number]
        elif username:
            return [user for user in data if user.username == username]
        elif number:
            return [user for user in data if user.number == number]
        else:
            return data
        
    @log_def(obj_name=__name__)
    @staticmethod
    def aut_for_user(username: str, password: str) -> bool:
        VariableTools.no_one_can_be_none(username, password)
        user = UserDao.get_by_username(username)
        if not user or user.password != password:
            return False
        return True
    
    @log_def(obj_name=__name__)
    @staticmethod
    def aut_for_number(number: str, password: str) -> bool:
        VariableTools.no_one_can_be_none(number, password)
        user = UserService.get_by_property(number=number)
        if not user or user.password != password:
            return False
        return True
    
    @log_def(obj_name=__name__)
    @staticmethod
    def create(username: str, password: str, number: str) -> User:
        VariableTools.no_one_can_be_none(username, password, number)
        if UserService.get_by_property(username=username, number=number):
            raise ValueError("User with this username and number already exists")
        
        user = UserDao.create(username=username, password=password, number=number)
        return user
        
    @log_def(obj_name=__name__)
    @staticmethod
    def update(user_id: int, username: str = None, password: str = None, number: str = None) -> None:
        VariableTools.check_id(user_id, "User")
        VariableTools.one_can_be_not_none(username, password, number)
        
        user = UserService.get_by_id(user_id)
        if not user:
            raise ValueError("User with this ID does not exist")

        username = VariableTools.compare_to_empty_str(user.username, username)
        password = VariableTools.compare_to_empty_str(user.password, password)
        number = VariableTools.compare_to_empty_str(user.number, number)

        if UserService.get_by_property(username=username, number=number):
            raise ValueError("User with this username or number already exists")
        
        UserDao.update(user_id=user_id, username=username, password=password, number=number)

    @log_def(obj_name=__name__)
    @staticmethod
    def delete(user_id: int) -> None:
        VariableTools.check_id(user_id, "User")
        
        data = UserService.get_by_id(user_id)
        if not data:
            raise ValueError("User with this ID does not exist")
        
        brockers = BrockerService.get_by_property(id_user=user_id)
        if brockers:
            for brocker in brockers:
                BrockerService.delete(brocker.id)
                
        UserDao.delete(user_id)
        
    @log_def(obj_name=__name__)
    @staticmethod
    def to_dict(id: int) -> dict:
        VariableTools.check_id(id, "User")
        user = UserService.get_by_id(id)
        if not user:
            raise ValueError("User with this ID does not exist")
        
        return {
            "id": user.id,
            "username": user.username,
            "number": user.number
        }
