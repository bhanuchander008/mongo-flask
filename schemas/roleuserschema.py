import marshmallow_mongoengine as ma
from models.roles_model import Roles


class RolesSchema(ma.ModelSchema):
    class Meta:
        model = Roles
