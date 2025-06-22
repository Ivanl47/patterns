from flask import Blueprint, request, jsonify
from app.services.device_data_service import DeviceDataService

device_data_router = Blueprint('device_data_router', __name__)

@device_data_router.route('/device-data', methods=['GET'])
def get_all_device_data():
    return jsonify([DeviceDataService.to_dict(device_data.id) for device_data in DeviceDataService.get_all()])

@device_data_router.route('/device-data/<int:device_data_id>', methods=['GET'])
def get_device_data_by_id(device_data_id):
    return jsonify(DeviceDataService.to_dict(device_data_id))

@device_data_router.route('/device-data', methods=['POST'])
def create_device_data():
    data = request.json
    device_data = DeviceDataService.create(data['device_id'], data.get('secure_status'), data.get('temprature'), data.get('humidity'))
    return jsonify(DeviceDataService.to_dict(device_data.id))

@device_data_router.route('/device-data/<int:device_data_id>', methods=['PUT'])
def update_device_data(device_data_id):
    data = request.json
    DeviceDataService.update(device_data_id, data.get('device_id'), data.get('secure_status'), data.get('temprature'), data.get('humidity'))
    return jsonify({'message': 'Device data updated successfully'})

@device_data_router.route('/device-data/<int:device_data_id>', methods=['DELETE'])
def delete_device_data(device_data_id):
    DeviceDataService.delete(device_data_id)
    return jsonify({'message': 'Device data deleted successfully'})
