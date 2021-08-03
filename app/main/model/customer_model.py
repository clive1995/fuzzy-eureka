
from sqlalchemy.orm import  relationship
# from .experience_model import Experience
from sqlalchemy import ForeignKey
from marshmallow import fields
from sqlalchemy.dialects.postgresql import JSON
from app.main import db, ma


class Customer(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    hash = db.Column(db.String())
    db.UniqueConstraint('email', name='uix_1')

    experience = relationship('Experience', back_populates="customer")
    education = relationship('Education', back_populates='customer')

class Experience(db.Model):
    __tablename__ = "experience"
    customer = relationship('Customer',back_populates="experience")

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'))
    noofyears = db.Column(db.Integer)
    company = db.Column(db.String)
    skills = db.Column(JSON)
    current = db.Column(db.Boolean)
    todate = db.Column(db.Date)
    fromdate = db.Column(db.Date)
    location = db.Column(db.String)
    title = db.Column(db.String)
    description = db.Column(db.String)


class Education(db.Model):
    __tablename__ = 'education'

    customer = relationship('Customer', back_populates='education')

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'))
    school = db.Column(db.String)
    degree = db.Column(db.String)
    fieldofstudy = db.Column(db.String)
    fromdate = db.Column(db.Date)
    todate = db.Column(db.Date)
    current = db.Column(db.Boolean)
    description = db.Column(db.String)


class EducationSchema(ma.SQLAlchemyAutoSchema):
    class meta:
        include_fk = True
        model = Education



class ExperienceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        include_fk = True
        model = Experience


class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        include_fk = True
        sqla_session = db.session
    experience = fields.Nested(ExperienceSchema,many=True)
    education = fields.Nested(EducationSchema, many=True)
