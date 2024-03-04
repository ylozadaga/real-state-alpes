from ....config.db import db

Base = db.declarative_base()


class Company(db.Model):
    __tablename__ = "company"
    id = db.Column(db.String, primary_key=True)
    nit = db.Column(db.String, primary_key=True)
    acronym = db.Column(db.String, primary_key=True)
    status = db.Column(db.String, primary_key=True)
    validity = db.Column(db.String, primary_key=True)
    organization_type = db.Column(db.String, primary_key=True)
    registration_category = db.Column(db.String, primary_key=True)
