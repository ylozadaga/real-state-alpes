from src.company_data_collector.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()


class Company(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.String, primary_key=True)
    creation_date = db.Column(db.DateTime, nullable=False)
    update_date = db.Column(db.DateTime, nullable=False)
