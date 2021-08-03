from flask_restplus import Namespace, fields


class ExperienceDTO:
    api = Namespace('experience', description="this area contains experience")

    addExperience = api.model('addExperience', {
        'customerId':fields.Integer(),
        'noofyears': fields.Integer(),
        'company': fields.String(),
        'skills': fields.List(fields.String()),
        'current': fields.Boolean(),
        'todate': fields.String(),
        'fromdate': fields.String(),
        'location': fields.String(),
        'title': fields.String(),
        'description':fields.String()
    })

    updateExperience = api.model('updateExperience',{
        'experienceId':fields.Integer(),
        'noofyears': fields.Integer(),
        'company': fields.String(),
        'skills': fields.List(fields.String()),
        'current': fields.Boolean(),
        'todate': fields.String(),
        'fromdate': fields.String(),
        'location': fields.String(),
        'title': fields.String(),
        'description':fields.String()
    })