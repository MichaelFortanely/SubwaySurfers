from gtts import gTTS
import os
from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# const new_data = {
#       has_pdf: false,
#       pdf_name: selectedFile.name,
#       text: null
#     }
# JSON Model shown above
class DataModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # treat has_pdf as a boolean
    has_pdf = db.Column(db.Integer, default=0)
    pdf_name = db.Column(db.String(100))
    text = db.Column(db.String(1000))

if __name__ == '__main__':
    app.run(debug=True)

# def convert_text_speech():
#     mytext = """My husband (m35) and I (f39) are separated. Our oldest (f4) looks a lot like me and according to my husband she has the same personality. I had bad things happen to me when I was younger(20's) and my husband knows about it. He never blamed me for what happened but he thinks I'm too trusting and "naive, his word" and that it was used against me. My husband started worrying about our daughter when she turned 3 and her personality started showing. He started making observations about our daughter being very calm and kind and too trusting. That people are going to take advantage of her. That she will have what happened to me happen to her too. He hates that she is trusting. Her kindergarten teacher says that she is very kind and fairly liked by her peers but that she is very laid back and doesn't take much space. she doest want to be in the center on attention and her psychologist says that she has healthy boundaries and is a happy child.
#     Even after talking her her  He insists that he should have the children more. I understand where he is coming from but I just don't want it to have negative effects on her. I don't know how to feel about this. how can I tell my 4 years old that her feelings and suspicions about her father are wrong when they are right?
#     """
#     myobj = gTTS(text=mytext, lang='en', slow=False)
#     myobj.save('reddit.mp3')
#     os.system("mpg321 reddit.mp3")