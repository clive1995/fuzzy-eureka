from flask_restplus import reqparse, Resource
from flask import request
from app.main import db
from app.main.dto.experience_dto import ExperienceDTO
# from app.main.model.experience_model import
from app.main.model.customer_model import Customer,Experience, ExperienceSchema, CustomerSchema
from datetime import datetime

parser = reqparse.RequestParser()
parser.add_argument('customer_id',type=int,required=True)

api = ExperienceDTO.api

deleteParser = reqparse.RequestParser()
deleteParser.add_argument('id', type=int, required=True)

@api.route('/add-experience')
class ExperienceTest(Resource):
    @api.expect(ExperienceDTO.addExperience)
    def post(self):
        try:
            data = request.json
            print(data)
            print(data['todate'])
            print(datetime.strptime(data['todate'], '%d-%m-%Y'))
            experience = Experience(
                customer_id=data['customerId'],
                noofyears = data['noofyears'],
                company = data['company'],
                skills = data['skills'],
                current = data['current'],
                todate =  datetime.strptime(data['todate'], '%d-%m-%Y'),
                fromdate = datetime.strptime(data['fromdate'], '%d-%m-%Y'),
                location = data['location'],
                title = data['title'],
                description= data['description']
            )

            db.session.add(experience)
            db.session.commit()
            return {'message': 'Did  work'}, 200
            return data
        except Exception as e:
            print(e)
            return {'message':'Did not work'}, 400

    @api.expect(parser)
    def get(self):
        data = parser.parse_args()
        # .filter_by(customer_id=data['customer_id'])
        query = db.session.query(Customer).join(Experience).all()
        schema = CustomerSchema()
        print(query)
        print(schema.dump(query,many=True))
        print(data)

    @api.expect(deleteParser)
    def delete(self):
        try:
            data = deleteParser.parse_args()
            data['id']
            experience = db.session.query(Experience).filter_by(id=data['id']).delete()
            db.session.commit()
            print(experience)
            return {'message':'Experience deleted Successfully'}, 200
        except Exception as e:
            return {'message':'Failed to delete record.'},400

    @api.expect(ExperienceDTO.updateExperience)
    def put(self):
        try:
            data = request.json
            experienceId = data['experienceId']
            data['todate'] = datetime.strptime(data['todate'],'%d-%m-%Y')
            data['fromdate'] = datetime.strptime(data['fromdate'],'%d-%m-%Y')
            del data['experienceId']
            print(data)
            db.session.query(Experience).filter_by(id=experienceId).update(data, synchronize_session=False)
            db.session.commit()
            return {'message':'data updated successfully'}, 200
        except Exception as e:
            print(e)
            return {'message':'Failed to updated data.'},400


