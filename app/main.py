from flask import Flask

from app.routs.get_and_produce_data_routs import data_blueprint
from app.routs.messages_route import messages_blueprint

app = Flask(__name__)
app.register_blueprint(data_blueprint, url_prefix='/api')
app.register_blueprint(messages_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run()