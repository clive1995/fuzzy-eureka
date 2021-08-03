from flask_restplus import Resource, reqparse
from flask import request
from app.main import db
from app.main.dto.user_dto import userDTO
from app.main.model.customer_model import Customer, CustomerSchema

api = userDTO.api

parseCustomer = reqparse.RequestParser()
parseCustomer.add_argument('customerId', type=int,required=True)

@api.route('/register')
class Register(Resource):
    @api.expect(userDTO.UserRegister)
    def post(self):
        data = request.json
        try:
            customer = db.session.query(Customer).filter_by(email=data['email']).first()
            if customer:
                return {'message':'User with this email already exists'},400
            customer = Customer(
                email=data['email'],
                username=data['username'],
                password=data['password']
            )
            db.session.add(customer)
            db.session.commit()
            return {'message':'User saved successfully'},200
            pass
        except Exception as e:
            print(e)
            return {'message':'Internal server error'}

    @api.expect(parseCustomer,validate=True)
    def get(self):
        data = parseCustomer.parse_args()
        print(data)
        customer = db.session.query(Customer).filter_by(id=int(data['customerId'])).first()
        print(customer)
        schema = CustomerSchema()
        print(schema.dump(customer))


@api.route('/customer-fetch-all')
class GetallCustomer(Resource):
    def get(self):
        query = db.session.query(Customer).all()
        schema = CustomerSchema()
        print(query[0])
        print(schema.dump(query[0]))
        return schema.dump(query,many=True)
        print(query)


@api.route('update-customer')
class UpdateCustomer(Resource):
    @api.expect(userDTO.updateCustomer)
    def put(self):
        try:
            data = request.json
            customer = db.session.query(Customer).filter_by(email=data['email']).first()
            if not customer:
                return {'message':'user with the given email does not exists.'},400

            customer.username = data['username']
            customer.password = data['password']
            db.session.commit()
            return {'message':'data saved Successfully'},200
        except Exception as e:
            print(e)
            return {'message':'Failed to save data'},400



# @api.route('/expereience')
# class Experience(Resource):
#     @api.expect()