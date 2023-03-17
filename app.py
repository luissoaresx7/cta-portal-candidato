from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, SelectField, DateField, RadioField
from wtforms.validators import ValidationError, DataRequired, \
    Email, EqualTo, Length
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__, template_folder='templates')
SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'QWKLWJKWHEFJHWEJFSHKJDAHFKJSHDFJKHSJKHF'
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50), index=True, unique=True)
  email = db.Column(db.String(150), unique=True, index=True)
  password_hash = db.Column(db.String(150))
  joined_at = db.Column(db.DateTime(), default=datetime.utcnow, index=True)

  def set_password(self, password):
        self.password_hash = generate_password_hash(password)

  def check_password(self, password):
      return check_password_hash(self.password_hash, password)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    complete_name = db.Column(db.String(64), nullable=True)
    social_name = db.Column(db.String(64), nullable=True)
    birth_date = db.Column(db.DateTime(80), nullable=True)
    raca_cor_etinia = db.Column(db.Integer(), nullable=True)
    gender = db.Column(db.Integer(), nullable=True)
    marital_status = db.Column(db.Integer(), nullable=True)
    nacionality = db.Column(db.String(64), nullable=True)
    state = db.Column(db.String(64), nullable=True)
    city = db.Column(db.String(64), nullable=True)
    rg = db.Column(db.String(64), nullable=True)
    shipping_date_rg = db.Column(db.DateTime(80), nullable=True)
    shipper_rg = db.Column(db.String(64), nullable=True)
    cpf = db.Column(db.String(64), nullable=True)
    cnh = db.Column(db.String(64), nullable=True)
    cep = db.Column(db.String(64), nullable=True)
    address = db.Column(db.String(64), nullable=True)
    house_number = db.Column(db.String(64), nullable=True)
    complement_address = db.Column(db.String(64), nullable=True)
    tel = db.Column(db.String(64), nullable=True)
    tel_message = db.Column(db.String(64), nullable=True)
    personal_email = db.Column(db.String(64), nullable=True)
    message_email = db.Column(db.String(64), nullable=True)
    scholarity_progress = db.Column(db.Integer(), nullable=True)
    school_term = db.Column(db.String(16), nullable=True)
    school = db.Column(db.String(64), nullable=True)
    pwd_person = db.Column(db.String(1), nullable=True)
    pwd_person_affirmative = db.Column(db.String(64), nullable=True)
    carrier_of_chronic_disease = db.Column(db.String(1), nullable=True)
    carrier_of_chronic_disease_affirmative = db.Column(db.String(64), nullable=True)
    vaccine_covid = db.Column(db.String(16), nullable=True)
    name_mom = db.Column(db.String(64), nullable=True)
    profession_mom = db.Column(db.String(64), nullable=True)
    scholarity_mom = db.Column(db.String(16), nullable=True)
    name_dad = db.Column(db.String(64), nullable=False)
    profession_dad = db.Column(db.String(64), nullable=True)
    scholarity_dad = db.Column(db.String(16), nullable=True)
    children = db.Column(db.String(1), nullable=True)
    many_children = db.Column(db.String(64), nullable=True)
    live_with_parents = db.Column(db.String(1), nullable=True)
    lives_with_other_family = db.Column(db.String(64), nullable=True)
    many_people_live_house = db.Column(db.String(64), nullable=True)
    member_family_name = db.Column(db.String(64), nullable=True)
    degree_of_kinship = db.Column(db.Integer(), nullable=True)
    age_member_family = db.Column(db.String(64), nullable=True)
    income_member_family = db.Column(db.String(64), nullable=True)

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
        choices=[('', ''),('DESQUITADO', 'Desquitado(a)'), ('DESQUITADO', 'Divorciado(a)'), ('SEPARADO', 'Separado(a)'),
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

    carrier_of_chronic_disease = RadioField(label='Portador de alguma doença crônica?', choices=[('S', 'Sim'), ('N', 'Não')])

    carrier_of_chronic_disease_affirmative = StringField(label=('Caso sim especifique'),
        validators=[Length(max=64)])

    vaccine_covid = SelectField(u'Vacina Covid:', choices=[('', ''), ('PRIMEIRADOSE', 'Primeira dose'), ('SEGUNDADOSE', 'Segunda dose'),('TERCEIRADOSE', 'Terceira dose'), ('QUARTADOSE', 'Quarta dose')],
        validators=[], )

#info of family composition#
    name_mom = StringField(label=('Nome da Mãe'),
        validators=[Length(max=64)])

    profession_mom = StringField(label=('Profissão da Mãe'),
        validators=[Length(max=64)])

    scholarity_mom = SelectField(u'Escolaridade do Pai:',choices=[('', ''), ('LE_ESCREVE', 'Lê e escreve '), ('EF_COMPLETO', 'Ensino Fundamental completo '),('EF_INCOMPLETO', 'Ensino Fundamental incompleto '), ('EM_COMPLETO', 'Ensino Médio completo ')
    , ('EM_INCOMPLETO', 'Ensino Médio incompleto '), ('SP_COMPLETO', 'Superior completo'),('SP_INCOMPLETO', 'Superior incompleto'), ('PG_COMPLETO', 'Pós-graduação completo'),('PG_INCOMPLETO', 'Pós-graduação incompleto')],
        validators=[], )

    name_dad = StringField(label=('Nome do Pai'),
        validators=[Length(max=64)])

    profession_dad = StringField(label=('Profissão do Pai'),
        validators=[Length(max=64)])

    scholarity_dad = SelectField(u'Escolaridade do Pai:',choices=[('', ''), ('LE_ESCREVE', 'Lê e escreve '), ('EF_COMPLETO', 'Ensino Fundamental completo '),('EF_INCOMPLETO', 'Ensino Fundamental incompleto '), ('EM_COMPLETO', 'Ensino Médio completo ')
    , ('EM_INCOMPLETO', 'Ensino Médio incompleto '), ('SP_COMPLETO', 'Superior completo'),('SP_INCOMPLETO', 'Superior incompleto'), ('PG_COMPLETO', 'Pós-graduação completo'),('PG_INCOMPLETO', 'Pós-graduação incompleto')],
        validators=[], )

    children = RadioField(label='Tem filhos?', choices=[('S', 'Sim'), ('N', 'Não')])

    many_children =  StringField(label=('Quantos Filhos?'),
        validators=[Length(max=64)])

    live_with_parents = RadioField(label='Mora com seus pais?', choices=[('S', 'Sim'), ('N', 'Não')])

    lives_with_other_family = StringField(label=('Caso não especifique'),
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

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/student/register', methods=('GET', 'POST'))
def student_create():
    form = UserSub()
    if request.method == 'POST':
        complete_name = request.form['complete_name']
        social_name = request.form['social_name']
        birth_date_str = request.form['birth_date']
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
        raca_cor_etinia = request.form['raca_cor_etinia']
        marital_status = request.form['marital_status']
        nacionality = request.form['nacionality']
        state = request.form['state']
        city = request.form['city']
        rg = request.form['rg']
        shipping_date_rg_str = request.form['shipping_date_rg']
        shipping_date_rg = datetime.strptime(shipping_date_rg_str, "%Y-%m-%d").date() if shipping_date_rg_str else None
        shipper_rg = request.form['shipper_rg']
        try:
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
            school_term = request.form['school_term'] if 'school_term' in request.form else None
            school = request.form['school']
            if 'pwd_person' in request.form:
                pwd_person = request.form['pwd_person']
            else:
                pwd_person = ''
            pwd_person_affirmative = request.form['pwd_person_affirmative'] if 'pwd_person_affirmative' in request.form else None
            carrier_of_chronic_disease = request.form['carrier_of_chronic_disease'] if 'carrier_of_chronic_disease' in request.form else None
            carrier_of_chronic_disease_affirmative = request.form['carrier_of_chronic_disease_affirmative']
            vaccine_covid = request.form['vaccine_covid']
            name_mom = request.form['name_mom']
            profession_mom = request.form['profession_mom']
            scholarity_mom = request.form['scholarity_mom']
            name_dad = request.form['name_dad']
            profession_dad = request.form['profession_dad']
            scholarity_dad = request.form['scholarity_dad']
            children = request.form['children'] if 'children' in request.form else None
            many_children = request.form['many_children']
            live_with_parents = request.form['live_with_parents'] if 'live_with_parents' in request.form else None
            lives_with_other_family = request.form['lives_with_other_family']
            many_people_live_house = request.form['many_people_live_house']
            member_family_name = request.form['member_family_name']
            degree_of_kinship = request.form['degree_of_kinship']
            age_member_family = request.form['age_member_family']
            income_member_family = request.form['income_member_family']
        except Exception as e:
            print(e)

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
                          school_term=school_term,
                          school=school,
                          pwd_person=pwd_person,
                          pwd_person_affirmative=pwd_person_affirmative,
                          carrier_of_chronic_disease=carrier_of_chronic_disease,
                          carrier_of_chronic_disease_affirmative=carrier_of_chronic_disease_affirmative,
                          vaccine_covid=vaccine_covid,
                          name_mom=name_mom,
                          profession_mom=profession_mom,
                          scholarity_mom=scholarity_mom,
                          name_dad=name_dad,
                          profession_dad=profession_dad,
                          scholarity_dad=scholarity_dad,
                          children=children,
                          many_children=many_children,
                          live_with_parents=live_with_parents,
                          lives_with_other_family=lives_with_other_family,
                          many_people_live_house=many_people_live_house,
                          member_family_name=member_family_name,
                          degree_of_kinship=degree_of_kinship,
                          age_member_family=age_member_family,
                          income_member_family=income_member_family
                          )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('student_edit', student_id=student.id))
    return render_template('formsub.html', form=form)

