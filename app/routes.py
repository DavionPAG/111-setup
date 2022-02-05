from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello World'

app.get('/home')
def home():
  return 'Home'

app.route('/about', methods=['GET'])
def about():
  me = {
    'first': 'Davion',
    'last': 'Garcia',
    'hobbies': 'Chess',
    'active': True,
    }
  return me