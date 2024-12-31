from flask import Flask, request, jsonify, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import random
import string
from converter import parse_questionnaire

app = Flask(__name__)
CORS(app)
app = Flask(__name__, template_folder='.')

# 配置 Flask 和数据库
app.config['SECRET_KEY'] = 'your_secret_key_here'  # 替换为更复杂的密钥
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# 数据库模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# 数据库初始化
def create_tables():
    db.create_all()

# 生成唯一ID
def generate_unique_id(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


@app.route('/login.html')
def login():
    return render_template('./static/login.html')

@app.route('/register.html')
def register():
    return render_template('./static/register.html')

@app.route('/reset.html')
def reset():
    return render_template('./static/reset.html')



# 用户注册
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"message": "All fields are required"}), 400
    if len(username) > 32 or len(password) < 8 or len(password) > 32:
        return jsonify({"message": "Invalid username or password length"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already registered"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    # 确保生成的ID唯一
    user_id = generate_unique_id()
    while User.query.filter_by(id=user_id).first():  # 检查ID是否已存在
        user_id = generate_unique_id()  # 如果已存在，重新生成ID
    
    new_user = User(id=user_id, username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "user_id": user_id}), 201

# 用户登录
@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "All fields are required"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"message": "Invalid email or password"}), 401

    # 保存登录状态
    session['user_id'] = user.id
    session['username'] = user.username

    return jsonify({"message": "Login successful", "user_id": user.id}), 200

# 重置密码
@app.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    new_password = data.get('new_password')

    if not email or not username or not new_password:
        return jsonify({"message": "All fields are required"}), 400
    if len(new_password) < 8 or len(new_password) > 32:
        return jsonify({"message": "Invalid password length"}), 400

    user = User.query.filter_by(email=email, username=username).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
    user.password = hashed_password
    db.session.commit()
    return jsonify({"message": "Password reset successful"}), 200

# 获取用户信息
@app.route('/profile', methods=['GET'])
def user_profile():
    if 'user_id' not in session:
        return jsonify({"message": "Not logged in"}), 401

    user_id = session['user_id']
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    return jsonify({
        "user_id": user.id,
        "username": user.username,
        "email": user.email
    }), 200

# 用户登出
@app.route('/logout', methods=['POST'])
def logout_user():
    session.clear()  # 清除所有会话数据
    return jsonify({"message": "Logout successful"}), 200

# 主程序入口
if __name__ == '__main__':
    with app.app_context():
        create_tables()
    app.run(debug=True)
