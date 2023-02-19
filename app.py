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
    gender = db.Column(db.Integer(), nullable=True)
    marital_status = db.Column(db.Integer(), nullable=False)
    nacionality = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(1), nullable=False)
    state = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    rg = db.Column(db.String(64), nullable=False)
    shipping_date_rg = db.Column(db.DateTime(80), nullable=False)
    shipper_rg = db.Column(db.String(64), nullable=False)
    cpf = db.Column(db.String(64), nullable=False)
    cnh = db.Column(db.String(64), nullable=False)
    cep = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(64), nullable=False)
    house_number = db.Column(db.String(64), nullable=False)
    complement_address = db.Column(db.String(64), nullable=False)
    tel = db.Column(db.String(64), nullable=False)
    tel_message = db.Column(db.String(64), nullable=False)
    personal_email = db.Column(db.String(64), nullable=False)
    message_email = db.Column(db.String(64), nullable=False)
    scholarity_progress = db.Column(db.Integer(1), nullable=True)






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
        choices=[('', ''), ('AMARELA', 'Amarela(o)'),('BRANCA', 'Branca(o)'), ('CIGANA', 'Cigana(o)'),
                ('INDIGENA', 'Indigena'), ('PARDA', 'parda(o)'), ('PRETA', 'Preta(o)')],
        validators=[], )

    gender = SelectField(u'Gênero:',
        choices=[('', ''),('MASC', 'Masculino'), ('FEMININO', 'Feminino'), ('TRANS', 'Trangênero'),
                ('NAOBINARIO', 'Não-binário')],
        validators=[], )

    marital_status = SelectField(u'Estado Civil:',
        choices=[('', ''),('DESQUITADO', 'Desquitado(a)'), ('DESQUITADO', 'Divorciad(a)'), ('SEPARADO', 'Separado(a)'),
                ('SOLTEIRO', 'Solteiro(a)'),('UNIAOESTAVEL', 'União estavel'),('VIUVO', 'Viúvo(a)')],
        validators=[], )

    nacionality = StringField(label=('Nacionalidade:'),
        validators=[Length(max=64)])

    nacionality_br = RadioField(label=
        'Naturalizado Brasileiro?', choices=[('S', 'Sim'), ('N', 'Não')])

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

    scholarity_progress = RadioField(label='Ensino Médio', choices=[('NCONCLUIDO', 'Não concluído'), ('EMANDAMENTO', 'Em andamento'),('CONCLUIDO', 'Concluído')])

    school_term = RadioField(label='Período escolar', choices=[('MANHA', 'Manhã'), ('TARDE', 'Tarde'), ('NOTURNO', 'Noturno')])

    school = StringField(label=('Colégio:'),
        validators=[Length(max=64)])
#health#

    pwd_person = RadioField(label='Portador de alguma deficiência?', choices=[('S', 'Sim'), ('N', 'Não')])

    pwd_person_affirmative = StringField(label=('Caso sim especifique'),
        validators=[Length(max=64)])

    carrier_of_chronic_disease = RadioField(label='Portador de alguma doença crônica?', choices=[('1', 'Sim'), ('2', 'Não')])

    carrier_of_chronic_disease_affirmative = StringField(label=('Caso sim especifique'),
        validators=[Length(max=64)])

    vaccine_covid = SelectField(u'Vacina Covid:', choices=[('0', ''), ('1', 'Primeira dose'), ('2', 'Segunda dose'),('3', 'Terceira dose'), ('4', 'Quarta dose')],
        validators=[], )

