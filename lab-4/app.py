from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supa-pupa-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация базы данных
db = SQLAlchemy(app)

# Инициализация Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_page'
login_manager.login_message = 'Пожалуйста, авторизуйтесь для доступа к этой странице'

# Модель пользователя на основе UserMixin
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Создание таблиц базы данных
with app.app_context():
    db.create_all()

# Эндпоинты

# Корневой эндпоинт
@app.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('index.html', user=current_user)


# Страница входа и обработка POST запроса
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        return render_template('login.html')   
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Проверка обязательных полей
        if not email or not password:
            flash('Пожалуйста, заполните все поля', 'error')
            return render_template('login.html')
        
        # Поиск пользователя по email
        user = User.query.filter_by(email=email).first()
        
        if not user:
            flash('Пользователь с таким email не найден', 'error')
            return render_template('login.html')
        
        # Проверяем пароль
        if not check_password_hash(user.password, password):
            flash('Неверный пароль', 'error')
            return render_template('login.html')
        
        # Если все проверки пройдены, авторизуем пользователя
        login_user(user)
        flash(f'Добро пожаловать, {user.name}!', 'success')
        return redirect(url_for('index'))


# Страница регистрации и обработка POST запроса
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        return render_template('signup.html')
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Проверка обязательных полей
        if not name or not email or not password:
            flash('Пожалуйста, заполните все поля', 'error')
            return render_template('signup.html')
        
       # Проверяем, существует ли пользователь с таким email
        existing_user = User.query.filter_by(email=email).first()
        
        if existing_user:
            flash('Пользователь с таким email уже существует', 'error')
            return render_template('signup.html')
        
        # Регистрируем нового пользователя
        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password, name=name)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Вы зарегистрированы!', 'success')
        return redirect(url_for('login'))
    

@app.route('/logout')
def logout():
    # Выход из системы
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)