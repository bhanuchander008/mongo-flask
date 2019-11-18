from models.roles_model import Roles
from models.user_model import Users
from config import *
bttf = Users(firstName="Back To The Future",lastName="sheeram",username='bhanu',password="bhanu",roleId=1)
bttf.save()
