from flask import Flask, render_template, url_for, redirect
from flask.globals import request
from services.signup_service import SignupService
from services.login_service import LoginService


app = Flask(__name__)

''' login function '''
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # json_data = request.data
        email = request.form['email']
        password = request.form['password']
        result = LoginService({
            'email': email,
            'password': password
        }).login()
        if result == "UserNotFound":
            return render_template('lg.html', result='Invalid Username and Password')
        else:
            return redirect('/')
    return render_template('lg.html')

@app.route('/logout', methods=['GET'])
def logout():
    return redirect('/login')

'''' home function '''
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

'''' signup function '''
@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # json_data = request.data
        name = request.form['name']
        email = request.form['email']
        pas = request.form['password']
        c_pass = request.form['re_password']
        print(name, email, pas, c_pass)
        # if name == None or email == None or pas == None or c_pass == None:
        #     return render_template('signup.html')
        if pas == c_pass:
            auth = SignupService({
            'name': name,
            'email': email,
            'password': pas
            }).signup()
            if auth == "Already Exists":
                return render_template('signup.html', result="User Already Exists")
            else:
                return render_template('signup.html', result = "Successfully Regirstered")
            
        else:
            return render_template('signup.html', result="Password doesn't match")
    else:
        return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)