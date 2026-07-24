
def create_flask_server():
    from flask import Flask

    init_app = Flask(__name__)

    from config import configurations
    init_app.config.from_object(configurations)

    from models import db, user_datastore
    # db = SQLAlchemy(app)
    db.init_app(init_app)

    from routes.about import about_bp
    init_app.register_blueprint(about_bp)

    from routes.cars import cars_bp
    init_app.register_blueprint(cars_bp)

    from routes.test import test_bp
    init_app.register_blueprint(test_bp)

    from routes.auth import auth_bp
    init_app.register_blueprint(auth_bp)

    from flask_restful import Api
    init_api = Api(init_app, prefix="/api")

    from routes.cars_flask_restful import CarsResource
    init_api.add_resource(CarsResource, "/cars")

    from security import security
    security.init_app(init_app, user_datastore)

    return init_app

app = create_flask_server()  # app = create_flask_server() = Flask(__name__)

if __name__ == "__main__":
    app.run()