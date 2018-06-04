from flask import Flask, render_template, send_from_directory, request, redirect, jsonify
from dataaboutplaces.placesinfoset import info_about_places_set, SetInfoAboutPlace
from locations.location import info_about_location
from config.config_app import SECRET_KEY

app = Flask(__name__, static_url_path='/static')
app.secret_key = SECRET_KEY


@app.before_request
def before_request():
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)


@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')


@app.route('/map', methods=['GET'])
def map_page():
    return render_template('map.html')


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


@app.route('/location/<html>')
def redirect_to_html(html):
    return render_template(html), 200


@app.route('/set/info/test/<id_device>/<status>')
def set_info_test(id_device,status):
    SetInfoAboutPlace.set_info_about_places(id_device, status)
    return jsonify("OK"), 200


app.register_blueprint(info_about_places_set)
app.register_blueprint(info_about_location)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
