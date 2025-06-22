from app import create_app, db
import pymysql
print("pymysql imported")

app = create_app()

from app.routers.user_router import user_router
from app.routers.location_router import location_router
from app.routers.device_router import device_router
from app.routers.device_data_router import device_data_router
from app.routers.brocker_router import brocker_router

# Register blueprints
app.register_blueprint(user_router, url_prefix='/api')
app.register_blueprint(location_router, url_prefix='/api')
app.register_blueprint(device_router, url_prefix='/api')
app.register_blueprint(device_data_router, url_prefix='/api')
app.register_blueprint(brocker_router, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True)