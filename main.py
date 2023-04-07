from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import os


SECRET_KEY = os.urandom(64)
WTF_CSRF_SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY=SECRET_KEY,
    WTF_CSRF_SECRET_KEY=WTF_CSRF_SECRET_KEY
))


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    form.validate_on_submit()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
