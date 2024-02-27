from src.company_data_collector.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()


class Company(db.Model):
    __tablename__ = "reservas"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    itinerarios = db.relationship('Itinerario', secondary=reservas_itinerarios, backref='reservas')