#info of family composition#
    mame_mom = StringField(label=('Nome da Mãe'),
        validators=[Length(max=64)])

    profession_mom = StringField(label=('Profissão da Mãe'),
        validators=[Length(max=64)])

    scholarity_mom = SelectField(u'Escolaridade da Mãe:', choices=[('0', ''), ('1', 'Lê e escreve '), ('2', 'Ensino Fundamental completo '),('3', 'Ensino Fundamental incompleto '), ('4', 'Ensino Médio completo ')
    , ('5', 'Ensino Médio incompleto '), ('6', 'Terceiro Grau completo'),('7', 'Terceiro Grau incompleto'), ('8', 'Pós-graduação completo'),('9', 'Pós-graduação incompleto')],
        validators=[], )

    mame_dad = StringField(label=('Nome do Pai'),
        validators=[Length(max=64)])

    profession_dad = StringField(label=('Profissão do Pai'),
        validators=[Length(max=64)])

    scholarity_dad = SelectField(u'Escolaridade do Pai:',choices=[('0', ''), ('1', 'Lê e escreve '), ('2', 'Ensino Fundamental completo '),('3', 'Ensino Fundamental incompleto '), ('4', 'Ensino Médio completo ')
    , ('5', 'Ensino Médio incompleto '), ('6', 'Terceiro Grau completo'),('7', 'Terceiro Grau incompleto'), ('8', 'Pós-graduação completo'),('9', 'Pós-graduação incompleto')],
        validators=[], )

    children = RadioField(label='Tem filhos?', choices=[('S', 'Sim'), ('N', 'Não')])

    many_childrens =  StringField(label=('Quantos Filhos?'),
        validators=[Length(max=64)])

    live_whith_parents = RadioField(label='Mora com seus pais?', choices=[('S', 'Sim'), ('N', 'Não')])

    lives_whith_other_family = StringField(label=('Caso não especifique'),
        validators=[Length(max=64)])

    many_people_live_house = StringField(label=('Quantas pessoas moram na sua casa?'),
        validators=[Length(max=64)])

    member_family_name = StringField(label=('Nome'),
        validators=[Length(max=64)])

    degree_of_kinship = SelectField(u'Grau de parentesco:', choices=[('', ''), ('MAEPAI', 'Mãe/pai'), ('IRMAOIRMA', 'irmão/irmã'),('AVOVO', 'Avô/Avó'),('TIATIO', 'Tia/Tio')],
        validators=[], )

    age_member_family = StringField(label=('Idade'),
        validators=[Length(max=64)])

    income_member_family = StringField(label=('Caso trabalhe informe o valor da renda'),
        validators=[Length(max=64)])

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
        marital_status = request.form['marital_status']
        nacionality = request.form['nacionality']
        state = request.form['state']
        city = request.form['city']
        rg = request.form['rg']
        shipping_date_rg = request.form['shipping_date_rg']
        cpf = request.form['cpf']
        cnh = request.form['cnh']
        cep = request.form['cep']
        address = request.form['address']
        house_number = request.form['house_number']
        complement_address = request.form['complement_address']
        tel = request.form['tel']
        tel_message = request.form['tel_message']
        personal_email = request.form['personal_email']
        message_email = request.form['message_email']


        gender = request.form['gender']
        student = Student(complete_name=complete_name,
                          social_name=social_name,
                          birth_date=birth_date,
                          raca_cor_etinia=raca_cor_etinia,
                          gender=gender,
                          marital_status=marital_status,
                          nacionality=nacionality,
                          state=state,
                          city=city,
                          rg=rg,
                          shipping_date_rg=shipping_date_rg,
                          shipper_rg=shipper_rg,
                          cpf=cpf,
                          cnh=cnh,
                          cep=cep,
                          address=address,
                          house_number=house_number,
                          complement_address=complement_address,
                          tel=tel,
                          tel_message=tel_message,
                          personal_email=personal_email,
                          message_email=message_email,


                          )

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
            gender = request.form.get('gender')
            marital_status = request.form.get('marital_status')
            nacionality = request.form.get('nacionality')
            state = request.form.get('state')
            city = request.form.get('city')
            rg = request.form.get('rg')
            shipping_date_rg = request.form.get('shipping_date_rg')
            shipper_rg = request.form.get('shipper_rg')
            cpf = request.form.get('cpf')
            cnh = request.form.get('cnh')
            cep = request.form.get('cep')
            address = request.form.get('address')
            house_number = request.form.get('house_number')
            complement_address = request.form.get('complement_address')
            tel = request.form.get('tel')
            tel_message = tel_message
            personal_email = personal_email

            student.social_name = social_name
            student.birth_date = birth_date
            student.raca_cor_etinia = raca_cor_etinia
            student.gender = gender
            student.marital_status = marital_status
            student.nacionality = nacionality
            student.state = state
            student.city = city
            student.rg = rg
            student.shipping_date_rg = shipping_date_rg
            student.shipper_rg = shipper_rg
            student.cpf = cpf
            student.cnh = cnh
            student.cep = cep
            student.address = address
            student.house_number = house_number
            student.complement_address = complement_address
            student.tel = tel
            student.tel_message = tel_message
            student.personal_email = personal_email



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

class UserLogin(FlaskForm):
    class Meta:
        locales = ['pt_BR', 'pt']
        def get_translations(self, form):
            return super(FlaskForm.Meta, self).get_translations(form)
    email_login = StringField(label=('E-mail'),
        validators=[DataRequired(),
        Email(),
        Length(max=120)])
    password_login = PasswordField(label=('Senha'),
        validators=[DataRequired(),
        Length(min=8, message='A senha deve ter no mínimo %(min)d caracteres.')])



    submit = SubmitField(label=('Enviar'))


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = UserLogin()
    return render_template('login.html', form=form)







@app.route('/user/register', methods=('GET', 'POST'))
def register():
    form = CreateUserForm()
    if form.validate_on_submit():
         return redirect(url_for('student_create'))
    return render_template('register.html', form=form)

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html',)

