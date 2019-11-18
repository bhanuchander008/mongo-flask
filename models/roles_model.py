import datetime
import mongoengine as me
from mongoengine import ReferenceField
#from models.user_model import Users

# Roles model
class Roles(me.Document):
    name = me.StringField(max_length=60)
    status = me.StringField(default="Active")
    createdBy = me.ReferenceField('Users')
    updatedBy = me.ReferenceField('Users')
    createdAt = me.DateTimeField(required=True, default=datetime.datetime.utcnow())
    updatedAt = me.DateTimeField(required=True, default=datetime.datetime.utcnow())
    user= me.ReferenceField('Users',backpopulates="user_role")
