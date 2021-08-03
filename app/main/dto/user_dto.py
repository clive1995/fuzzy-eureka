from flask_restplus import Namespace, fields

class userDTO:
    api = Namespace('User', description='this is user DTO')

    UserRegister = api.model('UserRegister',{
        'username':fields.String(),
        'email':fields.String(),
        'password':fields.String(),
    })

    updateCustomer = api.model('updateCustomer',{
        'username':fields.String(),
        'email':fields.String(),
        'password':fields.String()
    })