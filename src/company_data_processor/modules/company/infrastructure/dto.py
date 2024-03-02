from company_data_processor.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()


class Company(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.String, primary_key=True)
    registration_date = db.Column(db.DateTime, nullable=False)
    renovation_date = db.Column(db.DateTime, nullable=False)
    nit = db.Column(db.String, primary_key=True)
    acronym = db.Column(db.String, primary_key=True)
    status = db.Column(db.String, primary_key=True)
    validity = db.Column(db.String, primary_key=True)
    organization_type = db.Column(db.String, primary_key=True)
    registration_category = db.Column(db.String, primary_key=True)
