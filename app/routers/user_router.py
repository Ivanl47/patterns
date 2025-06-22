from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

user_router = Blueprint('user_router', __name__)

@user_router.route('/users', methods=['GET'])
def get_all_users():
    return jsonify([UserService.to_dict(user.id) for user in UserService.get_all()])

@user_router.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    return jsonify(UserService.to_dict(user_id))

@user_router.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = UserService.create(data['username'], data['password'], data['number'])
    return jsonify(UserService.to_dict(user.id))

@user_router.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    UserService.update(user_id, data.get('username'), data.get('password'), data.get('number'))
    return jsonify({'message': 'User updated successfully'})

@user_router.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    UserService.delete(user_id)
    return jsonify({'message': 'User deleted successfully'})
