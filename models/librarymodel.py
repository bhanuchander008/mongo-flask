from flask import make_response,abort,request,redirect, url_for,Flask
from flask import make_response,abort,request,redirect, url_for,Flask
import datetime
import mongoengine as me
from mongoengine import ReferenceField
from flask_restful import Resource
import os
import marshmallow_mongoengine as ma
from flask import make_response, abort, request, redirect, url_for, Flask
from werkzeug.utils import secure_filename
from mongoengine import FileField
from config import *
from flask import jsonify

class Library(me.Document):
     files = me.StringField(max_length=50)




class library_Schema(ma.ModelSchema):
    class Meta():
        model=Library



app = Flask(__name__,static_url_path='/static')
path = os.getcwd()
UPLOAD_FOLDER = path+'/static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from config import db


class Library(Resource):
    def __init__(self):
        pass
    def post(self):
         files = request.files.getlist("file")
         print(files)
         li=[]
         for f in files:
             print(">>>>>>>>>>>>",f)
             filename = secure_filename(f.filename)
             f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
             file_url = url_for("static",filename=filename)
             lib_obj=library_Schema()
             obj1=lib_obj.load({"files":file_url}).data
             obj1.save()



clas
