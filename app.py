from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, SelectField, DateField, RadioField
from wtforms.validators import ValidationError, DataRequired, \
    Email, EqualTo, Length
import os

app = Flask(__name__, template_folder='templates')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = 'QWKLWJKWHEFJHWEJFSHKJDAHFKJSHDFJKHSJKHF'

class UserSub(FlaskForm):
    class Meta:
        locales = ['pt_BR', 'pt']
        def get_translations(self, form):
            return super(FlaskForm.Meta, self).get_translations(form)
    complete_name = StringField(label=('Nome Completo:'),
        validators=[DataRequired(),
        Length(max=64)])
    social_name = StringField(label=('nome social:'),
        validators=[DataRequired(),
        Length(max=64)])
    age = StringField(label=('Idade:'),
        validators=[DataRequired(),
        Length(max=2)])

    birth_date = DateField(label=('Data de nascimento:'),
        format='%d/%m/%Y',
        validators=[DataRequired()], )

    raca_cor_etinia = SelectField(u'Raça/Cor/Etinia:',
        choices=[('0', ''), ('1', 'Amarela(o)'),('2', 'Branca(o)'), ('3', 'Cigana(o)'),
                ('4', 'Indigena'), ('5', 'parda(o)'), ('6', 'Preta(o)')],
        validators=[DataRequired()], )

    gender = SelectField(u'Gênero:',
        choices=[('0', ''),('1', 'Masculino'), ('2', 'Feminino'), ('3', 'Trangênero'),
                ('4', 'Não-binário')],
        validators=[DataRequired()], )

    marital_status = SelectField(u'Estado Civil:',
        choices=[('0', ''),('1', 'Desquitado(a)'), ('2', 'Divorciado(a)'), ('3', 'Separado(a)'),
                ('4', 'Solteiro(a)'),('4', 'União estavel'),('4', 'Viúvo(a)')],
        validators=[DataRequired()], )

    nacionality = StringField(label=('Nacionalidade:'),
        validators=[DataRequired(),
        Length(max=64)])

    state = StringField(label=('Estado:'),
        validators=[DataRequired(),
        Length(max=64)])

    city = StringField(label=('Cidade:'),
        validators=[DataRequired(),
        Length(max=64)])

    rg = StringField(label=('RG:'),
        validators=[DataRequired(),
        Length(max=12)])

    shipping_date_rg = DateField(label=('Data de expedição:'),
        format='%d/%m/%Y',
        validators=[DataRequired()], )

    shipper_rg  = StringField(label=('Expedidor:'),
        validators=[DataRequired(),
        Length(max=64)])

    cpf = StringField(label=('CPF:'),
        validators=[DataRequired(),
        Length(max=14)])

    cnh = StringField(label=('CNH'),
        validators=[DataRequired(),
        Length(max=14)])

    cep = StringField(label=('Cep'),
        validators=[DataRequired(),
        Length(max=9)])

    address = StringField(label=('Endereço'),
        validators=[DataRequired(),
        Length(max=64)])

    house_number = StringField(label=('Número da casa:'),
        validators=[DataRequired(),
        Length(max=6)])

    complement_address = StringField(label=('Complemento'),
        validators=[DataRequired(),
        Length(max=64)])

    tel = StringField(label=('Telefone pessoal'),
        validators=[DataRequired(),
        Length(max=64)])


    tel_message = StringField(label=('Telefone para Recado'),
        validators=[DataRequired(),
        Length(max=64)])

    personal_email = StringField(label=('E-mail pessoal'),
        validators=[DataRequired(),
        Length(max=64)])


    message_email = StringField(label=('E-mail para Recado'),
        validators=[DataRequired(),
        Length(max=64)])

    school = StringField(label=('Colégio'),
        validators=[DataRequired(),
        Length(max=64)])

    submit = SubmitField(label=('Enviar'))

@app.route('/sub', methods=('GET', 'POST'))
def sub():
    form = UserSub()
    return render_template('formsub.html', form=form)


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


    submit = SubmitField(label=('Enviar'))

@app.route('/registro', methods=('GET', 'POST'))
def register():
    form = CreateUserForm()
    if form.validate_on_submit():
         return redirect(url_for('sub'))
    return render_template('register.html', form=form)

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')