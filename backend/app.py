from flask import Flask
from flask_cors import CORS

from routes.auth import auth_routes
from routes.booking import booking_routes
from routes.admin import admin_routes

app = Flask(__name__)
CORS(app)

# Register routes
app.register_blueprint(auth_routes)
app.register_blueprint(booking_routes)
app.register_blueprint(admin_routes)

if __name__ == "__main__":
    app.run(debug=True)