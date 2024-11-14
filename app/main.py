from flask import Flask

from app.routs.get_data_rout import data_blueprint

app = Flask(__name__)
app.register_blueprint(data_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run()