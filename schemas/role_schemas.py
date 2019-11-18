import marshmallow_mongoengine as ma
from models.roles_model import Roles
from schemas.user_schemas import UsersSchema
from marshmallow import fields
from marshmallow.fields import Nested

class RoleSchema(ma.ModelSchema):

    class Meta:
    
        model = Roles
