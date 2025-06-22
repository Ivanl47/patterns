from flask import Blueprint, request, jsonify
from app.services.device_service import DeviceService

device_router = Blueprint('device_router', __name__)

@device_router.route('/devices', methods=['GET'])
def get_all_devices():
    return jsonify([DeviceService.to_dict(device.id) for device in DeviceService.get_all()])

@device_router.route('/devices/<int:device_id>', methods=['GET'])
def get_device_by_id(device_id):
    return jsonify(DeviceService.to_dict(device_id))

@device_router.route('/devices', methods=['POST'])
def create_device():
    data = request.json
    device = DeviceService.create(data['name'], data['type'], data['topic'], data['location_id'])
    return jsonify(DeviceService.to_dict(device.id))

@device_router.route('/devices/<int:device_id>', methods=['PUT'])
def update_device(device_id):
    data = request.json
    DeviceService.update(device_id, data['name'], data['type'], data['topic'], int(data['location_id']))
    return jsonify({'message': 'Device updated successfully'})

@device_router.route('/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    DeviceService.delete(device_id)
    return jsonify({'message': 'Device deleted successfully'})
