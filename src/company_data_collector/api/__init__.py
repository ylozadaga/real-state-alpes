import os

from flask import Flask, jsonify
from flask_swagger import swagger

basedir = os.path.abspath(os.path.dirname(__file__))


def record_handlers():
    from ..modules.company import application


def import_alchemy_models():
    from ..modules.company.infrastructure import dto


def start_consumer(app: Flask):
    import threading
    from ..modules.company.infrastructure import consumers as company

    threading.Thread(target=company.subscribe_to_events()).start()

    threading.Thread(target=company.subscribe_to_commands,
                     args=[app.app_context(), app.test_request_context()]).start()


def create_app(config={}):
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL',
                                                      'sqlite:///' + os.path.join(basedir, 'company-data-collector.db'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = config.get('TESTING')

    from ..config.db import init_db
    init_db(app)

    from ..config.db import db

    import_alchemy_models()
    record_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            start_consumer(app)

    from . import company
    app.register_blueprint(company.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "rs-alpes - company_data_collector"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
