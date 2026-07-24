from flask import request
from flask_restful import Resource
from models import db, cars

# @cars_bp.route("/cars", methods=["GET", "POST", "PUT", "DELETE"])
class CarsResource(Resource):
# def cars_route():
    # if request.method == "POST":
    def post(self):
        car_data = request.json # getting the total json object from {"name": "value", "fuel": "value"} format
        if not car_data.get('name') or not car_data.get('fuel'):
            return {"message": "name and fuel are required fields"}, 400
        new_car = cars(name=car_data.get('name'), fuel=car_data.get('fuel'))
        db.session.add(new_car)
        db.session.commit()
        return {
            "message": "car added successfully",
            "car": {"name": new_car.name, "fuel": new_car.fuel}
        }
    def get(self):
        all_cars = cars.query.all()
        if not all_cars:
            return {"message": "no cars found"}, 404
        rows = [{"id": row.id, "name": row.name, "fuel": row.fuel} for row in all_cars]
        return {
            "data": rows,
            "message": "cars retrieved successfully"
        }
    def put(self):
        car_data = request.json
        if not car_data.get('id'):
            return {"message": "id is required to update a car"}, 400
        car_id = car_data.get('id')
        car_to_update = cars.query.get(car_id)
        if car_to_update:
            car_to_update.name = car_data.get('name', car_to_update.name)
            car_to_update.fuel = car_data.get('fuel', car_to_update.fuel)
            db.session.commit()
            return {
                "message": "car updated successfully",
                "car": {"id": car_to_update.id, "name": car_to_update.name, "fuel": car_to_update.fuel}
            }
        else:
            return {"message": "car not found"}, 404
    def delete(self):
        car_id = request.json.get('id')
        if not car_id:
            return {"message": "id is required to delete a car"}, 400
        car_to_delete = cars.query.get(car_id)
        if car_to_delete:
            db.session.delete(car_to_delete)
            db.session.commit()
            return {"message": "car deleted successfully"}
        else:
            return {"message": "car not found"}, 404
