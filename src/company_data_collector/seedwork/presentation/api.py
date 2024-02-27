import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


def create_blueprint(identifier: str, url_prefix: str):
    return Blueprint(identifier, __name__, url_prefix=url_prefix)
