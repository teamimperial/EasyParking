from flask import Flask, render_template, send_from_directory
from dataaboutplaces.placesinfoset import info_about_places_set
from locations.location import info_about_location
from config.config_app import SECRET_KEY

app = Flask(__name__, static_url_path='/static')
app.secret_key = SECRET_KEY


@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')


@app.route('/map', methods=['GET'])
def map_page():
    return render_template('map.html')


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


app.register_blueprint(info_about_places_set)
app.register_blueprint(info_about_location)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
