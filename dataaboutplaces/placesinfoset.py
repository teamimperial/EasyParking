from flask import Blueprint, request, abort, jsonify
from config.config_mysql import mysql


info_about_places_set = Blueprint('info_about_places_set', __name__)


class InfoAboutPlaceSet:
    def __init__(self):
        pass

    @classmethod
    def save_info_about_place(cls, id_parking, id_place, id_line, status):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'UPDATE place, line, parking SET place_empty = %s WHERE place.id_line = line.id_line ' \
                'and line.id_parking = parking.id_parking and line.line_number = %s ' \
                'and place.place_number = %s and parking.id_parking = %s; '
        param = (status, id_line, id_place, id_parking)

        cursor.execute(query, param)

        connect.commit()
        cursor.close()


@info_about_places_set.route('/set/info', methods=['POST'])
def set_info_about_places():
    if not request.json and 'id_device' not in request.json and 'status' not in request.json:
        return abort(404)

    id_device = request.json['id_device'].split('.')
    id_parking = id_device[0]
    id_line = id_device[1]
    id_place = id_device[2]
    status = request.json['status']
    InfoAboutPlaceSet.save_info_about_place(id_parking, id_place, id_line, status)
    return jsonify('OK'), 200

