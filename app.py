from flask import Flask
from controller.controller_injuries import blueprint

app = Flask(__name__)

app.register_blueprint(blueprint, url_prefix="/api")
# Run the app
if __name__ == '__main__':

    app.run(debug=True)