import marshmallow_mongoengine as ma
from models.user_model import Users
from schemas.roleuserschema import RolesSchema
from marshmallow import fields
from marshmallow.fields import Nested

class UserSchema(ma.ModelSchema):
    roleId =ma.fields.Nested(RolesSchema,many=True)
    class Meta:
        fields=("roleId",)
        model = Users

class user_signupSchema(ma.ModelSchema):
    class Meta:
        fields=("email","password")
        model = Users

class User_loginSchema(ma.ModelSchema):
    class Meta:
        fields=("email","password")
        model = Users

class UsersSchema(ma.ModelSchema):
    class Meta:
        #fields=("email","password")
        model = Users
