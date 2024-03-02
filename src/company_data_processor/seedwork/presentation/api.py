from flask import (
    Blueprint
)


def create_blueprint(identifier: str, url_prefix: str):
    return Blueprint(identifier, __name__, url_prefix=url_prefix)
