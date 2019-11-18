from flask import request
from flask import jsonify
from flask_restful import Resource
from models.user_model import Users
from schemas.user_schemas import UserSchema, user_signupSchema,User_loginSchema
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
# API calls for get and post users
class GetcreateUsers(Resource):
    def __init__(self):
        pass

    def get(self):
        #try:
            user = Users.objects.all()
            print(">>>>>>>>>>>>>>>>>>>>>>.",user)
            if user:
                user_schema = UserSchema(many=True)
                print("<<<<<<<<<<<<<<<<<<<<",user_schema)
                data = user_schema.dump(user).data
                print("<<<<<<<<<<<<<<<<<",data)
                return jsonify({"data": data, 'message': "Inserted Successfully"})
            else:
                return jsonify({'Success': True, 'message': "Data does not exists"})
        # except Exception as e:
        #     return e

    def post(self):
        try:
            json_data = request.get_json()
            user_schema = UserSchema()
            obj = user_schema.load(json_data).data
            obj.save()
            data = user_schema.dump(obj).data
            return jsonify({"data": data, 'message': "Inserted Successfully"})
        except Exception as e:
            return e



class UserSignup(Resource):
    def post(self):
        #try:
            json_data= request.get_json()
            password=json_data["password"]

            hash_password = generate_password_hash(password)
            print(hash_password)
            schema = user_signupSchema()
            new_signup = schema.load(json_data).data
            new_signup.password = hash_password
            new_signup.save()
            data = schema.dump(new_signup).data
            # logger.info("user signup successfully")
            # loggers.info("user signup successfully")
            return {'success':True,
                'data'         : data
                }
    #     else:
    #         # logger.warning("email already exists")
    #         # loggers.warning("email already exists")
    #         return ({"success":False,"message":"email already exists"})
    # # except Exception as e:
    # #     # logger.warning(str(e))
    #     #     # loggers.warning(str(e))
    #         # return({"success":False,"message":str(e)})




class Signin(Resource):
    def __init__(self):
        pass

    # login call for the user
    def post(self):
        try:
            sign_in = request.get_json()
            print(sign_in)
            email = sign_in['email']
            print(email)
            password = sign_in['password']
            email_check = Users.objects.get(email=email)
            print(user.password)
            if email_check is not None:
                schema = User_loginSchema()
                data   = schema.dump(email_check)
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",data)
                hashed_password = email_check.password
                print(hashed_password)
                if check_password_hash(hashed_password,password):
                    return {"success":True,
                        'data':data,
                        'message': 'logined successfully'
                        }
                else:

                    return({"success":False,"message": "Invalid password"})
            else:

                return({"success":False,"message": "Invalid UserName"})
        except Exception as e:
        #     # logger.warning(str(e))
        #     # loggers.warning(str(e))
              return({"success":False,"message":str(e)})
