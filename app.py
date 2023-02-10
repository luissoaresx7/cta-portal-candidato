from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, SelectField, DateField, RadioField
from wtforms.validators import ValidationError, DataRequired, \
    Email, EqualTo, Length
import os, datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates')
SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'QWKLWJKWHEFJHWEJFSHKJDAHFKJSHDFJKHSJKHF'
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    complete_name = db.Column(db.String(64), nullable=False)
    social_name = db.Column(db.String(64), nullable=True)
    birth_date = db.Column(db.DateTime(80), nullable=False)
    raca_cor_etinia = db.Column(db.Integer(), nullable=True)

    def __repr__(self):
        return f'<Student {self.complete_name}>'

class UserSub(FlaskForm):
    class Meta:
        locales = ['pt_BR', 'pt']
        def get_translations(self, form):
            return super(FlaskForm.Meta, self).get_translations(form)
    complete_name = StringField(label=('Nome Completo:'),
        validators=[DataRequired(),
        Length(max=64)])

    social_name = StringField(label=('Nome social:'),
        validators=[Length(max=64)])

    birth_date = DateField(label=('Data de nascimento:'),
        format='%d/%m/%Y',
        validators=[DataRequired()], )

    raca_cor_etinia = SelectField(u'Raça/Cor/Etinia:',
        choices=[('0', ''), ('1', 'Amarela(o)'),('2', 'Branca(o)'), ('3', 'Cigana(o)'),
                ('4', 'Indigena'), ('5', 'parda(o)'), ('6', 'Preta(o)')],
        validators=[], )

    gender = SelectField(u'Gênero:',
        choices=[('0', ''),('1', 'Masculino'), ('2', 'Feminino'), ('3', 'Trangênero'),
                ('4', 'Não-binário')],
        validators=[], )

    marital_status = SelectField(u'Estado Civil:',
        choices=[('0', ''),('1', 'Desquitado(a)'), ('2', 'Divorciado(a)'), ('3', 'Separado(a)'),
                ('4', 'Solteiro(a)'),('4', 'União estavel'),('4', 'Viúvo(a)')],
        validators=[], )

    nacionality = StringField(label=('Nacionalidade:'),
        validators=[Length(max=64)])

    state = StringField(label=('Estado:'),
        validators=[Length(max=64)])

    city = StringField(label=('Cidade:'),
        validators=[Length(max=64)])

    rg = StringField(label=('RG:'),
        validators=[Length(max=12)])

    shipping_date_rg = DateField(label=('Data de expedição:'),
        format='%d/%m/%Y',
        validators=[], )

    shipper_rg  = StringField(label=('Expedidor:'),
        validators=[Length(max=64)])

    cpf = StringField(label=('CPF:'),
        validators=[Length(max=14)])

    cnh = StringField(label=('CNH'),
        validators=[Length(max=14)])

    cep = StringField(label=('Cep'),
        validators=[Length(max=9)])

    address = StringField(label=('Endereço'),
        validators=[Length(max=64)])

    house_number = StringField(label=('Número da casa:'),
        validators=[Length(max=6)])

    complement_address = StringField(label=('Complemento'),
        validators=[Length(max=64)])

    tel = StringField(label=('Telefone pessoal'),
        validators=[Length(max=64)])


    tel_message = StringField(label=('Telefone para Recado'),
        validators=[Length(max=64)])

    personal_email = StringField(label=('E-mail pessoal'),
        validators=[Length(max=64)])

    message_email = StringField(label=('E-mail para Recado'),
        validators=[Length(max=64)])

    school = StringField(label=('Colégio:'),
        validators=[Length(max=64)])

    vaccine_covid = SelectField(u'Vacina Covid:',
        choices=[('0', ''), ('1', 'Primeira dose'), ('2', 'Segunda dose'),('3', 'Terceira dose'), ('4', 'Quarta dose')],
        validators=[], )

    mame_mom = StringField(label=('Nome da Mãe'),
        validators=[Length(max=64)])

    profession_mom = StringField(label=('Profissão da Mãe'),
        validators=[Length(max=64)])

    scholarity_mom = SelectField(u'Escolaridade da Mãe:',
        choices=[('0', ''), ('1', 'Lê e escreve '), ('2', 'Ensino Fundamental completo '),('3', 'Ensino Fundamental incompleto '), ('4', 'Ensino Médio completo ')
                 , ('5', 'Ensino Médio incompleto '), ('6', 'Terceiro Grau completo'),('7', 'Terceiro Grau incompleto'), ('8', 'Pós-graduação completo'),('9', 'Pós-graduação incompleto')],
        validators=[], )

    mame_dad = StringField(label=('Nome do Pai'),
        validators=[Length(max=64)])

    profession_dad = StringField(label=('Profissão do Pai'),
        validators=[Length(max=64)])

    scholarity_dad = SelectField(u'Escolaridade do Pai:',
        choices=[('0', ''), ('1', 'Lê e escreve '), ('2', 'Ensino Fundamental completo '),('3', 'Ensino Fundamental incompleto '), ('4', 'Ensino Médio completo ')
                 , ('5', 'Ensino Médio incompleto '), ('6', 'Terceiro Grau completo'),('7', 'Terceiro Grau incompleto'), ('8', 'Pós-graduação completo'),('9', 'Pós-graduação incompleto')],
        validators=[], )

    submit = SubmitField(label=('Enviar'))

@app.route('/student/register', methods=('GET', 'POST'))
def student_create():
    form = UserSub()
    if request.method == 'POST':
        complete_name = request.form['complete_name']
        social_name = request.form['social_name']
        birth_date_str = request.form['birth_date']
        birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d").date()
        raca_cor_etinia = request.form['raca_cor_etinia']
        student = Student(complete_name=complete_name,
                          social_name=social_name,
                          birth_date=birth_date,
                          raca_cor_etinia=raca_cor_etinia)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('student_edit', student_id=student.id))
    return render_template('formsub.html', form=form)

@app.route('/student/<int:student_id>/edit/', methods=('GET', 'POST'))
def student_edit(student_id):
    student = Student.query.get_or_404(student_id)
    print(request.method)
    if request.method == 'POST':
        try:
            social_name = request.form.get('social_name')
            birth_date_str = request.form.get('birth_date')
            birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d").date()
            raca_cor_etinia = request.form.get('raca_cor_etinia')

            student.social_name = social_name
            student.birth_date = birth_date
            student.raca_cor_etinia = raca_cor_etinia

            db.session.add(student)
            db.session.commit()

            return redirect(url_for('student_edit', student_id=student.id))
        except Exception as ex:
            print(ex)

    form = UserSub(obj=student)
    return render_template('formsub_edit.html', form=form)

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

@app.route('/user/register', methods=('GET', 'POST'))
def register():
    form = CreateUserForm()
    if form.validate_on_submit():
         return redirect(url_for('student_create'))
    return render_template('register.html', form=form)

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('indexteste.html')