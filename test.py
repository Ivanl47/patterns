from app import create_app, db
from tests import Data, DeviceDataTest, DeviceTest, LocationTest, UserTest, BrockerTest
from app.services import DeviceService, LocationService, DeviceDataService, UserService, BrockerService

from tests import SetupTables, URDTables
from app.busineslogic import UserActivity


app = create_app()

with app.app_context():
    db.drop_all()
    print("All tables dropped!")
    
app = create_app()

def prepare_test_environment():
    with app.app_context():
        Data.create_data_base()

def test_device_part_dao():
    with app.app_context():
        DeviceDataTest.tests()
        DeviceTest.tests()
        LocationTest.tests()
        UserTest.tests()
        BrockerTest.tests()
        UserTest.delete_test(id = Data.get_broker()["to_delete"]["user_id"])
        
    
def test_device_service():
    with app.app_context():
        UserActivity.set_data_from_csv(
            "D:\\Desktop\\patterns\\Patter-API\\test_data.csv"
            )
        # SetupTables.Base_Location_Services()
        # locations = LocationService.get_all()
        # SetupTables.Base_Device_Services(locations)
        # devices = DeviceService.get_all()
        # SetupTables.Base_DeviceData_Services(devices)
        # SetupTables.Base_User_Services()
        # SetupTables.Base_Brocker_Services()
        
        # URDTables.Test_DeviceData_Services()
        # URDTables.Test_User_Services()
        # URDTables.Test_Brocker_Services()
        
        # # BaseLocationTablesServices()
        # list_locations = LocationService.get_all()
        # # BaseDeviceTablesServices(list_locations)
        # list_devices = DeviceService.get_all()
        # BaseDeviceDataTablesServices(list_devices)
        
        
        
        # Device_test_service() 
        # DeviceData_test_service()
               
        # pass
        
if __name__ == '__main__':
    # prepare_test_environment()
    test_device_service()
    # test_device_part_dao()
    

