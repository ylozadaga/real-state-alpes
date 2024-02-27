import os

from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from flask_swagger import swagger

basedir = os.path.abspath(os.path.dirname(__file__))


def record_handlers():
    import src.company_data_collector.modules.company.application


def import_alchemy_models():
    import src.company_data_collector.modules.company.intrastructure.dto


def start_consumer():
    import threading
    import src.company_data_collector.modules.company.intrastructure.consumers as company

    threading.Thread(target=company.subscribe_to_events()).start()

    threading.Thread(target=company.subscribe_to_commands()).start()


def create_app(config={}):
    app = Flask(__name__, instance_relative_config=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'database.db')
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
            start_consumer()

    from . import company
    app.register_blueprint(company.bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
