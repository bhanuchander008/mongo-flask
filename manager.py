from config import app
from flask_mongoengine import MongoEngine
from models.loginhistory_model import LoginHistory
from models.permissions_model import Permissions
from models.resetlink_model import ResetLink
from models.resetpassword_model import ResetPassword
from models.roles_model import Roles
from models.user_model import Users
from models.views_model import Views
from models.librarymodel import Library

app.config['MONGODB_SETTINGS'] = {
    'db': 'sample',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)
