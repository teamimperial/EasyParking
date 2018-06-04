from flask import Blueprint, request, abort, jsonify

info_about_places = []

info_about_places_set = Blueprint('info_about_places_set', __name__)


@info_about_places_set.route('/set/info', methods=['POST'])
def set_info_about_places():
    if not request.json and 'id' not in request.json and 'status' not in request.json:
        return abort(400)

    id_device = request.json['id']
    status = request.json['status']
    place = [id_device, status]

    if len(info_about_places) == 0:
        info_about_places.append(place)
    else:
        value = 0
        for place_saved in info_about_places:
            id_device_saved = place_saved[0].split('.')
            id_device_split = id_device.split('.')
            if int(id_device_saved[0]) == int(id_device_split[0]) \
                    and int(id_device_saved[1]) == int(id_device_split[1]) \
                    and int(id_device_saved[2]) == int(id_device_split[2]):
                place_saved[1] = status
                value = 1
                break
        if value == 0:
            info_about_places.append(place)
    return jsonify('OK'), 200


@info_about_places_set.route('/get/info/<id_parking>', methods=['GET'])
def get_info_about(id_parking):
    info_about_parking = []
    save_info = info_about_places
    for place in save_info:
        id_parking_saved = place[0].split('.')
        if id_parking_saved[0] == id_parking:
            place_to_return = {
                'id_line': id_parking_saved[1],
                'id_place': id_parking_saved[2],
                'status': place[1]
            }
            info_about_parking.append(place_to_return)
    return jsonify(id_parking=id_parking, places=info_about_parking)


@info_about_places_set.route('/get/all/info')
def get_all_info():
    return str(info_about_places)


class SetInfoAboutPlace:
    def __init__(self):
        pass

    @classmethod
    def set_info_about_places(cls, id_device, status):
        place = [id_device, status]
        if len(info_about_places) == 0:
            info_about_places.append(place)
        else:
            value = 0
            for place_saved in info_about_places:
                id_device_saved = place_saved[0].split('.')
                id_device_split = id_device.split('.')
                if int(id_device_saved[0]) == int(id_device_split[0]) \
                        and int(id_device_saved[1]) == int(id_device_split[1]) \
                        and int(id_device_saved[2]) == int(id_device_split[2]):
                    place_saved[1] = status
                    value = 1
                    break
            if value == 0:
                info_about_places.append(place)
