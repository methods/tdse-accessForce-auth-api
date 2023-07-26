from flask import Flask
from controller import authorise

app = Flask(__name__)

app.register_blueprint(authorise, url_prefix="/authorise")

if __name__ == "__main__":
    app.run(port=5000)
