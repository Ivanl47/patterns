from app import db
from app.models import Brocker

class BrockerDao:
    @staticmethod
    def get_all() -> list:
        return Brocker.query.all()
    
    @staticmethod
    def get_by_id(broker_server_id: int) -> Brocker:
        return Brocker.query.get(broker_server_id)
    
    @staticmethod
    def get_by_property(id_device: int = None, id_user: int = None) -> (Brocker | list | None):
        if id_device is not None and id_user is not None:
            broker_server = Brocker.query.filter_by(id_device=id_device, id_user=id_user).first()
        elif id_device is not None:
            broker_server = Brocker.query.filter_by(id_device=id_device).all()
        elif id_user is not None:
            broker_server = Brocker.query.filter_by(id_user=id_user).all()
        else:
            broker_server = None
            
        return broker_server
             
    @staticmethod
    def update(
        broker_server_id: int,
        id_device: int,
        id_user: int
    ) -> Brocker:
        broker_server = BrockerDao.get_by_id(broker_server_id)
        broker_server.id_device = id_device
        broker_server.id_user = id_user
            
        db.session.commit()
        return broker_server
    
    @staticmethod
    def create(id_device: int = None, id_user: int = None) -> Brocker:
        broker_server = Brocker(
            id_device=id_device,
            id_user=id_user
        )
        db.session.add(broker_server)
        db.session.commit()
        return broker_server
    
    @staticmethod
    def delete(broker_server_id: int) -> None:
        broker_server = BrockerDao.get_by_id(broker_server_id)
        db.session.delete(broker_server)
        db.session.commit()