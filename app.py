# Purpose: Starts the Flask app and registers every Blueprint. Run: python3 app.py
# The only place to launch the app. Port comes from .env (PORT), default 5001.
import os
from flask import Flask
from dotenv import load_dotenv
from routes.login_routes import login_bp
from routes.period_routes import period_bp
from routes.open_review_routes import submit_open_bp
from routes.confidential_review_routes import submit_confidential_bp
from routes.integrity_routes import integrity_bp

load_dotenv()

app = Flask(__name__)
app.secret_key = '123'
app.register_blueprint(login_bp)   # /  and  /login
app.register_blueprint(period_bp)  # /periods
app.register_blueprint(submit_open_bp) # /submitOpen
app.register_blueprint(submit_confidential_bp) # /submitConfidential
app.register_blueprint(integrity_bp)  # /integrity

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
