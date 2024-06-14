from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = (
    os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS") == "True"
)
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run()
