from flask import Flask, render_template, request, flash, redirect, url_for
from sqlalchemy.exc import SQLAlchemyError

from api_routes import routes
from database import db_session, Funcionario
from sqlalchemy import select, and_, func
from flask_login import LoginManager, login_required, login_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'senaisp'

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/calculos')
def calculos():
    return render_template("calculos.html")


@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")


@app.route('/geometria')
def geometria():
    return render_template("geometria.html")


@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            flash("soma realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:
            # passo 1: emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar a soma", 'alert-danger')
    return render_template("operacoes.html")


@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtrair = n1 - n2
            return render_template("operacoes.html", n1=n1, n2=n2, subtrair=subtrair)

    return render_template("operacoes.html")


@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multiplicar = n1 * n2
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicar=multiplicar)

    return render_template("operacoes.html")


@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            dividir = n1 / n2
            return render_template("operacoes.html", n1=n1, n2=n2, dividir=dividir)

    return render_template("operacoes.html")


@app.route('/triangulo_perimetro', methods=['GET', 'POST'])
def triangulo_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            perimetro = n1 + n1 + n1
            return render_template("geometria.html", n1=n1, perimetro=perimetro)
        else:
            # passo 1: emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar o perimetro", 'alert-danger')
    return render_template("geometria.html")

    return render_template("geometria.html")


@app.route('/triangulo_area', methods=['GET', 'POST'])
def triangulo_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            area = (n1 * n1) / 2
            return render_template("geometria.html", n1=n1, area=area)
        else:
            # passo 1: emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar a area", 'alert-danger')
    return render_template("geometria.html")

    return render_template("geometria.html")


@app.route('/circulo_perimetro', methods=['GET', 'POST'])
def circulo_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            perimetro2 = 2 * 3, 14 * n1
            return render_template("geometria.html", n1=n1, perimetro2=perimetro2)
        else:
            # passo 1: emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar o perimetro", 'alert-danger')
    return render_template("geometria.html")

    return render_template("geometria.html")


@app.route('/circulo_area', methods=['GET', 'POST'])
def circulo_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            area2 = 3, 14 * n1 ** 2
            return render_template("geometria.html", n1=n1, area2=area2)
        else:
            # passo 1: emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar a area", 'alert-danger')
    return render_template("geometria.html")


@app.route('/quadrado_perimetro', methods=['GET', 'POST'])
def quadrado_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            perimetro3 = n1 + n1 + n1 + n1
            return render_template("geometria.html", n1=n1, perimetro3=perimetro3)
        else:
            # passo 1: emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar o perimetro", 'alert-danger')
    return render_template("geometria.html")


@app.route('/quadrado_area', methods=['GET', 'POST'])
def quadrado_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            area3 = n1 * n1
            return render_template("geometria.html", n1=n1, area3=area3)
        else:
            # passo 1: emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar a area", 'alert-danger')
    return render_template("geometria.html")


@app.route('/hexagono_perimetro', methods=['GET', 'POST'])
def hexagono_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            perimetro4 = n1 + n1 + n1 + n1 + n1 + n1
            return render_template("geometria.html", n1=n1, perimetro4=perimetro4)
        else:
            # passo 1: emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar o perimetro", 'alert-danger')
    return render_template("geometria.html")


@app.route('/hexagono_area', methods=['GET', 'POST'])
def hexagono_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            area4 = ((n1 * n1) / 2) * 6
            return render_template("geometria.html", n1=n1, area4=area4)
        else:
            # passo 1: emitir a mensagem e a categoria do flash
            flash("preencha o campo para realizar a area", 'alert-danger')
    return render_template("geometria.html")


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@login_manager.user_loader
def load_user(user_id):
    user = select(Funcionario).where(Funcionario.id == int(user_id))
    resultado = db_session.execute(user).scalar_one_or_none()
    return resultado


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/teste', methods=['GET'])
def teste_():
    return render_template('teste.html')


@app.route('/logar', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')
        ''' verificação usando not
        if not email or not senha:
            flash('preencher todos os campos!', 'danger')
            return render_template('login.html')
        '''
        if not email or not senha:
            flash(f'preencher todos os campos!', 'alert-danger')
            return render_template('login.html')

        else:
            verificar_email = select(Funcionario).where(Funcionario.email == email)
            resultado_email = db_session.execute(verificar_email).scalar_one_or_none()

            if resultado_email:
                # se encontrado na base da dados
                if resultado_email.check_password(senha):
                    # login correto
                    login_user(resultado_email)
                    flash(f'Login com sucesso!', 'success')
                    return redirect(url_for('home'))
                else:
                    # login incorreto
                    flash('email incorreta!', 'danger')
                    return render_template('login.html')

            else:
                # se nao encontrado
                flash(f'email não encontrado!', 'danger')
                return render_template('login.html')

    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('index'))


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastro_funcionario():
    if request.method == 'POST':
        nome = request.form.get('form-nome')
        data_nascimento = request.form.get('form-nascimento')
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')
        cpf = request.form.get('form-cpf')
        cargo = request.form.get('form-cargo')
        salario = float(request.form.get('form-salario'))
        if not nome or not data_nascimento or not email or not senha or not cpf or not salario or not cargo:
            flash('preencher todos os campos!', 'danger')
            return render_template('login.html')
        ver_email = select(Funcionario).where(Funcionario.email == email)
        exist_email = db_session.execute(ver_email).scalar_one_or_none()
        if exist_email:
            flash(f'email: {email} ja esta cadastrado!', 'danger')
            return render_template('login.html')
        try:
            new_user = Funcionario(nome=nome, data_nascimento=data_nascimento, email=email, cpf=cpf, salario=salario,
                                    cargo=cargo)
            new_user.set_password(senha)
            db_session.add(new_user)
            db_session.commit()
            flash(f'usuario: {nome} cadastrado com sucesso!', 'success')
            print('cadastrado com sucesso!')
            return redirect(url_for('login'))
        except SQLAlchemyError as e:
            flash(f'erro na base de dados', 'danger')
            print(f'erro na base de dados {e}')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Error:', 'danger')
            print(f'Erro {e}')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/funcionarios')
@login_required
def funcionarios():
    ver_email = select(Funcionario)
    result_email = db_session.execute(ver_email).scalars().all()
    return render_template('funcionarios.html', lista_funcionarios=result_email)

@app.route('/animais')
def animais():
    return render_template('animais.html')


@app.route('/gatos')
def listar_gatos():
    gatos = routes.get_gatos()
    return render_template('gatos.html', gatos=gatos)

# TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)

