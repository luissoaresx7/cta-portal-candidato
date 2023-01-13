from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, SelectField, DateField, IntegerField
from wtforms.validators import ValidationError, DataRequired, \
    Email, EqualTo, Length

import os

app = Flask(__name__, template_folder='templates')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = 'QWKLWJKWHEFJHWEJFSHKJDAHFKJSHDFJKHSJKHF'

class CreateUserForm(FlaskForm):
    class Meta:
        locales = ['pt_BR', 'pt']
        def get_translations(self, form):
            return super(FlaskForm.Meta, self).get_translations(form)
    username = StringField(label=('Nome de usuário'),
        validators=[DataRequired(),
        Length(max=64)])
    email = StringField(label=('E-mail'),
        validators=[DataRequired(),
        Email(),
        Length(max=120)])
    password = PasswordField(label=('Senha'),
        validators=[DataRequired(),
        Length(min=8, message='A senha deve ter no mínimo %(min)d caracteres.')])
    confirm_password = PasswordField(
        label=('Confirmação da senha'),
        validators=[DataRequired(message='*Required'),
        EqualTo('password', message='As senhas devem ser iguais.')])
    raca_cor_etinia = SelectField(u'Raça/Cor/Etinia', choices=[('1', 'Amarela(o)'), ('2', 'Branca(o)'),('3','Cigana(o)'),('4','Indigena'),('5','parda(o)'),('6','Preta(o)' ), ])

    idade = IntegerField(label='Idade'),
    validators = [DataRequired(message='Required'),
    Length(min=2),]

    submit = SubmitField(label=('Enviar'))


class UserSub(FlaskForm):
    class Meta:
        locales = ['pt_BR', 'pt']

        def get_translations(self, form):
            return super(FlaskForm.Meta, self).get_translations(form)

    username = StringField(label=('Nome de usuário'),
        validators=[DataRequired(),
        Length(max=64)])
    email = StringField(label=('Nome social'),
         validators=[DataRequired(),
        Length(max=64)])
    born_date = DateField(label=('Data de nascimento'),
        validators=[DataRequired(),])

    raca_cor_etinia = SelectField(u'Raça/Cor/Etinia',
         choices=[('1', 'Amarela(o)'), ('2', 'Branca(o)'), ('3', 'Cigana(o)'),
         ('4', 'Indigena'), ('5', 'parda(o)'), ('6', 'Preta(o)') ])

    idade = StringField(label=('Idade'),
    validators = [DataRequired(message='Required'),
         Length(min=2),])

    submit = SubmitField(label=('Enviar'))

@app.route('/registro', methods=('GET', 'POST'))
def index():
    form = CreateUserForm()
    if form.validate_on_submit():
        return f'''<h1> Bem-vindo {form.username.data} </h1>'''
    return render_template('register.html', form=form)

@app.route('/inscricao', methods=('GET', 'POST'))
def sub():
    formSub = UserSub()
    return render_template('formulario.html', form=formSub)