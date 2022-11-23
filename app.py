from gtts import gTTS
import os
from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, abort, fields

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

dummy_data_structure = dict()
text_put_args = reqparse.RequestParser()
text_put_args.add_argument("text", type=str, help="The text entered in from the page", required=True)

def convert_text_speech(input, id):
    myobj = gTTS(text=input, lang='en', slow=False)
    myobj.save(str(id) + '.mp3')
    os.system("mpg321 " + str(id) + ".mp3")
    return str(id) + ".mp3"


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

class Text(Resource):
    def get(self, text_id):
        if text_id not in dummy_data_structure.keys():
            return None
        else:
            return dummy_data_structure[text_id]

    def put(self, text_id):
        args = text_put_args.parse_args()
        dummy_data_structure[text_id] = convert_text_speech(args['text'], text_id)
        return args['text']

api.add_resource(Text, '/text/<int:text_id>')

if __name__ == '__main__':
    app.run(debug=True)