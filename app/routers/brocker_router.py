from flask import Blueprint, request, jsonify
from app.services import BrockerService, DeviceDataService, DeviceService, UserService
from app.busineslogic import UserActivity

brocker_router = Blueprint('brocker_router', __name__)

@brocker_router.route('/brockers', methods=['GET'])
def get_all_brockers():
    return jsonify([BrockerService.to_dict(brocker.id) for brocker in BrockerService.get_all()])

@brocker_router.route('/brockers/<int:brocker_id>', methods=['GET'])
def get_brocker_by_id(brocker_id):
    return jsonify(BrockerService.to_dict(brocker_id))

@brocker_router.route('/brockers', methods=['POST'])
def create_brocker():
    data = request.json
    brocker = BrockerService.create(data['id_device'], data['id_user'])
    return jsonify(BrockerService.to_dict(brocker.id))

@brocker_router.route('/brockers/<int:brocker_id>', methods=['PUT'])
def update_brocker(brocker_id):
    data = request.json
    BrockerService.update(brocker_id, data.get('id_device'), data.get('id_user'))
    return jsonify({'message': 'Brocker updated successfully'})

@brocker_router.route('/brockers/<int:brocker_id>', methods=['DELETE'])
def delete_brocker(brocker_id):
    BrockerService.delete(brocker_id)
    return jsonify({'message': 'Brocker deleted successfully'})

@brocker_router.route('/brockers/getdata/<int:location_id>', methods=['GET'])
def get_by_location(location_id):
    data = UserActivity.get_all_data_in_location(location_id)
    print(data)
    return jsonify([DeviceDataService.to_dict(device_data.id) for device_data in data])
    
@brocker_router.route('/brockers/getuser/<int:user_id>', methods=['GET'])
def get_device_by_user(user_id):
    data = UserActivity.get_device_by_user(user_id)
    return jsonify([DeviceService.to_dict(device.id) for device in data])

@brocker_router.route('/brockers/getmiddle/<int:location_id>', methods=['GET'])
def get_middle_data(location_id):
    data = UserActivity.get_middle_data_in_location(location_id)
    return jsonify(data)

@brocker_router.route('/brockers/aut', methods=['PUT'])
def get_aut():
    data = request.json
    status = UserActivity.autorize_user(username=data['username'], password=data['password'])
    if not status:
        return jsonify({'error': 'Authorization failed'}), 401
    user = UserService.get_by_property(username=data['username'])[0]
    result = {'id': user.id}
    return jsonify(result)

@brocker_router.route('/brockers/addDevice', methods=['PUT'])
def add_device():
    data = request.json
    print(data['device_id'], data['user_id'])
    status = BrockerService.create(id_user=data['user_id'], id_device=data['device_id'])
    if not status:
        return jsonify({'error': 'Failed to add device'}), 400
    return jsonify({'message': 'Device added successfully'})