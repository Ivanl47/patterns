from app.dao import BrockerDao
from app.models import Brocker
from .data import Data

class BrockerTest:
    @staticmethod
    def create_test() -> Brocker:
        data = Data.get_broker()
        broker = BrockerDao.create(
            id_device=data["common"]["device_id"],
            id_user=data["common"]["user_id"]
        )
        assert broker.id_device == data["common"]["device_id"]
        assert broker.id_user == data["common"]["user_id"]
        
        return broker
    
    @staticmethod
    def search_test(broker: Brocker) -> None:
        data = BrockerDao.get_by_id(broker.id)
        assert data is not None
        assert data.id == broker.id
        assert data.id_device == broker.id_device
        assert data.id_user == broker.id_user
    
    @staticmethod
    def update_test(broker: Brocker) -> None:
        updated_broker = BrockerDao.update(
            broker.id,
            id_device=Data.broker["change"]["device_id"],
            id_user=Data.broker["change"]["user_id"]
        )
        
        assert updated_broker is not None
        assert updated_broker.id == broker.id
        assert updated_broker.id_device == Data.broker["change"]["device_id"]
        assert updated_broker.id_user == Data.broker["change"]["user_id"]
    
    @staticmethod
    def delete_test(broker: Brocker) -> None:
        deleted_broker = BrockerDao.delete(broker.id)
        result = BrockerDao.get_by_id(broker.id)
        assert result is None
    
    @staticmethod
    def tests():
        obj = BrockerTest.create_test()
        assert obj is not None
        BrockerTest.search_test(obj)
        BrockerTest.update_test(obj)
        BrockerTest.delete_test(obj)