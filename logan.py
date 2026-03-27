from flask import Flask, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

WHATSAPP_NUMBER = "231887935222"

# DATABASE SETUP
def init_db():
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS orders (name TEXT, product TEXT)")
    conn.commit()
    conn.close()

init_db()

def save_order(name, product):
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()
    c.execute("INSERT INTO orders VALUES (?, ?)", (name, product))
    conn.commit()
    conn.close()

def get_orders():
    conn = sqlite3.connect("orders.db")
    c = conn.cursor()
    c.execute("SELECT * FROM orders")
    data = c.fetchall()
    conn.close()
    return data

def wa_link(text):
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={text.replace(' ', '%20')}"

# LOGIN
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("username") == "admin" and request.form.get("password") == "1234":
            session["admin"] = True
            return redirect("/dashboard")

    return '''
    <h2>🔐 Admin Login</h2>
    <form method="POST">
        <input name="username" placeholder="Username"><br><br>
        <input name="password" type="password" placeholder="Password"><br><br>
        <button type="submit">Login</button>
    </form>
    '''

# DASHBOARD
@app.route("/dashboard")
def dashboard():
    if "admin" not in session:
        return redirect("/")

    orders = get_orders()
    order_list = "".join([f"<li>{o[0]} - {o[1]}</li>" for o in orders])

    return f'''
    <h1>📊 Admin Dashboard</h1>
    <ul>{order_list}</ul>
    <a href="/store">Go to Store</a><br><br>
    <a href="/logout">Logout</a>
    '''

# STORE
@app.route("/store", methods=["GET", "POST"])
def store():
    order_link = ""

    if request.method == "POST":
        name = request.form.get("name")
        product = request.form.get("product")

        save_order(name, product)

        message = f"Hello, my name is {name}. I want to order: {product}. I have completed payment."
        order_link = wa_link(message)

    return f'''
    <h1>💙 LOGAN EFB STORE 💙</h1>

    <form method="POST">
        <input name="name" placeholder="Your Name"><br><br>

        <select name="product">
            <option>Premium Account ($20)</option>
            <option>Starter Account ($10)</option>
            <option>Pro Max Account ($35)</option>
        </select><br><br>

        <button type="submit">Place Order</button>
    </form>

    {"<a href='" + order_link + "'>📲 Confirm on WhatsApp</a>" if order_link else ""}

    <h3>💳 Payment</h3>
    <p>EcoBank: Mustapha Lumeh - 231779276394</p>
    <p>Remitly: Mustapha Lumeh - +231887935222</p>
    '''

# LOGOUT
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)