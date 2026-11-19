# Purpose: Starts the Flask app and registers every Blueprint. Run: python3 app.py
# The only place to launch the app. Port comes from .env (PORT), default 5001.
import os
from flask import Flask
from dotenv import load_dotenv
from routes.login_routes import login_bp
from routes.period_routes import period_bp

load_dotenv()

app = Flask(__name__)
app.register_blueprint(login_bp)   # /  and  /login
app.register_blueprint(period_bp)  # /periods

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
