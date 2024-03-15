from flask import Flask, request, jsonify
from controllers.CreateController import create_controller
from controllers.HomeController import home_controller
from controllers.DeleteController import delete_controller
from conn import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/library_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '4ca069aca94aaeb89f16f8d36f4c77f8'

db.init_app(app)

app.register_blueprint(create_controller, url_prefix="/add_book")
app.register_blueprint(home_controller, url_prefix="/")
app.register_blueprint(delete_controller, url_prefix="/delete_book")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
