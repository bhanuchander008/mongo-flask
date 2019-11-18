import datetime
import mongoengine as me
from mongoengine import ReferenceField
from models.roles_model import Roles


# Users model
class Users(me.Document):
    firstName = me.StringField(max_length=50, required=False)
    lastName = me.StringField(max_length=50, required=False)
    email = me.StringField(max_length=50)
    username = me.StringField(max_length=50, required=False)
    password = me.StringField(required=False)
    status = me.StringField(default="InActive")
    mobile = me.StringField(max_length=13)
    emailVerified = me.BooleanField(default=False)
    mobileVerified = me.BooleanField(default=False)
    roleId = me.ReferenceField(Roles, required=False)
    createdAt = me.DateTimeField(required=True, default=datetime.datetime.now())
    updatedAt = me.DateTimeField(required=True, default=datetime.datetime.now())