@app.route('/student/<int:student_id>/edit/', methods=('GET', 'POST'))
def student_edit(student_id):
    student = Student.query.get_or_404(student_id)
    if request.method == 'POST':
        try:
            social_name = request.form.get('social_name')
            birth_date_str = request.form.get('birth_date')
            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
            raca_cor_etinia = request.form.get('raca_cor_etinia')
            gender = request.form.get('gender')
            marital_status = request.form.get('marital_status')
            nacionality = request.form.get('nacionality')
            state = request.form.get('state')
            city = request.form.get('city')
            rg = request.form.get('rg')
            shipping_date_rg_str = request.form['shipping_date_rg']
            shipping_date_rg = datetime.strptime(shipping_date_rg_str, "%Y-%m-%d").date() if shipping_date_rg_str else None
            shipper_rg = request.form.get('shipper_rg')
            cpf = request.form.get('cpf')
            cnh = request.form.get('cnh')
            cep = request.form.get('cep')
            address = request.form.get('address')
            house_number = request.form.get('house_number')
            complement_address = request.form.get('complement_address')
            tel = request.form.get('tel')
            tel_message = request.form.get('tel_message')
            personal_email = request.form.get('personal_email')
            school_term = request.form.get('school_term')
            school = request.form.get('school')
            pwd_person = request.form.get('pwd_person')
            pwd_person_affirmative = request.form.get('pwd_person_affirmative')
            carrier_of_chronic_disease = request.form.get('carrier_of_chronic_disease')
            carrier_of_chronic_disease_affirmative = request.form.get('carrier_of_chronic_disease_affirmative')
            vaccine_covid = request.form.get('vaccine_covid')
            name_mom = request.form.get('name_mom')
            profession_mom = request.form.get('profession_mom')
            scholarity_mom = request.form.get('scholarity_mom')
            name_dad = request.form.get('name_dad')
            profession_dad = request.form.get('profession_dad')
            scholarity_dad = request.form.get('scholarity_dad')
            children = request.form.get('children')
            many_children = request.form.get('many_children')
            live_with_parents = request.form.get('live_with_parents')
            lives_with_other_family = request.form.get('lives_with_other_family')
            many_people_live_house = request.form.get('many_people_live_house')
            member_family_name = request.form.get('member_family_name')
            degree_of_kinship = request.form.get('degree_of_kinship')
            age_member_family = request.form.get('age_member_family')
            income_member_family = request.form.get('income_member_family')

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
            student.school_term = school_term
            student.school = school
            student.pwd_person = pwd_person
            student.pwd_person_affirmative = pwd_person_affirmative
            student.carrier_of_chronic_disease = carrier_of_chronic_disease
            student.carrier_of_chronic_disease_affirmative = carrier_of_chronic_disease_affirmative
            student.vaccine_covid = vaccine_covid
            student.name_mom = name_mom
            student.profession_mom = profession_mom
            student.scholarity_mom = scholarity_mom
            student.name_dad = name_dad
            student.profession_dad = profession_dad
            student.scholarity_dad = scholarity_dad
            student.children = children
            student.many_children = many_children
            student.live_with_parents = live_with_parents
            student.lives_with_other_family = lives_with_other_family
            student.many_people_live_house = many_people_live_house
            student.member_family_name = member_family_name
            student.degree_of_kinship = degree_of_kinship
            student.age_member_family = age_member_family
            student.income_member_family = income_member_family

            db.session.add(student)
            db.session.commit()

            return redirect(url_for('student_edit', student_id=student.id))
        except Exception as ex:
            print(ex)

    form = UserSub(obj=student)
    return render_template('formsub_edit.html', form=form)

#REGISSTER#
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
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


#LOGIN#
class UserLogin(FlaskForm):
    class Meta:
        locales = ['pt_BR', 'pt']
        def get_translations(self, form):
            return super(FlaskForm.Meta, self).get_translations(form)
    email = StringField(label=('E-mail'),
        validators=[DataRequired(),
        Email(),
        Length(max=120)])
    password = PasswordField(label=('Senha'),
        validators=[DataRequired(),
        Length(min=8, message='A senha deve ter no mínimo %(min)d caracteres.')])

    submit = SubmitField(label=('Enviar'))

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = UserLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for('index'))
        flash('E-mail ou senha inválida.')
    return render_template('login.html', form=form)

#INDEX#
@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html',)

@app.route("/logout")
# @login_required
def logout():
    logout_user()
    return redirect(url_for('index'))