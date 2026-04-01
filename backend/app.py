from flask import Flask
from flask_cors import CORS

# import routes
from routes.auth import auth_routes
from routes.booking import booking_routes
from routes.admin import admin_routes

# create app FIRST
app = Flask(__name__)
CORS(app)

# register routes
app.register_blueprint(auth_routes)
app.register_blueprint(booking_routes)
app.register_blueprint(admin_routes)

# run server
if __name__ == "__main__":
    app.run(debug=True)