from flask import Flask, render_template,request, redirect
#import pymongo

app = Flask(__name__)

#client = pymongo.MongoClient('mongodb://0.0.0.0:27017/',connect=False)
#db = client["Brain-Tumor-Detection"]

@app.route('/')
def welcome_page():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/login2',methods=['POST','GET'])
def login_post():
    print(request.form)
    return redirect('/upload')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/upload')
def upload_img():
    return render_template('imageInput.html')

@app.route('/upload2',methods=['POST','GET'])
def upload_img():
    return render_template('imageInput.html')


if __name__ == '__main__':
    app.run(debug = True)