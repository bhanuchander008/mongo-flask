from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'sample',
    'host': 'localhost',
    'port': 27017

}
db = MongoEngine(app)

db = MongoEngine(app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
STRIPE_API_KEY = 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv'
