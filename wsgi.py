import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
csrf = CSRFProtect(app)

SECRET_KEY = os.urandom(43)#Создаем рандомнй ключ
app.config['SECRET_KEY'] = SECRET_KEY


class MyForm(FlaskForm):
    name = StringField('name')


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/sign/', methods=['GET', 'POST'])
def myform():
    form = MyForm()
    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

