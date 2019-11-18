from flask import request
from flask import jsonify
from flask_restful import Resource
from models.roles_model import Roles
from schemas.role_schemas import RoleSchema


# API calls for get and post roles
class GetcreateRoles(Resource):
    def __init__(self):
        pass

    def get(self):
        try:
            role = Roles.objects.all()
            if role:
                role_schema = RoleSchema(many=True)
                data = role_schema.dump(role).data
                return jsonify({"data": data, 'message': "Inserted Succesfuuly"})
            else:
                return({'Success': True, 'message': "Data does not exists"})
        except Exception as e:
            return e

    def post(self):
        try:
            json_data = request.get_json()
            role_schema = RoleSchema()
            obj = role_schema.load(json_data).data
            obj.save()
            data = role_schema.dump(obj).data
            return jsonify({"data": data, 'message': "Inserted Succesfuuly"})
        except Exception as e:
            return e
#
# class GetAggRoles(Resource):
#     def __init__(self):
#         pass
#
#     def get(self):
#         try:
#             role = Roles.objects.all()
#             if role:
#                 role_schema = RoleSchema(many=True)
#                 data = role_schema.dump(role).data
#                 return jsonify({"data": data, 'message': "Inserted Succesfuuly"})
#             else:
#                 return({'Success': True, 'message': "Data does not exists"})
#         except Exception as e:
#             return e
