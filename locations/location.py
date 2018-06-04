from flask import Blueprint, jsonify
from config.config_mysql import mysql


class GetLocationsFromDataBase:
    def __init__(self, location_address):
        self.location_address = location_address

    @classmethod
    def get_all_location(cls):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT address.id_address, address.coordinates, address.location_name FROM address;'

        cursor.execute(query)

        locations = cursor.fetchall()

        connect.commit()
        cursor.close()

        return locations


info_about_location = Blueprint('info_about_location', __name__)


@info_about_location.route('/get/locations', methods=['GET'])
def get_all_location():
    locations = GetLocationsFromDataBase.get_all_location()
    response_address = []
    for result in locations:
        location_name = result[2]
        coordinate = result[1].split(',')
        lat = coordinate[0]
        lng = coordinate[1]
        url = location_name.lower().split(' ')[0] + ".html"
        address = {
            'location_id': result[0],
            'name': location_name,
            'lat': float(lat),
            'lng': float(lng),
            'url': "/location/" + url
        }
        response_address.append(address)
    return jsonify(location=response_address), 200


@info_about_location.route('/near/location/<lat>/<lng>')
def near_location(lat, lng):
    all_locations = GetLocationsFromDataBase.get_all_location()
    results = []
    for location in all_locations:
        coordinate = location[1].split(',')
        lat_db = float(coordinate[0])
        lng_db = float(coordinate[1])
        result_sum = pow(pow(float(lat)+lat_db, 2) + pow(float(lng) + lng_db, 2), 0.5)
        id_location = location[0]
        result = {
            'result': result_sum,
            'id_location': id_location
        }
        results.append(result)
    count = len(results)
    return jsonify(near_location=results, count=count), 200
