import json
from flask import request
from flask import jsonify
from flask_restful import Resource
from models.roles_model import Roles
from schemas.role_schemas import RoleSchema


# API calls for getbyid and update roles
class UpdateRoles(Resource):
    def __init__(self):
        pass

    def get(self,id):
        try:
            role = Roles.objects(id=id)
            if role:
                role_schema = RoleSchema(many=True)
                data = role_schema.dump(role).data
                return jsonify({"data": data, 'message': "Inserted Succesfuuly"})
            else:
                return({'Success': True, 'message': "Data does not exists"})
        except Exception as e:
            return e

    def put(self,id):
        # try:
        role_data =  request.get_json()
        role = Roles.objects(id=id).update(role_data)
        if role:
            print("----------------",role)
                # json_data = request.get_json()
                # role_schema = RoleSchema()
                # obj = role_schema.load(json_data).data
                # obj.save()
                # data = role_schema.dump(obj).data
                # return jsonify({"data": data, 'message': "Inserted Succesfuuly"})
        # except Exception as e:
            # return e
