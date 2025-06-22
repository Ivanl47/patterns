from flask import Blueprint, request, jsonify
from app.services.location_service import LocationService

location_router = Blueprint('location_router', __name__)

@location_router.route('/locations', methods=['GET'])
def get_all_locations():
    return jsonify([LocationService.to_dict(loc.id) for loc in LocationService.get_all()])

@location_router.route('/locations/<int:location_id>', methods=['GET'])
def get_location_by_id(location_id):
    return jsonify(LocationService.to_dict(location_id))

@location_router.route('/locations', methods=['POST'])
def create_location():
    data = request.json
    location = LocationService.create(data.get('room'), data.get('adress'))
    return jsonify(LocationService.to_dict(location.id))

@location_router.route('/locations/<int:location_id>', methods=['PUT'])
def update_location(location_id):
    data = request.json
    LocationService.update(location_id, data.get('room'), data.get('adress'))
    return jsonify({'message': 'Location updated successfully'})

@location_router.route('/locations/<int:location_id>', methods=['DELETE'])
def delete_location(location_id):
    LocationService.delete(location_id)
    return jsonify({'message': 'Location deleted successfully'})
