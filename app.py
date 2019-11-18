from flask import Flask
from flask_restful import Api
from config import app
from controllers.roles.getpost_roles import GetcreateRoles
from controllers.roles.getbyidupdate_roles import UpdateRoles
from controllers.users.getpost_users import GetcreateUsers,UserSignup,Signin
from models.librarymodel import Library

api = Api(app)

api.add_resource(GetcreateRoles, '/addrole')
api.add_resource(UpdateRoles, '/updaterole/<id>')
api.add_resource(GetcreateUsers, '/adduser')
api.add_resource(UserSignup, '/signup')
api.add_resource(Signin, '/sigin')
api.add_resource(Library, '/file')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
