from config_app import app
from flaskext.mysql import MySQL

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1111'
app.config['MYSQL_DATABASE_DB'] = 'easyparking'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)
