from flask import Blueprint, jsonify
from config.config_mysql import mysql

info_about_places_get = Blueprint('info_about_places_get', __name__)


class InfoAboutPlaceGet:
    def __init__(self):
        pass

    @classmethod
    def get_info_about_parking(cls, id_parking):
        connect = mysql.connect()
        cursor = connect.cursor()

        query = 'SELECT line.line_number, place.place_number, place_empty from line, place, parking ' \
                'where parking.id_parking = %s and line.id_parking=parking.id_parking and ' \
                'place.id_line = line.id_line;'
        param = id_parking

        cursor.execute(query, param)
        info = cursor.fetchall()

        connect.commit()
        cursor.close()

        return info


@info_about_places_get.route('/send/data/<id_parking>')
def send_data_about_places(id_parking):
    results = InfoAboutPlaceGet.get_info_about_parking(id_parking)
    info_about_parking = []
    for result in results:
        place = {
            'id_line': result[0],
            'id_number': result[1],
            'status': result[2]
        }
        info_about_parking.append(place)
    return jsonify(id_parking=id_parking,places=info_about_parking), 200
