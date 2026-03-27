from flask import Flask, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "logan_secret"

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.String(50))
    desc = db.Column(db.String(200))

# Create DB
with app.app_context():
    db.create_all()

# HOME
@app.route('/')
def home():
    accounts = Account.query.all()
    items = ""

    for acc in accounts:
        msg = f"Hello 🤍, I’m interested in {acc.name} ({acc.price}) 🩵. Please guide me 🤗"
        link = f"https://wa.me/231887935222?text={msg}"

        items += f"""
        <div class='card'>
            <h3>{acc.name}</h3>
            <p>{acc.desc}</p>
            <h2>{acc.price}</h2>
            <a href="{link}" target="_blank">
                <button>Buy 💬</button>
            </a>
        </div>
        """

    return f"""
    <html>
    <head>
    <style>
    body {{
        margin:0;
        font-family: Arial;
        background: url('https://i.imgur.com/8Km9tLL.jpeg') no-repeat center/cover;
        color:white;
        text-align:center;
    }}

    h1 {{
        font-size:50px;
        color:#00ffc3;
        text-shadow:0 0 20px #00ffc3;
    }}

    .card {{
        background:rgba(0,0,0,0.6);
        margin:20px;
        padding:20px;
        border-radius:15px;
    }}

    button {{
        padding:10px 20px;
        background:#00ffc3;
        border:none;
        border-radius:10px;
        cursor:pointer;
    }}

    .top {{
        margin-top:40px;
    }}

    a {{
        color:white;
    }}
    </style>
    </head>

    <body>

    <h1>🔥 LOGAN EFB STORE 🔥</h1>
    <p>Buy • Sell • Trade • Exchange eFootball Accounts</p>

    <div class="top">
        <a href="/login">Login</a> | 
        <a href="/register">Register</a>
    </div>

    {items}

    </body>
    </html>
    """

# REGISTER
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user = User(
            name=request.form['name'],
            email=request.form['email'],
            password=request.form['password']
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/login')

    return """
    <h2>Register</h2>
    <form method="post">
        <input name="name" placeholder="Name"><br>
        <input name="email" placeholder="Email"><br>
        <input name="password" placeholder="Password"><br>
        <button>Register</button>
    </form>
    """

# LOGIN
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            email=request.form['email'],
            password=request.form['password']
        ).first()

        if user:
            session['user'] = user.email
            return redirect('/')

    return """
    <h2>Login</h2>
    <form method="post">
        <input name="email"><br>
        <input name="password"><br>
        <button>Login</button>
    </form>
    """

# ADMIN PANEL
@app.route('/admin', methods=['GET','POST'])
def admin():
    if 'user' not in session or session['user'] != "admin@gmail.com":
        return "Access Denied ❌"

    if request.method == 'POST':
        acc = Account(
            name=request.form['name'],
            price=request.form['price'],
            desc=request.form['desc']
        )
        db.session.add(acc)
        db.session.commit()
        return redirect('/admin')

    return """
    <h2>Admin Panel 👑</h2>
    <form method="post">
        <input name="name" placeholder="Account Name"><br>
        <input name="price" placeholder="Price"><br>
        <input name="desc" placeholder="Description"><br>
        <button>Add</button>
    </form>
    """

# LOGOUT
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

# RUN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)