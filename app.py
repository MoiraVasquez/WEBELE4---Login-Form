from flask import Flask, render_template, request
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'maeswolf'

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.is_submitted():
        result = request.form
        email = request.form["email"]
        password = request.form["password"]
        message = ""
        if request.form["email"] == "test@flask.app" and request.form["password"] == "password123":
            return render_template('user.html', password=password, email=email, result=result)
        else:
            message = "Invalid email or password"
            return render_template('login.html', form=form, password=password, message=message, email=email, result=result)
    return render_template('login.html', form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
