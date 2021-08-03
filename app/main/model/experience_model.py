# from .customer_model import Customer
# from app.main import db, ma
# from sqlalchemy.dialects.postgresql import JSON
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship
#
#
# class Experience(db.Model):
#     __tablename__ = "experience"
#     customer = relationship(Customer)
#
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     customer_id = db.Column(db.Integer, ForeignKey('customer.id'))
#     noofyears = db.Column(db.Integer)
#     company = db.Column(db.String)
#     skills = db.Column(JSON)
#     current = db.Column(db.Boolean)
#     todate = db.Column(db.Date)
#     fromdate = db.Column(db.Date)
#     location = db.Column(db.String)
#     title = db.Column(db.String)
#
#
# class ExperienceSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         include_fk = True
#         model = Experience