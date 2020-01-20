from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from main import get_tweets

UPLOAD_FOLDER = '/Users/yifansheep/Desktop/Flask/api'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return "Hello"

@app.route('/twitterkeyword', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        keyword = request.args.get("keyword")
        return get_tweets(keyword)

    if request.method == 'POST':
        keyword = request.form.get("keyword")
        print("------- KEYWORD -------")
        print(request.form.get("keyword"))
#below runs misha's code using fetched keyword and then returns the json file
        print(get_tweets(keyword))
        return get_tweets(keyword)


app.run(port=8080)