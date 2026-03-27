from flask import Flask, request, redirect

app = Flask(__name__)

# Temporary storage
accounts = [
    {"name": "Pro Account 🔥", "price": "$10", "desc": "High rated squad"},
    {"name": "Starter Account ⚽", "price": "$5", "desc": "Good for beginners"}
]

@app.route('/')
def home():
    items_html = ""
    for acc in accounts:
        msg = "Hello 🤍, I’m interested in {} ({}) 🩵".format(acc['name'], acc['price'])
        whatsapp_link = f"https://wa.me/231887935222?text={msg}"

        items_html += f"""
        <div class="card">
            <h3>{acc['name']}</h3>
            <p>{acc['desc']}</p>
            <h2>{acc['price']}</h2>
            <a href="{whatsapp_link}" target="_blank">
                <button>Buy via WhatsApp 💬</button>
            </a>
        </div>
        """

    return f'''
    <html>
    <head>
    <title>LOGAN EFB STORE</title>

    <style>
    body {{
        margin:0;
        font-family: Arial;
        background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
        color:white;
        text-align:center;
    }}

    h1 {{
        font-size: 40px;
        margin-top: 20px;
        color: #00ffc3;
    }}

    .container {{
        padding: 20px;
    }}

    .card {{
        background: rgba(255,255,255,0.05);
        margin: 15px;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(0,255,200,0.3);
    }}

    button {{
        padding: 10px 20px;
        border:none;
        border-radius:10px;
        background:#00ffc3;
        font-weight:bold;
        cursor:pointer;
    }}

    button:hover {{
        background:#00cfa0;
    }}

    .admin {{
        margin-top: 30px;
    }}
    </style>

    </head>

    <body>

    <h1>🔥 LOGAN EFB STORE 🔥</h1>
    <p>Buy • Sell • Trade • Exchange Accounts</p>

    <div class="container">
        {items_html}
    </div>

    <div class="admin">
        <h2>Admin Panel</h2>
        <form action="/add" method="post">
            <input name="name" placeholder="Account Name"><br><br>
            <input name="price" placeholder="Price"><br><br>
            <input name="desc" placeholder="Description"><br><br>
            <button type="submit">Add Account</button>
        </form>
    </div>

    </body>
    </html>
    '''

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    price = request.form['price']
    desc = request.form['desc']

    accounts.append({
        "name": name,
        "price": price,
        "desc": desc
    })

    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)